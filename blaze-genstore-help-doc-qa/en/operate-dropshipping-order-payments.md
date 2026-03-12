# Process order payments

This page explains how **Dropshipping order payments** are processed in Genstore — from the customer’s payment to the merchant’s settlement.
It covers buyer payment methods, payment confirmation, order status updates, and merchant payout rules.

## Choose the right payment solution for you

Genstore offers two distinct payment pathways for merchants. You can select the solution that best aligns with your business maturity, legal entity status, and conversion goals:

| Feature | Genstore Payments | Drop Pay |
| :--- | :--- | :--- |
| **Positioning** | Brand Growth / All-in-One Solution | Quick Start / Lightweight Solution |
| **Onboarding (KYC)** | Required; currently supports US or HK entities only | No onboarding/KYC required |
| **Sell Dropshipping Products** | Supported | Supported |
| **Sell Custom/Other Products** | Supported | Not supported |
| **Accelerated Checkout** | Supported (Higher conversion) | Not supported |
| **Fund Splitting & Settlement** | Standard rules apply | Standard rules apply |
| **Payout Method** | Personal or Business Bank Account | PayPal Account |

Both [Drop Pay](./operate-dropshipping-drop-pay.md) and [Genstore Payments](./operate-dropshipping-genstore-payments.md) are fully integrated with the Genstore Dropshipping ecosystem. You should evaluate each option based on your specific operational requirements and scaling strategy.


## Payment overview

When a customer places an order, the system determines the available payment method based on the product type:

1. **Verify product type** – If the cart contains Dropshipping products, only **Genstore Payments** or **Drop Pay** will be available.
2. **Customer completes payment** – The system initiates authorization and charge through the payment gateway.
3. **Confirm payment result** – Upon success, an order is created, and payment status updates automatically.
4. **Sync to admin** – The order appears as **Paid** in the admin and moves into the fulfillment stage.

## Payment status reference

| Payment status | Description                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Pending**    | The order has been created, but payment is not yet completed.                                                            |
| **Processing** | The system is waiting for a response from the payment gateway.                                                           |
| **Paid**       | Payment is successful and confirmed by the system.                                                                       |
| **Failed**     | Payment was declined or failed during processing.                                                                        |
| **Refunded**   | Payment has been refunded to the buyer.                                                                                  |
| **Chargeback** | The cardholder has disputed the transaction, and the corresponding amount has been deducted from the merchant’s balance. |

## Merchant payout process

* After the buyer completes payment, the funds are **temporarily held by Genstore**.
* Once the clearing period ends, the system automatically deducts applicable fees and releases the remaining funds to the merchant’s available balance:
  * Payment processing fee
  * Product cost
  * Dropshipping service fee
* For **Dropshipping orders**:
  * Clearing period: **45 days**
  * Settlement period: **5 days**
* For **regular orders**:
  * Clearing period: **5 days**
  * Settlement period: **0 days (daily auto-settlement)**
* After settlement, funds are transferred to the merchant’s linked bank account. Bank processing times may vary slightly.

> For more details, see [Fund splitting and settlement rules](./operate-dropshipping-fund-splitting.md).

::: faq

## FAQ

### Q1. What if an order doesn’t show as “Paid” after the customer pays?

> A: Payment gateways may experience delays. In most cases, status updates within a few minutes.
>  If it hasn’t updated after 30 minutes, check the payment record or contact support.

### Q2. Does a failed payment automatically cancel the order?

> A: Yes. If the buyer does not complete payment within the time limit, the system automatically cancels the order and releases inventory.

### Q3. Are Dropshipping payments processed differently from regular orders?

> A: Yes. Dropshipping orders must be paid through **Genstore Payments** or **Drop Pay**, and they follow a longer clearing cycle than regular orders.

:::