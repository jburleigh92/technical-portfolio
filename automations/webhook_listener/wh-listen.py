from flask import Flask, request, jsonify
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        # Run your custom script logic here
        run_custom_script(data)
        print("Script executed successfully.")
    except Exception as e:
        print(f"Script execution failed: {e}")

    return jsonify(status='success'), 200

def run_custom_script(data):
    # Extract customer_phone and tracking_link
    customer_phone = data.get('customer_phone', '')
    full_tracking_link = data.get('full_tracking_link', '')
    
    # Format phone number to 10 digits
    formatted_phone = ''.join(filter(str.isdigit, customer_phone))[-10:]
    
    # Extract ETA from the tracking link
    eta = extract_eta_from_tracking_link(full_tracking_link)
    
    # Generate ETA window
    eta_window = generate_eta_window(eta)
    
    # Print extracted data for verification
    print("Extracted customer_phone:", formatted_phone)
    print("Extracted ETA:", eta)
    print("Generated ETA window:", eta_window)
    
    # Opt-in the user
    opt_in_user(formatted_phone)
    
    # Send SMS with the extracted ETA window
    send_sms(formatted_phone, eta_window)

def opt_in_user(phone):
    uid = "3561"
    status = "true"  # or "false" depending on the desired opt-in status
    url = f"https://lab.alpineiq.com/api/v2/optin/text/{phone}/{status}"
    headers = {
        "X-APIKEY": "5SjCibqe6mqffgS2Zq3PBA1It06WwyxD7DwVLj3QGIIkaJLMonQbTU5OWw",
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, headers=headers)
    
    if response.status_code == 200:
        print("Opt-in API call successful.")
    else:
        print(f"Failed to update SMS opt-in status. Status code: {response.status_code}")
        print(response.text)

def send_sms(phone, eta_window):
    url = "https://lab.alpineiq.com/api/v2/sms"
    headers = {
        "Content-Type": "application/json",
        "X-APIKEY": "5SjCibqe6mqffgS2Zq3PBA1It06WwyxD7DwVLj3QGIIkaJLMonQbTU5OWw"
    }
    
    # Determine the message body based on the ETA window
    if eta_window == "N/A":
        message_body = "Your order is on the way!"
    else:
        message_body = f"Your order is on the way! ETA: {eta_window}"
    
    data = {
        "body": message_body,
        "campaignID": "3561",  # Optional, you can remove this if not needed
        "phone": phone
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("SMS sent successfully.")
    else:
        print(f"Failed to send SMS. Status code: {response.status_code}")
        print(response.text)

def extract_eta_from_tracking_link(tracking_link):
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use webdriver_manager to handle ChromeDriver installation and setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(tracking_link)

    try:
        # Wait for the page to load and the ETA element to be present
        wait = WebDriverWait(driver, 20)
        eta_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "ETA")]')))
        eta_text = eta_element.text
        eta = eta_text.split(': ')[1].replace(' min', '')
    except Exception as e:
        print(f"Failed to extract ETA: {e}")
        eta = "N/A"
    finally:
        driver.quit()
    
    return int(eta) if eta.isdigit() else eta

def generate_eta_window(eta):
    if eta == "N/A":
        return "N/A"
    eta = int(eta)
    if eta <= 5:
        return "5-10 mins or less"
    elif eta <= 10:
        return "10-15 mins"
    elif eta <= 15:
        return "15-20 mins"
    elif eta <= 20:
        return "20-30 mins"
    elif eta <= 30:
        return "25-35 mins"
    elif eta <= 45:
        return "30-45 mins"
    elif eta <= 60:
        return "45-60 mins"
    elif eta <= 90:
        return "60-90 mins"
    else:
        return "90-120 mins"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
