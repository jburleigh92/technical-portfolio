# Technical Portfolio — Jason Burleigh
Solutions Engineer | Systems Integration Lead | Technical Operations

This portfolio documents my end-to-end systems engineering work: API integrations, workflow automation, multi-platform architecture design, and data-driven operational tooling. All projects in this repository were designed, implemented, and deployed into real production environments with live customers, real transactions, and operational dependencies.

I specialize in building reliable automation layers across fragmented platforms, transforming manual workflows into scalable systems, and translating operational constraints into technical architecture. My background spans POS systems, logistics routing platforms, loyalty systems, eCommerce, webhook orchestration, and custom Python microservices.

---

## Core Strengths

**Systems Architecture**
- Designing multi-system workflows connecting POS, dispatch, eCommerce, CRM, loyalty, and internal tooling  
- Mapping data flows, defining integration logic, and building resilience around third-party API limitations  

**API Integrations & Automation**
- REST APIs, webhooks, OAuth2 authentication  
- Building Python microservices and webhook listeners (Flask)  
- Automated data extraction from structured and unstructured sources  
- Real-time notification and event-driven processing  

**Data Normalization & Catalog Management**
- Standardizing inconsistent vendor data across 50+ sources  
- Designing naming conventions, taxonomy rules, and catalog mapping logic  
- Implementing automated cleaning, extraction, and classification workflows  

**Technical Operations & Reliability**
- Troubleshooting POS, eCommerce, logistics, and CRM system failures  
- Creating SOPs, operational diagnostics, and cross-team communication frameworks  
- Rapid debugging and issue triage in production environments  

---

## Highlighted Projects in This Portfolio

### Payment Verification Engine (PostPay)
A unified Python-based automation system that eliminated manual payment verification delays.  
Key components include:
- Gmail API extraction (OAuth2) for real-time payment notifications  
- MacOS iMessage database parsing for Zelle/SMS verification  
- SQLite storage with deduplication and timestamp filtering  
- Slack API notifications for dispatch and driver workflows  
- End-to-end logic that reduced verification delays from 10–15 minutes to near-instant  

### Webhook Listener & ETA Extraction Service (WhListen)
A Flask-based microservice that:
- Listens to Tookan dispatch webhooks  
- Extracts ETAs, verification events, and status updates  
- Uses Selenium to pull additional dynamic data when needed  
- Triggers customer messages and downstream workflow actions  
- Supports real-time delivery visibility and automated routing logic  

### Loyalty Auto-Enrollment System
Designed to remove the need for manual onboarding by:
- Intercepting dispatch verification events  
- Creating or updating profiles via Alpine IQ API  
- Applying points, opt-ins, and SMS notifications programmatically  
- Replacing manual UI flows with a fully automated pipeline  

### Multi-Platform eCommerce Architecture
Co-architected front- and back-end integrations connecting:
- Blaze POS  
- Tookan (dispatch)  
- Alpine IQ (CRM/loyalty)  
- WooCommerce (storefront)  
- Slack API (operational observability)  
- Custom Python services for data flow and automation  

This work included API mapping, catalog synchronization, error handling logic, webhook workflow definition, and supporting two iterations of a production storefront.

---

## Technical Domains Represented

- Python automation  
- REST API design and integration  
- Webhook orchestration  
- Data parsing and normalization  
- SQLite and lightweight data persistence  
- Selenium for dynamic data extraction  
- Slack API messaging workflows  
- POS, logistics, and loyalty integrations  
- eCommerce and catalog systems  
- Operational reliability engineering  

---

## Purpose of This Portfolio

This repository serves as a technical demonstration of my ability to:
- Architect complex, multi-platform integrations  
- Build automation systems that directly improve operational performance  
- Reverse engineer undocumented or partially documented workflows  
- Debug and stabilize production environments with real users and real systems  
- Translate operational constraints into scalable technical solutions  

All code samples, diagrams, and documentation reflect real projects used in production environments supporting daily operations, live orders, payments, and integrations.

