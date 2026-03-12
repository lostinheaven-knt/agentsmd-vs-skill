# Shopline store migration

This guide explains how to use the **Genstore Migration Assistant** to migrate your Shopline store data (including store information, products, etc.) to Genstore.

## Start migration

- When your store has a large amount of data, the migration process may take a long time.
- Do not modify API permissions during the migration process, as it may cause the migration to fail.
- Avoid making large-scale data changes to your Shopline store during migration to prevent data inconsistencies.
- [Install the Genstore Migration Assistant](./start-migrate-guide#install-the-genstore-migration-tool).

### Step 1: Obtain Shopline API access permissions

During migration, the system needs to read and synchronize store data through the Shopline API. Before starting migration, you must create a custom app in Shopline and obtain an API access token. Follow these steps:
1. Log in to your Shopline admin, navigate to **Apps**, and click **Develop App** in the top-right corner to start the app development process.
2. Click **Create an App**, enter an app name, and select **App Developer**. The system will automatically fill in the **Contact Email**. After completing the form, click **Create an App**.
3. In the returned app list, find your newly created app and click **Edit** under the **Actions** column to configure permissions.
4. In the **Permission configuration** tab, click **Configuration** after **Integrate Admin API**, select all permissions starting with `Read` (e.g., `Read products`), then click **Save**.
5. Review your selected permissions in the **Permissions configuration** tab.
6. In the **API certificate** tab, click **Install App** to generate your API access token.
7. Still in the **API Credentials** tab, under **Use your access token to request data from Admin API**, click the eye icon to reveal your access token.
8. For security, the system will prompt you to verify your identity. Complete the verification and save your access token securely.  
    **Note:** The access token can only be viewed once. Make sure to store it safely.

### Step 2: Open the Genstore Migration Assistant

1. Log in to your Genstore admin and navigate to **Apps**.
2. In the **Installed** tab, find **Migration Tool**.
3. Click **Launch app**, select **Shopline** as the migration source, and click **Start migration**.

### Step 3: Store authorization

1. Enter the domain of your Shopline store to be migrated.
	::: tip
	Please enter the full domain ending with `myshopline.com` (e.g., `sample.myshopline.com`). Custom domains (e.g., `brand.com`) are not supported.
	:::
2. Enter your access token.
3. After completing the settings, click **Next**.

### Step 4: Select migration modules

Genstore supports migrating the following modules from Shopline to Genstore:

|Module|Required|
|---|---|
|Store|Optional|
|Products|Optional|

When migrating products, you can choose the **Overwrite update** method: the system will match existing product data and skip duplicate entries instead of creating duplicates.

### Step 5: Customize migration settings

You can select specific data for migration based on filter conditions:

- Products: Filter by status (active, inactive, archived).

### Step 6: Start migration

1. After confirming all settings, click **Start migration**.
2. The system will begin processing your migration. You can monitor the migration progress in the app interface. Migration time depends on the data volume, so please be patient.
3. Once migration is complete, log in to your Genstore admin to finalize your store configuration. We recommend reading the [Store Quick Launch Checklist](./start-quick-launch-checklist.md).

## View migration records

After completing your store migration, you can view your migration history in the Migration Assistant app, including:

- **Migration time**
- **Migration platform** (Shopline)
- **Store domain**
- **Migration modules**
- **Migration data results**
- **View error details** (You can export error data for later review and troubleshooting)