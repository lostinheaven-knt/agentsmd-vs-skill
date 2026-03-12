# Chargeback process and dispute handling

A **chargeback** occurs when a buyer (the cardholder) disputes a completed credit card transaction and requests their issuing bank to reverse the payment. If approved, the disputed amount is withdrawn from your account. Chargebacks typically relate to concerns about transaction authenticity, product quality, or the customer’s experience.
## Understand the chargeback process

Here’s how a typical chargeback process works:

1. **Customer initiates a dispute**  
    The cardholder contacts their issuing bank to report a problem with a credit card transaction.
2. **Merchant receives a chargeback notification**  
    The issuing bank submits the chargeback through the credit card network. Genstore Payment is then notified and may request supporting documents from the merchant. You will see the chargeback notice in your Genstore admin and must respond within the specified time.
3. **Funds are temporarily deducted**  
    Genstore Payment immediately deducts the disputed amount and any associated fees from your account balance or pending payouts.
4. **Merchant responds**  
    You can either accept the chargeback or submit evidence to dispute it before the deadline.
5. **Card network reviews the evidence**  
    The card network or issuing bank will review your submission. This process can take up to 75 days.
6. **Final decision is made**
    - If the merchant wins the case, the disputed amount (minus processing fees) will be returned to your account.    
    - If the buyer wins, the funds remain with the buyer.

Chargeback policies may vary depending on the card network (e.g., Visa, Mastercard) and the countries or regions involved in the transaction.

::: tip
In certain cases, such as when the transaction has already been refunded, Genstore Payment will automatically dispute the chargeback on your behalf.
:::

## Review dispute cases in payment dashboard

To view and manage disputes, go to **Finance** -> **Payments** -> **All** in your Genstore admin, then open the **Disputes** tab.

There are three types of dispute notifications:

1. **Notification of chargeback**  
    The buyer questions the transaction—such as claiming they didn’t receive the product, the charge is incorrect, or the transaction is fraudulent. After initial review, the issuing bank sends a chargeback notice to the merchant, requiring action.
2. **Request for information**  
    When the issuing bank needs clarification or additional transaction details, they will send an information request. The merchant is expected to submit supporting documentation.
3. **Notification of fraud**  
    If the cardholder reports suspected fraud (e.g., stolen card, unauthorized use), the issuing bank sends a fraud notice to the merchant and requests relevant transaction records.
### Fields in the dispute table

| **Field**                    | **Description**                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Payment reference number** | Unique ID for the original transaction                                                                                    |
| **Dispute reference number** | Unique ID for the dispute                                                                                                 |
| **Reason code**              | Code provided by the card network explaining the reason for the chargeback                                                |
| **Payment date**             | Date the original transaction was completed                                                                               |
| **Dispute date**             | Date Genstore Payment received the dispute notice                                                                         |
| **Chargeback amount**        | Amount being disputed                                                                                                     |
| **Payment method**           | Payment method used in the original transaction                                                                           |
| **Status**                   | Dispute status:<br/>- `open` (dispute can be challenged)<br/>- `closed` (resolved or cannot be challenged)                |
| **Dispute ends at**          | Last day to submit evidence; “–” means the dispute cannot be challenged                                                   |
| **Latest event**             | Most recent update in the chargeback case                                                                                 |
| **Action column**            | - `Respond`: available for open disputes<br/>- `View`: for closed or resolved disputes<br/>- `Reply`: shown for ROI cases |

## Decide whether to accept or dispute a chargeback

For chargebacks that are eligible for dispute, you can choose between:

- **Accepting the chargeback**  
    Agree to the chargeback result and allow the funds to be refunded to the buyer.
- **Disputing the chargeback**  
    Submit evidence within the specified timeframe (usually 14–40 days) to contest the chargeback. Note: The dispute process can take time and may incur additional fees.

:::tip
We recommend disputing only if you have clear, verifiable evidence and the disputed amount is significant.
:::

If you choose to dispute a chargeback, gather as much relevant documentation as possible. Examples include:

- Order history and prior transactions with the buyer
- Proof of delivery (e.g., shipping or tracking information)
- Communication records (e.g., emails or chat logs with the buyer)