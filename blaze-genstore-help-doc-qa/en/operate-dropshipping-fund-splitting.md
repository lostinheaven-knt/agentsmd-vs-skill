# Manage fund allocation and settlements

When a customer purchases an order containing **Genstore Dropshipping products** and completes payment, the system automatically handles fund allocation and clearing in the background.
After deducting all relevant fees, the remaining amount is credited to your merchant account balance.

## Fee structure

Each dropshipping order includes the following three fee types before settlement:

| Fee type                   | Description                                                                     |
| -------------------------- | ------------------------------------------------------------------------------- |
| **Payment processing fee** | Charged for processing payments through **Genstore Payments** or **Drop Pay**.                  |
| **Product cost**           | The supplier cost of goods purchased through the Genstore Dropshipping service. |
| **Service fee**            | A system commission charged for using the Genstore Dropshipping service.        |

You can review fee details for each transaction in：
- **Finance** -> **Payments** (with Genstore Payments)
- **Dropshipping** -> **Balance** (with Drop Pay)

## Clearing and settlement cycles

Settlement timing depends on whether the order includes **dropshipping products**.

### 1. Orders containing dropshipping products

Includes:

* Orders with only dropshipping products
* Orders containing both dropshipping and regular products

| **Stage**       | **Duration** | **Description**                                                                                                              |
|-----------------|--------------|------------------------------------------------------------------------------------------------------------------------------|
| **Clearing**    | 45 days      | After the buyer makes the payment, Genstore will complete the funds clearing between the platform and the supplier within 45 days. |
| **Settlement**  | 5 days       | After clearing, Genstore will complete the funds settlement between the platform and the merchant within 5 days.               |
| **Payout**      | -            | Once the funds are successfully settled, they will be transferred to the merchant's account the next day. After the transfer is successful, the system will automatically initiate the payout according to your payment plan and deposit the funds into your designated account. Please note that banks may require additional processing time. |



::: tip
Fund related activities are only processed on weekdays. Activities on non-weekdays will be postponed accordingly.
::: 

### 2. Orders with only regular products

| **Stage**       | **Duration** | **Description**                                                                                                              |
|-----------------|--------------|------------------------------------------------------------------------------------------------------------------------------|
| **Clearing**    | 5 days      | After the buyer makes the payment, Genstore will complete the funds clearing between the platform and the supplier within 5 days. |
| **Settlement**  | 0 days       | Once clearing completes, funds are automatically settled to your bank account at the end of each day. Slight delays may occur depending on the bank.         |
| **Payout**      | -            | Once the funds are successfully settled, they will be transferred to the merchant's account the next day. After the transfer is successful, the system will automatically initiate the payout according to your payment plan and deposit the funds into your designated account. Please note that banks may require additional processing time. |



## Notes

* Funds will only be credited to your available balance after settlement is complete. The withdrawable portion will be automatically withdrawn to your linked bank account in batches according to your schedule configuration.
* Funds can only be withdrawn **after the clearing cycle ends**.
* If an order contains both dropshipping and regular products, the **45-day clearing cycle** applies to the entire order.
* All transaction and deduction records are available under 
  * **Finance -> Payments -> Transactions** (with Genstore Payments)
  * **Dropshipping** -> **Balance** (with Drop Pay)
* Bank transfer times may vary depending on region and account type.
