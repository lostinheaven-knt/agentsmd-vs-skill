# Configure third-party payments

If you choose not to use [Genstore Payments](./operate-genstore-payments.md), you can still receive payments through third-party payment providers supported by Genstore. You can activate or change your payment provider from the Genstore payment settings page.

During activation, you may be required to submit and verify your bank account information with the payment provider to ensure smooth transaction processing. It’s recommended that you confirm your store's eligibility to receive payments with the provider before submitting any bank information.

## Activate a credit card payment provider

:::tip

**Please note that the following payment methods cannot be activated at the same time.**

| Payment Provider  | Type   | Payment Method                     |
| ----------------- | ------ | ---------------------------------- |
| Genstore Payments | Direct | Credit card, Google Pay, Apple Pay |
| Stripe            | Direct | Credit card                        |
| Lianlian          | Direct | Credit card                        |
| Asiabill          | Direct | Credit card                        |
| Pingpong          | Direct | Credit card                        |
| Braintree         | Direct | Credit card                        |
| Authorize.net     | Direct | Credit card                        |
| Oceanpayment      | Direct | Credit card                        |

:::

**Steps:**

1. Log in to your Genstore admin.
2. Go to **Settings** -> **Payments**. Here, you can directly activate Genstore Payments, Stripe, or PayPal.
3. If you want to use other payment options, go to the **More payment methods** section and click **Add payment method**. From the list, select the provider you wish to use:
	- **Third-party payment provider**: These are embedded directly into the checkout page, allowing buyers to complete payment without being redirected.
	- **Additional payment methods**: These require buyers to be redirected to an external page to complete payment.
	- **Manual payment**: You can add options such as manual payments or cash on delivery.
4. After selecting a payment provider, enter your account credentials in the pop-up window.
5. Click **Save** to complete the process.

## Change your payment provider

:::tip

After changing your payment provider, we recommend saving the changes and then testing your store by placing an order to ensure the new provider is working properly.

:::

**Steps:**

1. Log in to your Genstore admin.
2. Navigate to **Settings** -> **Payments**. Here, you can directly activate Genstore Payments, Stripe, or PayPal.
3. If you want to use other payment options, go to the **More payment methods** section and click **Add payment method**. From the list, select the provider you wish to use:
    - **Third-party payment provider**: These are embedded directly into the checkout page, allowing customers to complete payment without being redirected.
    - **Additional payment methods**: These require customers to be redirected to an external page to complete the payment.
    - **Manual payment**: Add offline options such as manual payments or cash on delivery.
4. After selecting a provider, enter your account credentials in the pop-up window.
5. Click **Save** to complete the setup.

## Get notified of payment configuration changes

Payment configuration is crucial for your store, so we’ll notify you via email or in-system alerts if there are any changes to your payment settings. If a configuration change was not made by you, be sure to restore the original settings and report it.
