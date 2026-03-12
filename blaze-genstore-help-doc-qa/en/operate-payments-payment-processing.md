# Process credit card payments

When customers pay for an online order using a credit card, the payment must be processed before the funds are deposited into your account. This process is handled by your payment provider and typically involves the following stages:

| **Stage**         | **Description**                                              | **Key considerations**                                       |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Authorization** | The customer’s credit card is validated by the payment provider and issuing bank to confirm its validity and available balance. At this stage, no funds are transferred—only an authorization hold is placed on the card. | No actual payment occurs at this point; it only confirms card validity and balance. |
| **Capture**       | After authorization, the payment must be captured to transfer funds from the customer’s credit card to the merchant’s account. The payment provider sends the transaction details to the acquiring bank, initiating the transfer. | The capture must be completed within the authorization period; otherwise, the payment cannot be processed. |
| **Clearing**      | The acquiring bank reviews the transaction details and requests funds from the credit card network, which then contacts the issuing bank. Fees are deducted at multiple stages before the funds are returned to the merchant’s account. | Funds pass through multiple institutions before reaching the merchant. |
| **Funding**       | The acquiring bank deducts transaction fees and deposits the remaining funds into the merchant’s account. | The deposit time varies by provider, typically taking a few business days. |

## Automatic vs. manual capture

Genstore offers flexible payment capture options, allowing you to choose between **automatic capture** and **manual capture** based on your business needs. Each option has its advantages and can help you better manage orders and cash flow.

### Automatic capture

- **Best for**: Businesses looking to streamline payment processing, especially those handling high order volumes. Automatic capture reduces manual steps and improves efficiency.
- **Advantages**: Ensures payments are captured immediately upon checkout, minimizing the risk of human error.
- **Default setting**: Genstore enables automatic capture by default, meaning payments are processed as soon as a customer completes checkout. No additional steps are required.

### Manual capture

- **Best for**: Businesses needing greater control over transactions, such as those dealing with high fraud risk or requiring manual order verification before capturing payments.
- **Advantages**: Allows merchants to review orders before capturing payment, ensuring accuracy and fraud prevention.
- **Requirements**: If you enable manual capture, each payment must be manually processed within the authorization period. This option is ideal for businesses that need additional review steps.

### Authorization period for payment capture

All credit card payment providers set a time limit (authorization period) within which a payment must be captured after authorization. If payment is not captured within this period, the authorization expires, and the transaction cannot be completed.

- **Genstore Payments**: Offers a **7-day authorization period**. If the payment is not captured within this timeframe, the authorization is automatically canceled, and you will not be able to process the transaction.
  **Exchange rate considerations**: When capturing payments in a foreign currency, the amount is converted based on the exchange rate at the time of capture, not authorization. If exchange rates fluctuate between authorization and capture, the final amount received may differ.
- **Third-party payment providers**: Authorization periods and transaction fees may vary. Contact your payment provider for details.

## Enable automatic payment capture (recommended)

By default, automatic capture is enabled. If you have changed your settings and want to restore automatic capture, follow these steps:

1. Log in to your **Genstore admin account** and go to **Settings -> Payments**.
2. Scroll to **Payment capture method** at the bottom, click **Manage**, and choose **Automatically at checkout** in the dialog.
3. Click **Confirm** to apply the changes.

## Enable manual payment capture

If you prefer to manually capture payments, follow these steps:

1. Log in to your **Genstore admin account** and go to **Settings -> Payments**.
2. Scroll to **Payment capture method** at the bottom, click **Manage**, and choose **Manually capture** in the dialog.
3. Click **Confirm** to save your changes.

:::tip

- In manual capture mode, you must process each payment within the authorization period to avoid failed transactions.
- Before switching to manual capture, carefully evaluate your business needs. To reduce risk and streamline payments, we recommend using automatic capture.

:::
