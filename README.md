# 🚀 Baked Budz — Full Technical Systems Portfolio  
### **Jason Burleigh — Solutions Engineer / Integration Architect**

This repository documents the complete set of systems, integrations, automations, and engineering work I designed, implemented, and maintained for the Baked Budz delivery operation.  
It includes all major components involved in order intake, customer verification, dispatch workflows, real-time driver tracking, automated payment verification, loyalty enrollment, and cross-system notifications.

The system connected multiple platforms and automated nearly every operational step from the moment an order was placed until loyalty points were awarded.

---

# 🧩 HIGH-LEVEL ARCHITECTURE (A→Z)

This end-to-end system integrated:

- **Weedmaps** — primary external ordering channel  
- **BakedBudz.store** — custom WordPress/WooCommerce eCommerce site (v1 Blaze plugin → v2 standalone API-driven integration)  
- **Blaze POS** — system of record for orders, customers, catalog, and compliance  
- **Tookan** — dispatch engine, driver telemetry, and webhook events  
- **Gmail API / Google OAuth2** — ingestion of Zelle, Venmo, Cash App, and Apple Pay payment notifications  
- **MacOS iMessage SQLite DB** — real-time Zelle SMS extraction  
- **SQLite** — state, deduplication, event storage, and payment matching  
- **Slack API** — automated operational notifications  
- **Alpine IQ** — loyalty enrollment and SMS delivery  
- **Custom Python services** — PostPay payment engine, webhook listeners, verification logic, API orchestrators  

All components worked together to form a unified automated operations pipeline.

---

# 🔧 TECHNOLOGIES & SKILLS USED

### **API & Integration Engineering**
- REST APIs (Blaze, Tookan, Alpine, Slack)
- Webhooks (Blaze POS → Tookan → custom listeners)
- JSON parsing and transformation
- API authentication (API keys, headers, tokens)
- Reverse-engineering undocumented API behavior
- Data mapping between mismatched systems

### **Automation & Backend Engineering**
- Python (core automation scripts)
- Flask (webhook servers)
- Selenium (ETA extraction automation for Tookan tracking links)
- SQLite (local DB for payment verification state)
- Cron-style continuous processes
- Heroku runtime for cloud-hosted components
- Local MacOS runtime for iMessage extraction
- Multi-layer error handling and resilience logic

### **Debugging & Reliability Work**
- Regex extraction patterns for payment messages
- Timestamp filtering to prevent stale events
- Deduplication logic to avoid double-processing
- Cross-provider format normalization
- Payment-source discrepancy handling (email vs SMS)
- Log-based troubleshooting and historical replay testing

### **Operational System Design**
- End-to-end process design
- SOP and workflow definition
- Vendor API research and integration planning
- Real-world incident triage
- Multi-system rollout and staff onboarding

---

# 🧠 FLAGSHIP PROJECTS

## ⭐ 1. **PostPay — Automated Payment Verification Engine**

**Purpose:**  
Remove dispatcher delays by verifying Zelle, Cash App, Venmo, and Apple Pay payments automatically.

### **Data ingestion**
- Gmail API (OAuth2) to ingest email notifications  
- MacOS iMessage SQLite parsing for Zelle SMS  
- Regex patterns for payment type + sender + amount  
- Timestamp-bound filtering to avoid stale messages  

### **Processing & storage**
- Normalization of inconsistent formats across payment providers  
- SQLite event store with deduplication  
- Order-matching logic  
- Cross-day filtering to avoid reprocessing older payments  

### **Output**
- Slack API notifications automatically sent to dispatch and drivers  
  - Example:  
    `Payment Verified — Order #1234 — $75.00 received via Cash App`

### **Operational impact**
- Eliminated 10–15 min delays  
- Prevented drivers from being stalled at the customer’s door  
- Reduced cancellations and ETA disruptions  
- Verified ~50 orders/day during peak hours  


---

## ⭐ 2. **whlisten.py — Real-Time Webhook Listener + ETA Engine**

**Purpose:**  
Consume Tookan webhooks, extract tracking links, determine ETA ranges, and trigger post-verification workflows.

### **Core responsibilities**
- Flask webhook endpoint for Tookan events  
- Parsing task metadata including tracking URLs  
- Selenium-based ETA extraction when API didn't expose ETA  
- ETA → window conversion (e.g., “15–20 mins”)  
- Triggering opt-in, loyalty, and SMS flows  
- Slack operational notifications  
- Continuous runtime with error logging

---

## ⭐ 3. **Alpine Auto-Enrollment Engine**

**Purpose:**  
Bypass Alpine IQ’s manual enrollment flow and automatically enroll customers into loyalty + send SMS after verification.

### **How it worked**
- Tookan "Verified Customer" event triggered the workflow  
- Checked Alpine for an existing profile  
- Created profile if missing  
- Updated opt-in status via:  
  `PUT /optin/text/{phone}/{status}`  
- Triggered automated SMS via Alpine API  
- Ensured enrollment only occurred after verified orders  

### **Impact**
- Removed manual customer onboarding  
- Standardized customer experience  
- Kept loyalty program fully automated and synchronized to real behavior  

---

# 🔥 COMPLETE PIPELINE (ORDER → DELIVERY → PAYMENT → LOYALTY)

The overall automated workflow I designed:

1. **Order placed**
   - Weedmaps or BakedBudz.store v1/v2  
   - Routes into Blaze POS  

2. **Customer verification**
   - Automated logic to confirm returning/new customer status  
   - Allowed or blocked order progression  

3. **Dispatch creation**
   - Blaze → Tookan API  
   - Driver assignment  

4. **Driver verification events**
   - Tookan → webhook listener  
   - Extracted tracking link + ETA  

5. **Payment verification**
   - PostPay → email + SMS extraction  
   - Matches payment to order  
   - Slack notification  

6. **Loyalty flow**
   - Verified event triggers Alpine flow  
   - Auto-enrollment + SMS  

7. **Notifications**
   - Slack keeps team updated on all key events  

This represents the fully integrated, automated operations ecosystem.

---

# 📂 REPO STRUCTURE

project-root/                           ← GitHub repo name: "technical-portfolio"
│
├── README.md                           ← Full rewritten version you approved
│
├── architecture/
│     ├── system-diagram.md             ← Full system A→Z
│     ├── data-flow.md                  ← Order → Verification → Payment → Dispatch → Loyalty
│
├── automations/
│     ├── webhook_listener/
│     │       ├── wh-listen.py          ← Uploaded file
│     │       └── README.md             ← Explains Tookan→Alpine logic
│     │
│     ├── alpine_enroll/
│     │       ├── alpine_enroll.py      ← Enrollment logic
│     │       └── README.md
│     │
│     ├── verification_flow/
│     │       ├── verification_flow.md
│     │       └── flow_diagram.png
│     │
│     ├── postpay/                      ← Full evolution of payment engine
│     │       ├── PostPay1.3.2.py
│     │       ├── PostPay2.1.1.py
│     │       ├── PostPay3.2.1.py
│     │       ├── PostPay4.py
│     │       ├── schema.md             ← Message regex patterns, DB schema, logic
│     │       └── README.md
│     │
│     └── payment_verification.py       ← Final standalone verification logic
│
├── api-tests/
│     ├── blaze.postman_collection.json
│     ├── tookan.postman_collection.json
│     ├── alpine.postman_collection.json
│
├── docs/
│     ├── blaze-api-notes.md
│     ├── alpine-api-research.md
│     ├── webhook-debugging-log.md
│     ├── integration_challenges.md
│     ├── operations_architecture.md
│     └── slack-notification-flow.md
│
└── samples/
      ├── tookan_webhook.json
      ├── alpine_enroll_request.json
      └── alpine_enroll_response.json
      
---

# 📬 CONTACT  
**LinkedIn:** https://www.linkedin.com/in/jason-burleigh  
**Email:** jburleigh1992@gmail.com  

---

# 🏁 END OF README

