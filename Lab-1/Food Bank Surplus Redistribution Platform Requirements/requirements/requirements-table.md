# Requirements Table

This document contains the functional and non-functional requirements for the **Food Bank Surplus Redistribution Platform**.

## Functional Requirements

| ID | Type | Requirement Description | Priority | Acceptance Criteria | Rationale | Use Case Ref |
|---|---|---|---|---|---|---|
| **FR-001** | Functional | The system shall allow donor partners (restaurants and grocery stores) to post surplus edible food batches with quantity, expiry time, and dietary tags. | High | **Pass:** A donor can create a food batch listing with all required fields and the listing is visible to shelters.<br>**Fail:** A valid listing submission is rejected or missing from the active claim board. | Capturing structured batch details enables shelters to quickly identify suitable and safe food donations. | UC-01 |
| **FR-002** | Functional | The system shall allow verified shelter coordinators to browse available food batches and reserve pickup windows before food expiry. | High | **Pass:** A verified shelter can reserve an available pickup slot for a valid food batch.<br>**Fail:** Shelter reservation is allowed after expiry or reservation for unavailable slots is accepted. | Reservation workflow reduces food wastage and ensures timely redistribution to beneficiaries. | UC-02 |
| **FR-003** | Functional | The system shall prevent expired food batches from remaining active on the claim board and automatically mark them unavailable. | High | **Pass:** A batch becomes unavailable immediately after expiry and cannot be reserved.<br>**Fail:** An expired batch remains visible as active or allows new reservations. | Automated expiry handling is critical for food safety and operational trust. | UC-03 |
| **FR-004** | Functional | The system shall generate and share pickup verification details between donor partners and shelter coordinators after a successful reservation. | Medium | **Pass:** Reservation confirmation includes pickup details/verification for both parties.<br>**Fail:** Reservation is marked successful without delivering pickup verification information. | Pickup verification reduces coordination errors during handover. | UC-02 |
| **FR-005** | Functional | The system shall notify nearby verified shelters when high-quantity perishable food batches are newly listed. | Medium | **Pass:** Eligible nearby shelters receive notifications for matching new listings.<br>**Fail:** No notification is triggered for a qualifying high-priority listing. | Timely alerts improve pickup rates for perishable surplus food. | UC-04 |

## Non-Functional Requirements

| ID | Type | Requirement Description | Priority | Acceptance Criteria | Rationale | Use Case Ref |
|---|---|---|---|---|---|---|
| **NFR-001** | Performance | The platform shall dispatch push notifications to eligible shelters within 5 seconds for high-priority perishable listings inside a 5 km radius. | High | **Pass:** Performance tests show notification dispatch within 5 seconds under expected load.<br>**Fail:** Notification dispatch exceeds the maximum response window during normal operations. | Low-latency alerts are essential to reserve perishable food before expiry. | N/A |
| **NFR-002** | Security and Reliability | The platform shall allow only verified donor and shelter accounts to create listings, reserve pickups, and access reservation details. | High | **Pass:** Unauthorized or unverified users are blocked from protected actions and data.<br>**Fail:** Unverified users can post, reserve, or access restricted reservation information. | Access control protects safety, trust, and data integrity across the redistribution network. | N/A |
