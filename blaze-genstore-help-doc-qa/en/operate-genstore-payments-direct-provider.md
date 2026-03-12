# Configure direct payment

When you enable the direct checkout payment channel, your customers can enter their credit card information directly on your store's checkout page and complete the payment quickly and easily.

## Stripe payment setup guide

**Prerequisite**: You must have a verified Stripe account.

**Steps to configure**

1. Log in to your Genstore admin account and go to **Settings** -> **Payments**.
2. Click the **Connect** button next to **Stripe**, which will take you to the configuration page. Enter your Stripe account's email address and click the **Activate** button.
3. The page will redirect you to the Stripe login screen. Follow the instructions to log in and authorize.
4. After logging in, the page will redirect you back to the Genstore admin interface, confirming that the setup is complete.

### Common questions about binding Stripe

#### About the “Stripe payout capability not enabled” message

If your Stripe account hasn’t been granted payout capability, you may see this error when linking your Stripe account in Genstore. Payout capability refers to the ability to transfer funds from your Stripe account to your bank account.

To resolve this, please contact your Stripe account manager and provide your Stripe account details to find out the specific reason for the restriction.

#### About the “Stripe charge capability not enabled” message

If your Stripe account hasn’t been granted charge capability, you may encounter this error when linking your Stripe account to Genstore. Charge capability refers to the ability to receive funds from other sources into your Stripe account.

To resolve this, please contact your Stripe account manager and provide your Stripe account details to find out the specific reason for the restriction.

#### About the “Stripe card payment capability not enabled” message

If your Stripe account hasn’t been granted the ability to accept card payments, you may see this error when linking your Stripe account in Genstore. Card payment capability refers to the ability to accept credit or debit card payments from customers purchasing from your store.

We recommend logging in to your Stripe dashboard to check if the relevant payment methods are enabled. You can also contact your Stripe account manager for further details.

## PingPong payment setup guide

**Prerequisite**: You need to have a PingPong account and complete the store website review.

**Steps to configure**

1. Log in to your Genstore admin account and go to **Settings** -> **Payments**.
2. Click the **Add payment method** button under **More payment methods**.
3. In the **Third-party payment provider** tab, select **PingPong Pay** to enter the configuration page.
4. Enter your **AccId**, **ClientId**, and **Salt**, and choose the card images you'd like to display.
5. Click **Save**.

### How to get PingPong Pay account parameters

**Get AccId and Salt**

1. Log in to your PingPong admin account and go to **System** -> **Security Key**.
2. Find your store domain in the list and retrieve your **Acc ID** and the secret key details (Salt detail).

**Get client ID**

1. Log in to your PingPong admin account and go to **Account Center**.
2. In the account details section, find your **Client ID**.

## Consumer experience

Once you’ve completed the configuration, you can visit your store and test the payment process by purchasing a product.

### Checkout page

At checkout, you’ll see that the credit card payment option is now active. Select it, enter your credit card details (three key pieces of information), and click **Pay now** to complete the payment.
