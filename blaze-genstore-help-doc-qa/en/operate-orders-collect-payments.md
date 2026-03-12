# Collect order payments

By default, the system automatically captures payments made by credit card and certain other payment methods.

If your store is set to [manual capture](operate-payments-payment-processing#manual-capture), you’ll need to take an extra step to receive payment.

## Check your capture settings

If you’re unsure whether your store uses automatic or manual capture, go to **Settings** -> **Payments** to review your payment capture method.

For more details, see [Automatic vs. manual capture](./operate-payments-payment-processing#automatic-vs-manual-capture)

## Manually capture payments

When manual capture is enabled, eligible orders will be marked as **Authorized**. You’ll need to manually capture payment for each order [within the authorization period](./operate-payments-payment-processing#authorization-period-for-payment-capture) to ensure you get paid.

- Capturing a payment updates the payment status from **Authorized** to **Paid**.
- Use the **Payment status: Authorized** filter to quickly find orders that need to be captured. We recommend saving this view for easier access.

::: tip

Credit card authorization periods vary by payment provider.
 For example, **[Genstore Payments](./operate-genstore-payments.md)** allows 7 days to capture an authorized credit card payment.

:::

## How to capture a payment

1. In your Genstore admin, go to **Store** -> **Orders**.
2. Click the order number you want to capture.
3. In the **Summary** section of the order details page, click **Capture payment** to complete the process.

#### Notes

- You can’t capture more than the amount originally authorized. If the customer wants to add more items, you can edit the order and send an invoice for the difference, or ask them to place a new order.
- If you sell in multiple currencies, exchange rates may change between the time of authorization and capture.
- Not all payment providers support manual capture. If you’re unsure, check with your provider’s account manager. **Genstore Payments supports manual capture**, giving you more control over when you collect payment.