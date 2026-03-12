# Shopyy store migration

This guide explains how to use the **Genstore Migration Assistant** to migrate your Shopyy store data (including store information, products, etc.) to Genstore.

## Start migration

- When your store has a large amount of data, the migration process may take a long time.
- Do not modify API permissions during the migration process, as it may cause the migration to fail.
- Avoid making large-scale data changes to your Shopyy store during migration to prevent data inconsistencies.
- [Install the Genstore Migration Assistant](./start-migrate-guide#install-the-genstore-migration-tool).

### Step 1: Obtain Shopyy API access permissions

During migration, the system needs to read and synchronize store data through the Shopyy API. Before starting migration, you must create a developer app in Shopyy and obtain an API access token. Follow these steps:
1. Log in to your Shopyy admin, go to **Stores** -> **List**.
2. Find the store you wish to migrate and click **Backend**.
3. Navigate to **Settings** -> **System**.
4. Click **Developer** to enter the developer module.
    > **Note:** By default, a developer app is pre-installed with broad permissions. For data security, it is recommended to create a new app.
5. Click **Add a new App**, and enter your **App name**.
6. By default, all **Read_only** permissions are selected automatically. Click **Save**.
7. Back to the app list, click the copy icon next to the Token to obtain your **Admin API access token**.

### Step 2: Open the Genstore Migration Assistant

1. Log in to your Genstore admin and navigate to **Apps**.
2. In the **Installed** tab, find **Migration Tool**.
3. Click **Launch app**, select **Shopyy** as the migration source, and click **Start migration**.

### Step 3: Store authorization

1. Enter the Shopyy store domain to be migrated.
2. Enter your **Admin API access token**.
3. After completing the settings, click **Next**.

### Step 4: Select migration modules

Genstore supports migrating the following modules from Shopyy to Genstore:

|Module|Required|
|---|---|
|Store|Optional|
|Products|Optional|

::: tip
When migrating products, you can choose the **Overwrite update** method: the system will match existing data based on the handle and update the content, instead of creating duplicates.
:::

### Step 5: Customize migration settings

You can select specific data for migration based on filter conditions:
- Products: Filter by status (active, inactive).

### Step 6: Start migration

1. After confirming all settings, click **Start migration**.
2. The system will begin processing your migration. You can monitor the migration progress in the app interface. Migration time depends on the data volume, so please be patient.
3. Once migration is complete, log in to your Genstore admin to finalize your store configuration. We recommend reading the [Store Quick Launch Checklist](./start-quick-launch-checklist.md).

## View migration records

After completing your store migration, you can view your migration history in the Migration Assistant app, including:

- **Migration time**
- **Migration platform** (Shopyy)
- **Store domain**
- **Migration modules**
- **Migration data results**
- **View error details** (You can export error data for later review and troubleshooting)