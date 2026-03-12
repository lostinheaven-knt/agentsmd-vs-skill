# Configure offsite payment

When you use offsite checkout payment channels, customers are redirected to a third-party checkout page to complete their payment. After payment, they will be redirected back to your store.

## Airwallex credit card payment setup guide

**Prerequisites**

You need to contact your Airwallex account manager to complete the payment setup and enable developer permissions.

:::tip

Airwallex credit card payments are currently only supported on third-party checkout pages.

:::

**Steps to set up**

1. Log in to your Genstore admin account and go to **Settings** -> **Payments**.
2. Click the **Add payment method** button under **More payment methods**.
3. In the **Additional payment methods** tab, select **Airwallex Credit card** to enter the configuration page.
4. In the configuration page, fill in your **ClientId**, **API KEY**, and **SecretKey**, and choose the card images you want to display.
5. Click **Save**.

### How to get Airwallex account parameters

**Get ClientId and API KEY**

1. Log in to your Airwallex admin account and go to **Account** -> **Developer**.
2. Under the **API Keys** menu, find the **Admin API Key** to get your **CLIENT ID** and **API KEY**.

Get SECRET KEY

1. Log in to your Airwallex admin account and go to **Account** -> **Developer**.
2. Under the **Webhooks** menu, click **Add Webhook**.
3. In the **Summary** form, enter the **Notification URL** and select all **Events**, then click **Submit**.
   	:::tip
	You can contact Genstore Support to get the **Notification URL**.
	:::
4. Return to the **Webhooks** page to get the corresponding **SECRET KEY**.

### Consumer experience

After configuring everything, you can visit your store and test the payment process by purchasing a product.

#### Checkout page

On the checkout page, you will see the **Airwallex credit card** payment option. Select it and click the **Pay now** button. The page will redirect you to the Airwallex checkout page.

#### Third-party payment page

On the Airwallex payment page, choose your payment method, fill in the required details, and click **Submit**. After successful payment, you will be redirected back to the store’s checkout success page.

## PayPal payment setup guide

**Prerequisites**: You must have a verified PayPal business account.

**Steps to set up**

1. Log in to your Genstore admin account and go to **Settings** -> **Payments**.
2. Click the **Connect** button for PayPal.
3. Enter your PayPal account email address and click **Connect**.
4. You will be redirected to the PayPal login page. Follow the instructions to log in and authorize.
5. After successful login, the page will redirect back to the Genstore admin interface, confirming that authorization is complete.

### Common questions about binding PayPal

#### About the “PayPal email not confirmed” message

If the email address you used when registering your PayPal account hasn’t been officially verified, you may see this error when linking your PayPal account to Genstore.

We recommend you to log in to your PayPal account and check the verification status of email. Also, check your email inbox to see if you’ve received a verification email from PayPal.

#### About the “PayPal account restricted” message

If your PayPal account has been restricted , you may not be able to successfully link it to Genstore. In this case, we recommend you to contact your PayPal account manager and provide your PayPal account details to find out the specific reason.

### Consumer experience

After the setup is complete, you can enter your store and test the payment process by purchasing any product.

#### Product details page

On the product details page, you’ll see the **PayPal Express Checkout** button. Click the PayPal button to open the PayPal payment form and complete the payment.

#### Cart drawer and cart page

On the cart drawer or cart page, you will also see the **PayPal Express Checkout** button. Click it to open the PayPal payment form and complete the payment.

#### Checkout page

On the checkout page, you’ll notice the **PayPal Express Checkout** option activated at the top of the page or in the payment method section. Select it and click the **Pay now** button. The PayPal checkout page will open in the current window. After a successful payment, the customer will be redirected back to the store’s checkout success page.

## PricPay payment setup guide

Genstore supports integration with PricPay as an external payment method. Customers can select PricPay at checkout and complete their payment via the PricPay gateway.

::: tip

- **Customer phone numbers are required.** PricPay requires all buyers to provide a phone number at checkout. Make sure phone number collection is enabled in your store settings [**Settings** -> **Checkout**](./settings-checkout#phone-number) (set to **Visible, required**) before activating PricPay, otherwise payments may fail.
- Refunds for PricPay must be initiated from your PricPay merchant dashboard. Genstore does not support managing refunds for this payment method.  
- To ensure refund status is synced properly with your store, you’ll need to set up a refund callback URL.

:::

**Steps to configure PricPay**

1. Log in to your Genstore admin account and go to **Settings** -> **Payments**.
2. In the **More payment methods** section, click **Add payment method**.
3. Under the **Additional payment methods** tab, select **PricPay** to open the configuration page. Enter your **Merchant Number** and **APP Key**, and choose the card group icons to display.
4. Click **Save** to complete the setup. **Note:** Before saving, ensure phone number collection is enabled (**Visible, required**) in **Settings -> [Checkout](./settings-checkout.md)**. PricPay payments may fail without it.
5. Log in to your PricPay merchant dashboard and go to **Basic Information**.
6. In the **Callback URL** field, enter the following link:  
    `https://pay.genstore.ai/webhook/pricpay/refund`

