# Integrate with Omnisend

**Omnisend** is a powerful email (EDM) and SMS marketing platform that integrates with your Genstore store to enable real-time data sync. With Omnisend, you can build highly effective and personalized marketing workflows based on your store’s product, customer, and order data—such as welcome emails, cart recovery messages, and more.

## Prerequisites

- You must have an active **Omnisend account**
- The Omnisend store you authorize must be connected to your Genstore site URL

### How to link your Omnisend store with your Genstore store

1. Log in to your Omnisend account and switch to the store you want to connect.
2. Go to **Store settings** and select **Store information**.
3. Enter your Genstore store URL and click **Update information**.

## Install the Omnisend app

You can install the Omnisend app from the Genstore App Store.

1. Visit the [Genstore App Store](https://apps.genstore.ai) and log in to your Genstore account.
2. If you manage multiple stores, select the target store.
3. Search for `Genstore Omnisend`.
4. On the app page, click **Install**.
5. You’ll be redirected to the Genstore admin to begin the setup process.
6. [Optional] Click the pin icon next to the app name to add Omnisend to your sidebar menu for quicker access.

## Connect Omnisend and your Genstore store

Once authorized, Genstore will sync your store’s product, customer, and order data from the past three months to Omnisend. This enables you to configure and trigger automated marketing workflows in Omnisend.

1. Log in to your Genstore admin and locate **Omnisend** under the **Apps** section.
    - If it’s not pinned, go to **Apps -> Installed**, then click **Omnisend -> Launch app**.
2. In the **Account settings**, click **Connect**.
3. Confirm that the Omnisend store you're authorizing is linked to your Genstore URL.
4. You’ll be redirected to Omnisend to log in with your credentials.
5. Select the Omnisend store you want to connect.
6. Review the permissions Omnisend is requesting and click **Authorize access** to complete the process.

## Sync data

After completing the authorization, go to the **Data sync** section in the app and click **Sync** to transfer your store data to Omnisend.

**Initial sync scope**:

|Data type|Sync rule|
|---|---|
|Product data|All products in your Genstore store will be synced to Omnisend|
|Customer data|All customers from your Genstore store will be synced to Omnisend|
|Order data|Orders from the past three months will be synced to Omnisend|

**Ongoing sync rules**:

|Data type|Sync rule|
|---|---|
|Product data|New, updated, or deleted products will automatically sync to Omnisend|
|Customer data|New, updated, or deleted customers will automatically sync to Omnisend|
|Order data|All new orders will be automatically synced to Omnisend|

**Order status definitions**：

| Order status | Description |
| --- | --- |
| Paid for order | The order has been paid; includes orders with full or partial payment. |
| Order fulfilled | The order has entered the fulfillment process; includes fully or partially shipped orders. |
| Order canceled | The order has been canceled. |
| Placed order | Orders successfully created but not yet paid, shipped, or canceled. |

## Use cases

After syncing your data, you can access Omnisend’s prebuilt automation templates directly from the Genstore admin and use them to create powerful workflows inside Omnisend.

### Use case examples

- **Email campaigns**: Schedule promotional emails for discounts, seasonal sales, or product launches. Use Omnisend’s drag-and-drop editor and templates to personalize content.
- **Welcome new customers**: Automatically send a welcome email after account registration to establish a strong first impression and encourage the first purchase.
- **Behavior-based automation**: Trigger emails based on customer behaviors like placing an order, completing a payment, or canceling—such as thank-you messages, back-in-stock alerts, or cart recovery reminders.

Click **Create** under each use case to open the corresponding setup in Omnisend.

### Important notes

Only events synced via Genstore’s API can be used as **triggers** in Omnisend’s automation builder.

Before configuring your workflow, make sure the trigger you select is available in Omnisend’s system and has been successfully synced from your Genstore store.

**Learn more**:

- [Learn how to set up and customize your automation workflows, use audience filters and tags in automation – Omnisend Help Center](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings)