# Integrate with Klaviyo

In addition to Genstore’s built-in email marketing features, users familiar with the Klaviyo platform can take advantage of the official **Genstore Klaviyo** app. This integration enables native data sync between your Genstore store and Klaviyo, allowing you to continue using your existing workflows and templates while building a more efficient marketing automation system.

## Prerequisites

- You must have an active **Klaviyo account**

## Install the Klaviyo app

You can install the Klaviyo app from the Genstore App Store.

1. Visit the [Genstore App Store](https://apps.genstore.ai) and log in to your Genstore account.
2. If you manage multiple stores, select the store where you want to install the app.
3. Search for `Genstore Klaviyo`.
4. On the app page, click **Install**.
5. You’ll be redirected to the Genstore admin to begin the setup process.
6. [Optional] Click the pin icon next to the app name to add Klaviyo to your sidebar menu for quicker access.

:::tip
When authorizing the Genstore Klaviyo app, you may see a notice from Klaviyo about the app being “unreviewed.”

This app is officially developed by Genstore, and your data is only used to sync information between your Genstore store and Klaviyo. It will not be used for any other purpose. You can safely proceed with authorization.

If you have any questions, feel free to contact Genstore support.
:::

## Connect Klaviyo and your Genstore store

Once authorized, Genstore will sync your store’s product, customer, and order data from the past three months to Klaviyo. This data can then be used to power your email automation flows.

1. Log in to your Genstore admin and locate **Klaviyo** under the **Apps** section.
	- If it’s not pinned to the sidebar, go to **Apps -> Installed**, then click **Klaviyo -> Launch app**.
2. In **Account settings**, click **Connect**.
3. You’ll be redirected to Klaviyo. Sign in with your Klaviyo credentials.
4. Review the permissions requested by Klaviyo, then click **Allow** to complete the authorization.

## Set up customer and data sync

To sync your customers’ subscription status from Genstore to Klaviyo, you’ll first need to select a Klaviyo list. This is required by Klaviyo to manage subscriber data.

:::tip
A **Klaviyo list** is a group of customer contact information (such as email addresses) and represents the audience for your marketing emails.
:::

### Select a customer list

**Steps**:

1. In the **Customer data sync** settings, choose an existing list and click **Save**.
2. To create a new list, click **Create new list** under **Configure List opt-in settings**. You’ll be redirected to Klaviyo to complete the setup.

### Configure opt-in settings (in Klaviyo)

After selecting a list, configure how customer subscriptions are handled:

- **Double opt-in**: Customers will receive a confirmation email and must click to confirm before they are added to the list.
- **Single opt-in**: Customers are added to the list automatically without needing to confirm.

**Steps**:

1. Click **Set up** under the opt-in settings section to go to the list settings page in Klaviyo.
2. In **Account -> API keys**, choose either double opt-in or single opt-in depending on your preference.

## Sync data

After setup is complete, go to the **Data sync** section and click **Sync** to begin transferring your store data to Klaviyo.

**Initial sync scope**:

|Data type|Sync rule|
|---|---|
|Product data|All products in your store will be synced to Klaviyo|
|Customer data|All customers from your store will be synced to Klaviyo|
|Order data|Orders from the past three months will be synced to Klaviyo|

**Ongoing sync rules**:

|Data type|Sync rule|
|---|---|
|Product data|After authorization, any new, updated, or deleted products will automatically sync to Klaviyo|
|Customer data|After authorization, any new, updated, or deleted customers will automatically sync to Klaviyo|
|Order data|After authorization, all new orders will be automatically synced to Klaviyo|

## Use cases

After syncing your data, you can access common email marketing templates from the Genstore admin and use them to build automated flows in Klaviyo.

### Use case examples

- **Email campaigns**: Schedule promotional emails for sales events or new product launches. Use Klaviyo’s built-in templates to personalize content and send emails to segmented audiences.
- **Welcome new customers**: Automatically send a welcome email when a customer registers, helping build a strong first impression and encouraging their first purchase.
- **Behavior-based automation**: Send emails triggered by customer actions like placing an order, completing payment, or canceling an order—such as cart abandonment reminders or order confirmations—to boost repeat purchases.

Click **Create** under each use case to open the corresponding setup in Klaviyo.

### Important notes

When using customer behavior as a trigger for automation, only events that have been synced via Genstore’s API can be used.

In Klaviyo, make sure the **Trigger** and **Metric** you choose have already been synced from Genstore. This ensures your flows will run correctly.

**Learn more**:

- [Understanding flow triggers and filters - Klaviyo Help Center](https://help.klaviyo.com/hc/en-us/articles/115002779051)
- [How to use event data to personalize email and SMS flows](https://help.klaviyo.com/hc/en-us/articles/115002779071)
