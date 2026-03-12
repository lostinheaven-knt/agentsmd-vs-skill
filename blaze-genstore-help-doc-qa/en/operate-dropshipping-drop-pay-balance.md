# Balance page overview

Funds collected via Drop Pay are managed under the **Dropshipping** -> **Balance** -> **Drop Pay** view. This dashboard allows you to monitor your capital flow in real-time—from initial payment and clearing to final settlement and payout.

## Core metrics

* **Available balance:** The total amount currently available for refunds or dispute resolution. This includes total revenue, funds in clearing, and funds in settlement. *Note: Only "Settled" funds are eligible for payout.*
* **Reserve:** To protect both buyers and sellers, a portion of settled funds is held in a Reserve account to cover potential refunds or chargebacks. These funds belong to the merchant and are unfrozen once the order cycle is complete.
    * **Reserve threshold:** This is the minimum required balance for your reserve. Funds are only released for payout when the reserve balance exceeds this threshold.
* **Payable balance:** The amount that has finished the settlement process and is ready to be transferred to your PayPal account.

## Transaction monitoring

The list at the bottom of the page allows you to track every individual transaction processed through Drop Pay.

### Payments
This section shows the status of all transactions (Authorized, Refunded, etc.), risk scores, and the net amount after costs.

| Field | Description |
| :--- | :--- |
| **Create time** | The timestamp when the payment transaction was initiated. |
| **Payment reference number** | The unique ID for the transaction. Click the number to view a sidebar with full details, including processing fees, dropshipping cost breakdowns, and an event timeline. |
| **Status** | Current state of the payment (e.g., Authorized, Captured, Cancelled, Refunded, Partially Refunded). |
| **Orders** | Linked order ID. One payment usually equals one order, though multiple orders may appear if a checkout contained both physical and digital goods. |
| **Customer** | The customer's email address associated with the payment. |
| **Payment method** | The method used by the customer (e.g., Credit Card, Apple Pay, Klarna). |
| **Gross** | The original gross amount paid by the customer in their local currency. |
| **Net** | The final amount remaining after fees and costs, displayed in your settlement currency. |
| **Risk score** | An assessment of transaction risk (higher score = higher risk). Click the score to see data points like AVS (Address Verification), IP-to-Shipping match, 3D-Secure usage, and CVC checks. |

## Settlement history

This list displays batches of processed payments. Typically, all transactions from a single calendar day are grouped into one clearing batch. Once cleared, funds move to "Settled" status. For more details on cycles, see [Fund Splitting and Settlement Rules](./operate-dropshipping-fund-splitting.md).

| Field | Description |
| :--- | :--- |
| **Batch** | The unique identification number for the clearing batch. |
| **Date** | The estimated completion date for the batch clearing. |
| **Status** | Either **Clearing** or **Cleared**. |
| **Gross** | Total transaction volume in the batch (USD). |
| **Refund** | Total amount refunded within this batch. |
| **Fee** | Payment processing and transaction fees. |
| **Adjustments** | Any manual or systemic corrections to the clearing total. |
| **Net** | The actual settleable amount after all adjustments and fees are deducted. |

## Payouts

This log tracks transfers initiated from Genstore to your PayPal account. 

| Field | Description |
| :--- | :--- |
| **Creation date** | When the payout was initiated to your PayPal account. |
| **Type** | The category of the payout. |
| **Payout account** | Your linked PayPal email address. |
| **Payout amount** | Total gross amount scheduled for transfer (USD). |
| **Fees** | The transfer fee associated with the payout (USD). |
| **Transfer reference** | Unique reference number for the payout. |
| **Description** | A brief note or reference for the payout. |

::: tip
> * **Processing Time:** Actual arrival of funds depends on PayPal’s processing cycles, which vary by country/region.
> * **Account Health:** Ensure your PayPal account is verified and in good standing to avoid payout delays.
> * **Fee Transparency:** There is a difference between the "Payout amount" and the final amount in your PayPal due to transfer fees; these are detailed in each payout record.

:::

## Disputes

If a customer files a chargeback or dispute with their bank regarding a dropshipping product, it will appear here. You can respond by uploading evidence such as proof of delivery, customer communication logs, or fulfillment records. For more guidance, see [Chargebacks and Inquiries](./operate-genstore-payments-chargebacks-overview.md).