# More payment methods

In addition to [Genstore Payments](./operate-genstore-payments.md), Genstore supports several third-party payment providers, giving you the flexibility to choose the payment solution that best fits your business needs. With third-party payment services, your customers can complete payments directly on your online store, without being redirected to external sites, enhancing their shopping experience.

## How to set up

1. Log in to your Genstore admin.
2. Navigate to **Settings** -> **Payments**.
3. Under **More payment methods** section and click **Add payment method**. From the list, select the provider you wish to use:
    - **Third-party payment provider**: These are embedded directly into the checkout page, allowing customers to complete payment without being redirected.
    - **Additional payment methods**: These require customers to be redirected to an external page to complete the payment.
    - **Manual payment**: Add offline options such as manual payments or cash on delivery.
 For detailed instructions, refer to [Configure third-party payments](./operate-payments-third-party-configure.md).

## Supported third-party payment providers

The table below lists the third-party payment providers currently supported by Genstore and the payment methods they offer:

| Payment Provider | Type     | Payment Method             |
| :--------------- | :------- | :------------------------- |
| PayPal           | External | E-wallet                   |
| Stripe           | Direct   | Credit card                |
| Lianlian         | Direct   | Credit card                |
| Asiabill         | Direct   | Credit card                |
| Pingpong         | Direct   | Credit card                |
| Braintree        | Direct   | Credit card                |
| Authorize.net    | Direct   | Credit card                |
| Oceanpayment     | Direct   | Credit card                |
| Airwallex        | External | Credit card                |
| UseePay          | External | Credit card                |
| AsiaBill Local   | External | Local payment and E-wallet |
| Payssion         | External | Local payment and E-wallet |
| PricPay          | External | Local payment and E-wallet |

**Note:**
- When choosing a third-party payment provider, make sure to review their fees and payment processing times.
- If you remove the authorization for a third-party payment method or delete the account hosting parameters, refunds for past orders may no longer be processed. Please exercise caution when removing authorizations or account hosting parameters.
