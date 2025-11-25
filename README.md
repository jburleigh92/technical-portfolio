# Jason Burleigh — Technical Portfolio
**Solutions Engineer & Technical Operations Specialist**  
API Integrations • Workflow Automation • POS & Logistics Systems • SaaS Implementation

This portfolio showcases the real production systems I architected and automated across a multi-platform cannabis delivery operation. My work spans API orchestration, webhook design, data extraction pipelines, automation scripting, reverse-engineering system limitations, and building reliable end-to-end workflows across POS, logistics, eCommerce, CRM/loyalty, and payment systems.

I have spent the last decade building operationally critical systems for fast-paced environments. Many of these projects replaced fully manual processes and became the backbone of day-to-day operations—supporting 900+ SKUs, 50+ daily orders, $60K+ monthly revenue, and multiple dispatchers/drivers.

---

## ⭐ **Flagship Systems**

### **1. PostPay — Real-Time Payment Verification Engine**  
**Python · Gmail API (OAuth2) · iMessage DB Parsing · Slack API · SQLite · Webhooks · MacOS automation**

A full end-to-end system that automated all incoming payment verification (Zelle, Cash App, Venmo, Apple Pay).  
Key capabilities:

- Gmail API (OAuth2) pipeline to read and parse payment notifications  
- Reverse-engineered iMessage SQLite database to parse Zelle SMS (required because banks delayed email at night)  
- Timestamp + pattern matching to avoid duplicate or stale payments  
- SQLite-backed event storage for reliable state tracking  
- Slack API messaging to dispatchers and drivers  
- Continuous runtime on local Mac + Heroku-triggered components  
- Reduced delays from **10–15 minutes → instant**, eliminating delivery bottlenecks

This system became one of the core operational engines for the business.

---

### **2. Alpine IQ Auto-Enrollment & Loyalty Automation**  
**Tookan Webhooks · Blaze POS · Alpine IQ API · Python · SMS automation**

Alpine IQ required user-initiated enrollment, which broke the customer experience.  
I rebuilt the enrollment logic using:

- Tookan webhooks (more reliable than Blaze order events for verification timing)  
- Conditional logic based on order verification status  
- Alpine IQ API to automatically create + enroll users  
- Automatic SMS confirmation using Alpine’s messaging API  
- Fully hands-off loyalty flow with accurate, verified enrollment only after ID check

Result:  
**100% automated loyalty enrollment, unified point assignment, and SMS notification flow.**

---

### **3. Full Order Pipeline Orchestration (Weedmaps → Blaze → Tookan → Alpine IQ → Slack)**  
**API Design · Architecture · Webhooks · Data Mapping · Operational Engineering**

I authored the end-to-end architecture for the order flow:

1. **Weedmaps or bakedbudz.store** receives order  
2. Blaze POS pulls the order through its marketplace API  
3. Customer verification logic triggers  
4. Tookan handles the dispatch + realtime driver updates  
5. Loyalty enrollment automation triggers  
6. PostPay verifies payment  
7. Slack notifies driver + dispatcher  

This system connected **7+ platforms** using webhooks, API polling, and scripted logic—replacing what used to be 100% manual.

---

### **4. bakedbudz.store (v1 → v2) — Full eCommerce Architecture & Integration Layer**  
**WordPress/WooCommerce · Blaze Store API · Custom Developer Collaboration · System Design**

I led the technical design for two versions of the eCommerce storefront:

- **v1:** Used Blaze’s legacy plugin + outdated Store API → constant limitations + bugs  
- **v2:** Fully custom WordPress/WooCommerce store  
  - No dependency on Blaze frontend  
  - Custom workflows for menu sync, order routing, tracking UI  
  - Designed to support future white-labeling  
  - Allowed more integrations and custom logic

My role:  
Architecture, API strategy, system requirements, developer collaboration, testing, and operational modeling.

---

## 🔧 **Core Technical Skills**

### **Integrations & APIs**
REST APIs · Webhooks · JSON · API authentication  
Blaze POS · Onfleet · Tookan · Alpine IQ · Weedmaps API  
Slack API · Gmail API (OAuth2) · WordPress/WooCommerce APIs  

### **Data Extraction & Automation**
Python (automation + API clients)  
SQLite · ETL-style data pipelines  
Regex parsing · iMessage database extraction (MacOS)  
Data mapping · Catalog synchronization · Inventory logic  

### **Tools & Platforms**
Postman · Git · Heroku · Google Cloud · Selenium  
Google Workspace automation · Zapier · Make  

### **Technical Operations**
System configuration · Vendor onboarding  
SOP development · Incident debugging  
Monitoring and failure-mode design  
Cross-functional communication  
Scaling platforms and workflows  

---

## 📁 **Repository Structure**

### **/architecture/**
System diagrams and data-flow documentation (order → verification → dispatch → loyalty → payment).

### **/automations/**
Python scripts + workflow explanations:
- PostPay (v1 → v4)
- Alpine enrollment automation
- Verification logic
- Webhook handlers

### **/api-tests/**
Postman collections + API note bundles:
- Blaze
- Tookan
- Alpine IQ

### **/docs/**
Engineering notes:
- Debugging logs
- Integration challenges
- Architecture decisions
- Reverse-engineering notes (iMessage DB)

---

## 🎯 **What This Portfolio Demonstrates**

- Ability to design and deploy **multi-system, production-critical integrations**  
- Experience with **API ecosystems**, authentication, and CI-style automation  
- Skill in **reverse engineering** undocumented systems (iMessage DB)  
- Hands-on operational problem solving with measurable outcomes  
- Strong communication through diagrams, docs, and technical writeups  
- Deep understanding of **POS, logistics, eCommerce, and CRM** systems  

This is not a collection of “tutorial code.”  
These are **real production systems** that ran daily business operations end-to-end.

---

## 📬 Contact

**LinkedIn:** https://www.linkedin.com/in/jason-burleigh  
**Email:** jburleigh1992@gmail.com

---

## ⚙️ How to Use This Repo  
Browse the markdown files directly or navigate the rendered version via GitHub Pages once deployed.

