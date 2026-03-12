# Integrate with Mailchimp

**Mailchimp** is a powerful email (EDM) and SMS marketing platform that integrates with your Genstore store for real-time data synchronization. With Mailchimp, you can build personalized and automated marketing campaigns—such as welcome emails, cart recovery reminders, and more—based on your store’s product, customer, and order data.

## Prerequisites

- You must have an active **Mailchimp account**

## Install the Mailchimp app

You can install the Mailchimp app from the Genstore App Store.

1. Visit the [Genstore App Store](https://apps.genstore.ai) and log in to your Genstore account.
2. If you manage multiple stores, select the target store.
3. Search for `Genstore Mailchimp`.
4. On the app page, click **Install**.
5. You’ll be redirected to the Genstore admin to begin the setup process.
6. [Optional] Click the pin icon next to the app name to add Mailchimp to your sidebar menu for easier access.

## Connect Mailchimp and your Genstore store

Once authorized, Genstore will sync your store’s product, customer, and order data from the past three months to Mailchimp. This enables you to build automated workflows within Mailchimp using accurate and up-to-date store data.

1. Log in to your Genstore admin and locate **Mailchimp** under the **Apps** section.
    - If it’s not pinned, go to **Apps -> Installed**, then click **Mailchimp -> Launch app**.
2. In the **Account settings**, click **Connect**.
3. You’ll be redirected to Mailchimp. Log in with your Mailchimp credentials.
4. Review the requested permissions and click **Allow** to authorize the connection.

## Set up customer and data sync

To sync your customer subscription data from Genstore to Mailchimp, you’ll need to select a Mailchimp **Audience List** in advance. Mailchimp requires this list to manage subscribers and drive marketing actions.

A **Mailchimp Audience List** is the primary database of your customer contacts. All email campaigns, automations, and analytics in Mailchimp are based on this list.

### Select a customer Audience List

**Steps**:

1. In the Mailchimp customer sync settings, select an existing list and click **Save**.
2. To create a new list, click **Create new list** to be redirected to the Mailchimp dashboard.

## Sync data

Once your list is configured, go to the **Data sync** section and click **Sync** to begin syncing your store data with Mailchimp.

**Initial sync scope**:

|Data type|Sync rule|
|---|---|
|Product data|All products in your Genstore store will be synced to Mailchimp|
|Customer data|All customers from your Genstore store will be synced to Mailchimp|
|Order data|Orders from the past three months will be synced to Mailchimp|

**Ongoing sync rules**:

|Data type|Sync rule|
|---|---|
|Product data|New, updated, or deleted products will automatically sync to Mailchimp|
|Customer data|New, updated, or deleted customers will automatically sync to Mailchimp|
|Order data|All new orders will be automatically synced to Mailchimp|

## Use cases

After syncing your data, you can access Mailchimp’s ready-made email marketing templates directly from the Genstore admin and build your marketing automations inside Mailchimp.

### Use case examples

- **Email campaigns**: Send scheduled promotional emails for events or new product launches. Use Mailchimp’s prebuilt templates to personalize content and target segmented audiences.
- **Welcome new customers**: Automatically send a welcome email when a customer registers. This helps establish a strong first impression and encourages the first purchase.
- **Order notifications**: Trigger emails when customers place or cancel orders. Automate messages like order confirmations, shipping updates, and cancellation notices using Mailchimp flows.

Click **Create** under each use case to go to Mailchimp and configure the automation.