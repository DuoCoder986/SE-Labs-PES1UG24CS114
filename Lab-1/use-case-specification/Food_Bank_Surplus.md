# Use Case Specification: Reserve Pickup Window

## 1. Use Case Name

**Reserve Pickup Window (UC-02)**

## 2. Summary / Description

This use case describes how a **verified Shelter Coordinator** browses available surplus food batches and reserves a suitable pickup window before the food expires.

The system verifies that the shelter is authorized, checks that the selected food batch is still available and has not expired, and confirms the reservation. After a successful reservation, the system provides pickup verification details to the shelter and donor partner.

This use case supports the platform's primary objective of enabling timely redistribution of surplus edible food from restaurants and grocery stores to verified local shelters.

## 3. Actors

### Primary Actor

* **Shelter Coordinator (Verified Shelter)**

### Supporting Actors

* **Donor Partner (Restaurant / Grocery Store)**
* **System Administrator** — monitors reservation and activity information.

## 4. Preconditions

1. The Shelter Coordinator has a registered and verified shelter account.
2. The Food Bank Surplus Redistribution Platform is available.
3. At least one food batch is listed by a donor partner.
4. The selected food batch has not expired.
5. The selected food batch is currently available for reservation.
6. A valid pickup window is associated with the food batch.

## 5. Postconditions

### Success Postconditions

* The selected food batch is reserved for the verified shelter.
* The selected pickup window is recorded against the reservation.
* The food batch is no longer available for conflicting reservations.
* Pickup verification details are generated and provided to the relevant parties.
* The reservation/activity is recorded in the system logs.

### Failure Postconditions

* No reservation is created.
* The food batch remains available if it has not expired.
* The Shelter Coordinator is informed of the reason for reservation failure.

## 6. Main Flow (Basic Flow)

1. The **Shelter Coordinator** logs into the platform using a verified account.

2. The system verifies that the Shelter Coordinator is authorized to perform reservation operations.

3. The Shelter Coordinator selects **Browse Available Food Batches**.

4. The system displays currently available surplus food batches.

5. The Shelter Coordinator selects a suitable food batch.

6. The system displays the selected food batch details, including:

   * Quantity
   * Expiry time
   * Dietary tags
   * Available pickup information

7. The Shelter Coordinator selects an available **pickup window**.

8. The system validates the food batch's availability and expiry status.

9. If the food batch is available and has not expired, the system creates the reservation.

10. The system records the selected pickup window for the reservation.

11. The system generates **pickup verification details** for the reservation.

12. The system provides the pickup verification details to the Shelter Coordinator.

13. The relevant reservation information is made available to the Donor Partner for the food handover.

14. The system records the successful reservation in the activity logs.

15. The system displays a reservation confirmation to the Shelter Coordinator.

## 7. Alternative Flows

### Alt-1: Food Batch Expires Before Reservation Confirmation

* At step 8, if the food batch has expired before the reservation is completed:

  1. The system rejects the reservation.
  2. The system marks the food batch as unavailable.
  3. The expired batch is removed from the active claim board.
  4. The Shelter Coordinator is informed that the food batch can no longer be reserved.
  5. The use case ends unsuccessfully.

### Alt-2: Selected Pickup Window Is Unavailable

* At step 8, if the selected pickup window has already been reserved:

  1. The system rejects the selected pickup window.
  2. The system informs the Shelter Coordinator that the window is unavailable.
  3. The system displays other available pickup windows, if any.
  4. The Shelter Coordinator may select another available window.
  5. The use case continues from step 7.

### Alt-3: Food Batch Is Already Reserved

* At step 8, if another verified shelter has already reserved the food batch:

  1. The system prevents the new reservation.
  2. The system informs the Shelter Coordinator that the batch is unavailable.
  3. The Shelter Coordinator may return to the available food batch list.
  4. The use case ends or continues with another batch selection.

## 8. Exception Flows

### Exc-1: Unverified Shelter Account

1. At step 2, if the Shelter Coordinator's account is not verified:

   * The system denies access to the reservation operation.
   * The system displays an authorization error.
   * No reservation is created.
   * The use case ends unsuccessfully.

### Exc-2: Food Batch Becomes Unavailable During Reservation

1. At step 8, if the food batch becomes unavailable while the reservation is being processed:

   * The system cancels the reservation attempt.
   * The system informs the Shelter Coordinator that the batch is no longer available.
   * No conflicting reservation is created.
   * The use case ends unsuccessfully.

### Exc-3: System Failure During Reservation

1. If a system error occurs while creating the reservation:

   * The system does not confirm the reservation.
   * The system records the failure where possible.
   * The Shelter Coordinator receives an error message.
   * The Shelter Coordinator may retry the reservation later.

## 9. Related Use Cases

* **Browse Available Food Batches**
* **View Food Batch Details**
* **Validate Food Availability & Expiry**
* **Receive Pickup Verification Details**
* **Monitor Food Expiry**
* **Mark Batch Unavailable**
* **Remove Expired Batch from Claim Board**
* **View Reservation & Activity Logs**

## 10. UML Relationships

The use case corresponds to the relationships shown in the UML diagram:

* **Reserve Pickup Window** `<<include>>` **Validate Food Availability & Expiry**
* **Reserve Pickup Window** `<<include>>` **Receive Pickup Verification Details**
* **Browse Available Food Batches** `<<include>>` **View Food Batch Details**
* **Reserve Pickup Window** `<<extend>>` **Monitor Food Expiry** for the conditional expiry situation.

## 11. Requirement Traceability

| Requirement | Relationship to Use Case                                                                              |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| **FR-002**  | Primary requirement — verified shelters browse food batches and reserve pickup windows before expiry. |
| **FR-003**  | Supports reservation validation by preventing expired batches from being reserved.                    |
| **FR-004**  | Successful reservation generates and shares pickup verification details.                              |
| **NFR-002** | Ensures only verified shelter accounts can perform protected reservation operations.                  |

## 12. Acceptance Outcome

**Pass:** A verified Shelter Coordinator can select an available food batch, reserve a valid pickup window before expiry, and receive pickup verification details.

**Fail:** An expired or unavailable food batch/pickup window is successfully reserved, or an unverified shelter is allowed to perform the reservation.
