# Manage balance

The balance page gives merchants a comprehensive view of their account funds and management tools, making it easier to monitor financial activity in real-time and resolve any issues. This page includes:

- Viewing and tracking your account balance
- Interpreting key metrics and data points on the balance dashboard
- Managing adjustments and resolving discrepancies effectively

## How to access

Log in to the Genstore admin, then click **Finance** -> **Balance** in the left navigation bar. On this page, you'll see your total account funds and detailed settlement history.

::: tip
You must first activate **Genstore Payments** to use the **Finance** feature.
:::
## Available balance

At the top of the page, you'll find an overview of your total balance and its components. **Available balance** is the sum of all available funds (settling and settled), which can be used for refunds and withdrawals.

- **Available balance**: Represents funds currently undergoing clearing and settlement. You can use these funds to process refunds or handle chargebacks.
  - You can view the specific breakdown under the **Available balance** via the two smaller numbers: the left figure represents the available balance for Standard Products, and the right figure represents the available balance for Dropshipping Products.
  - Note: If these funds include revenue from Dropshipping orders, any refunds must comply with the [Dropshipping Refund Policy](./operate-dropshipping-after-sales-policy.md).
- **In clearing**: Funds currently in the clearing process.
- **In progress**: Funds that have successfully cleared and are currently in the settlement phase.
- **Available for payout**: Settlement successful. Funds will be automatically disbursed according to your Genstore Payments payout schedule.
- **Reserve**: A portion of settled funds is held in the reserve account to cover possible refunds, chargebacks, or other fees, ensuring both buyers and sellers are protected. These funds belong to the merchant but are held in reserve until the order is completed. The **Reserve threshold** is the minimum amount required in the reserve. Funds are only released when the balance exceeds the threshold.

## Clearing history

The table below displays detailed batch information for all payment orders currently in the clearing cycle, helping merchants track and understand fund movements.

| Field Name | Description |
| :--- | :--- |
| **Batch** | The unique identification number of the clearing batch. |
| **Date** | The date when the clearing schedule was completed. |
| **Status** | The status of the clearing batch, typically categorized as: `In clearing`, `Cleared`. |
| **Gross** | The total pending amount of payment orders converted into the settlement currency. |
| **Refund** | The total amount of all refunds processed within the clearing cycle. |
| **Fee** | All costs incurred during the clearing cycle, including payment processing fees, FX conversion fees, or Dropshipping-related charges. |
| **Adjustments** | Adjustments made to the settlement funds due to other reasons or discrepancies. |
| **Net** | The actual amount credited to the available balance after deducting all fees and adjustments from the gross revenue. |


## Settlement history

At the bottom of the page, you'll see a detailed list of all settlement orders, helping you track your funds' activity.

| Field name  | Description                                                            |
| ----------- | ---------------------------------------------------------------------- |
| **Time**        | The timestamp when the settlement took place                                     |
| **Action**    | The type of transaction causing the balance change, including: Settlement Completed, Chargeback Incurred, Transfer Initiated, Refund Processed, Balance Adjustment, and Merchant Top-up.                             |
| **Clear reference** | If the fund change is linked to a specific settlement batch, the corresponding reference number will be displayed here for tracking purposes. |
| **Amount**       |  The total amount of the specific fund change.   |
| **Available**      | The final account balance resulting from this specific fund change.     |
| **Reserve**         |  The effect of this transaction on your reserve balance. Additions to the reserve are shown as positive numbers, while releases/withdrawals from the reserve are shown as negative numbers.            |
| Negative | The effect of this transaction on your negative balance. Contributions to cover a negative balance are shown as positive numbers, while amounts that increase a negative balance or are deducted from it are shown as negative numbers.      |
| Others         | The effect of this transaction on other fund types. If you are using Dropshipping and have made a top-up to cover refunds, you can track the changes to those specific funds in this column.  |

## Payout history

When your funds are in the "Available for payout" balance, they will be sent to your bank account according to your set schedule. Every payout activity will be recorded here.

| Field Name | Description |
| :--- | :--- |
| **Time** | The timestamp when the payout was initiated. |
| **Type** | The type of action, typically categorized as `Payout` or `Transfer`. |
| **Amount** | The total amount for this specific payout. |
| **Transaction reference** | The unique identification number for this payout transaction. |
| **Description** | Additional notes or details regarding this payout, if applicable. |


## Filter function

The balance details page includes a filter feature to help you quickly sort settlement records by date and status. To use the filter:

1. Filter by date range.
2. Filter by status, e.g., **In clearing**, **Cleared**.

Click **Clear** to remove all filters and show the full list of records.
