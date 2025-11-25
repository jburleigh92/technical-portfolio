**# System Architecture — End-to-End Delivery Platform

This document provides a full technical overview of the integrated ordering, dispatch, verification, payment-processing, and loyalty-automation system built for Baked Budz.  
It includes the global architecture plus subsystem-specific diagrams for:  

1. Order Intake Flow  
2. Dispatch Flow  
3. Payment Verification Engine  
4. Loyalty Enrollment Engine  

This represents the complete production workflow used daily for all real customers, orders, payments, and post-order lifecycle events.

---

# 1. Full System Architecture (A→Z)

            +---------------------------+
            |      Weedmaps (WM)        |
            +-------------+-------------+
                          |
                          v
+-----------------------------+------------------------------+
|                     Order Intake Layer                     |
|  +---------------------------+  +-------------------------+ |
|  | BakedBudz.store (v1/v2)   |  |    Direct SMS Orders    | |
|  +---------------------------+  +-------------------------+ |
+-----------------------------+------------------------------+
                          |
                          v
                    +---------------------+
                    |     Blaze POS       |
                    |   (Order Creation)  |
                    +---------+-----------+
                              |
                              v
                   +----------------------+
                   | Customer Verification |
                   |    (Automated Logic) |
                   +----+--------------+---+
                        |              |
      Verified ----------              -------- Not Verified
                        |                           |
                        v                           v
           +----------------------+         (Pipeline Halted)
           | Tookan Dispatch API  |
           +----------+-----------+
                      |
                      v
        +--------------------------------+
        | Driver Assigned / ETA Tracking |
        +--------------------------------+
                      |
                      v
            +------------------------+
            | Payment Verification   |
            |    (PostPay Engine)   |
            +-----------+------------+
                        |
          Payment OK ---+--- Payment Error
                        |
                        v
       +--------------------------------------+
       | Alpine Loyalty (Auto Enrollment +    |
       |     SMS Notifications via API)       |
       +--------------------------------------+
                        |
                        v
             +--------------------------+
             | Slack Notifications      |
             | (Dispatch + Driver Ops)  |
             +--------------------------+

---

# 2. Subsystem Diagram — Order Intake Flow

       +---------------------+
       |   Weedmaps API      |
       +---------------------+
                 |
                 v
    +---------------------------+
    | Blaze POS — Order Created |
    +---------------------------+
                 |
                 v
+-------------------------------------------+
| Customer Verification Script               |
| • Validates ID                             |
| • Checks returning vs new customer         |
| • Ensures compliance                       |
+------------------+-------------------------+
                   |
          Verified |
                   v
       Order eligible for dispatch

---

# 3. Subsystem Diagram — Dispatch Flow (Tookan)

            +--------------------+
            | Blaze → Tookan API |
            +--------------------+
                     |
                     v
            +----------------------+
            | Tookan Task Created  |
            +----------------------+
                     |
               Driver Assigned
                     |
                     v
  +----------------------------------+
  | Tookan Event Webhooks            |
  | (Arrived, On The Way, Verified)  |
  +------------------+---------------+
                     |
                     v
         +------------------------+
         | Webhook Listener (wh) |
         | • Parses event         |
         | • Extracts ETA         |
         +------------------------+

---

# 4. Subsystem Diagram — Payment Verification Engine (PostPay)

              +------------------------+
              |    Payment Services    |
              | • Zelle                |
              | • Cash App             |
              | • Venmo                |
              | • Apple Pay            |
              +-----------+------------+
                          |
               Email or SMS Notification
                          |
                          v
 +-----------------------------------------------------+
 |                  Extraction Layer                   |
 | • Gmail API (OAuth2) reads payment emails           |
 | • MacOS iMessage DB parser extracts SMS payments    |
 | • Regex + timestamp filtering                       |
 +---------------------------+-------------------------+
                             |
                             v
           +-----------------------------+
           |   Payment Database (SQLite) |
           | • Deduplication             |
           | • Cross-day filtering       |
           | • Order matching logic      |
           +--------------+--------------+
                             |
                             v
             +------------------------------+
             |   Slack Notification Engine   |
             |  "Payment Verified: …"        |
             +------------------------------+

---

# 5. Subsystem Diagram — Loyalty Enrollment (Alpine IQ)

      +--------------------------+
      |   Tookan Verified Event  |
      +------------+-------------+
                   |
                   v
      +---------------------------+
      | Alpine Enrollment Script  |
      | • Profile lookup          |
      | • Auto-create if missing  |
      | • Apply loyalty points    |
      | • Send SMS via API        |
      +---------------------------+
                   |
                   v
    +------------------------------+
    | Slack Confirmation Message   |
    | "Customer enrolled + points" |
    +------------------------------+

---

# 6. Component Explanations

## Blaze POS
- System of record for orders  
- Sends immediate webhooks  
- Normalizes catalog & compliance metadata  

## Tookan
- Real-time driver status model  
- Authoritative “customer verified” event  
- Tracking link + ETA source  

## PostPay Engine
- Unified email + SMS parsing  
- Database-backed deduplication  
- Slack driver communication  

## Alpine IQ
- Loyalty program API  
- Auto enrollment  
- Transactional SMS  

## Slack API
- Central operational communication  
- Automated pipeline updates  

---

# 7. Future Enhancements

- Replace Selenium ETA scraping with Tookan ETA API  
- Containerize PostPay in Docker  
- Use Cloud Run for webhook listener  
- Add structured logging + monitoring (Sentry/Datadog)  
- Build unified “customer ledger” microservice  

---

# ✔ End of `system-diagram.md`
**
