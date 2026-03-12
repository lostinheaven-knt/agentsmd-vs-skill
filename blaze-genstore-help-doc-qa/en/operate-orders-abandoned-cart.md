# Abandoned checkouts

An abandoned checkout is defined as a session where a customer enters their email address but fails to complete the order within 10 minutes.

## **Abandoned checkout rules**

1. The user must have entered an **email address** on the **checkout page** for the order to be marked as abandoned.
2. Abandoned checkout data is kept for 3 months. If not recovered within that time frame, or if no attempt is made to recover it, the system will automatically delete the data.
3. Orders with a total of $0.00 on the checkout page are not considered abandoned checkouts.
4. When using Genstore Payments
   - When a payment fails due to a `declined card` or `insufficient funds`, the system generates an order but does not flag it as an abandoned checkout. For all other payment failures, the system records an abandoned checkout instead of creating a formal order.
5. When using a third-party payment gateway
   - When a payment fails due to a `declined card` or `insufficient funds`, the system generates an order but does not flag it as an abandoned checkout. For all other payment failures, the system records an abandoned checkout instead of creating a formal order.

## View abandoned checkouts

You can view records of abandoned checkouts to review the details of each instance. Here’s how:

1. Log in to Genstore admin and go to **Store** -> **Orders** -> **Abandoned checkouts**.
2. In the **Abandoned checkout list** section, select an order you want to review, then click on the **Order ID** to access the **Abandoned checkout details**.

## Automatically send abandoned checkout link

You can automatically gather relevant transaction details after a customer abandons checkout and send them a link via email to complete their purchase. Each message will include a link to the abandoned checkout, allowing customers to easily finalize their checkout. To set it up:

1. Log in to Genstore admin and go to **Marketing** -> **Marketing automations**.
2. Click **Create marketing automations** in the top right corner.
3. Select the **Abandoned checkout** automation template.
4. Click **Create task**.

Once the automation is active, you can edit and manage it, including turning it on or off.

## Manually share abandoned checkout link

You can also manually copy the abandoned checkout link and send it to the customer for payment. Here's how:

1. Log in to Genstore admin and go to **Store** -> **Orders** -> **Abandoned checkouts**.
2. Click the **Order ID** to access the abandoned checkout details page and click **Copy checkout URL**.
3. In the **Copy checkout URL** pop-up window, click the **Copy link** button.
4. Send the copied link to the customer, so they can complete their checkout. Customers can edit their checkout information and complete the payment through the checkout link.

## **View automation process and recall status**

You can review the marketing automation process and its recall status for each abandoned checkout. Here’s how:

1. Log in to Genstore admin and go to **Store** -> **Orders** -> **Abandoned checkouts**.
2. Open the **Abandoned checkout details** and find the **Marketing automation** module to see the automation process linked to the order.
3. In the **Recall notification status** section, check if the email has been successfully sent.
4. If you have not enabled the marketing automation service, or if it is enabled but no automation flow has been created, the system will prompt `Automation flow is not enabled. Please go to enable it`. Please go to enable the service and set up the [abandoned checkout recovery flow for marketing automation](./expand-marketing-automated-email-abandoned-checkout.md).

## Recover abandoned checkout

When a customer completes their checkout via the recovery link in the email or manually finishes the process, the Abandoned checkout is considered recovered.
