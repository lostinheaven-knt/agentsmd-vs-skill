# Shoplazza store migration

This guide explains how to use the **Genstore Migration Assistant** to migrate your Shoplazza store data (including store information, products, etc.) to Genstore.
## Start migration

- When your store has a large amount of data, the migration process may take a long time.
- Do not modify API permissions during the migration process, as it may cause the migration to fail.
- Avoid making large-scale data changes to your Shoplazza store during migration to prevent data inconsistencies.
- [Install the Genstore Migration Assistant](./start-migrate-guide#install-the-genstore-migration-tool).
 
### Step 1: Obtain Shoplazza API access permissions

During migration, the system needs to read and synchronize store data through the Shoplazza API. Before starting migration, you must create a developer app in Shoplazza and obtain an API access token. Follow these steps:
1. Log in to your Shoplazza admin, go to **Apps** -> **Manage private Apps**, and enable app development.
2. Click **Create App**
3. In the app actions panel, enter the app details and configure permissions.  
4. Click **Save** to obtain the Admin API access token.

### Step 2: Open the Genstore Migration Assistant

1. Log in to your Genstore admin and navigate to **Apps**.
2. In the **Installed** tab, find **Migration Tool**.
3. Click **Launch app**, select **Shoplazza** as the migration source, and click **Start migration**.

### Step 3: Store authorization

1. Enter the Shoplazza store domain to be migrated. Please enter the full domain ending with `myshoplazza.com` (e.g., `sample.myshoplazza.com`). Custom domains (e.g., `brand.com`) are not supported.
2. Enter your **Admin API access token**.
3. After completing the settings, click **Next**.

### Step 4: Select migration modules

Genstore supports migrating the following modules from Shoplazza to Genstore: 

| Module   | Required |
| -------- | -------- |
| Store    | Optional |
| Products | Optional |

### Step 5: Customize migration settings

You can select specific data for migration based on filter conditions:
- Products: Filter by status (active, draft).

### Step 6: Start migration

1. After confirming all settings, click **Start migration**.
2. The system will start processing the migration, and you can view the migration progress in the application interface. The migration time depends on the amount of data, please be patient.
3. After the migration is complete, you can enter the Genstore admin to further improve the store settings. It is recommended to read [Store Quick Launch Checklist](./start-quick-launch-checklist.md)

## View migration records

After completing the store migration, you can view all migration history records in the Migration Assistant app, including:

- **Migration time**
- **Migration platform** (Shoplazza)
- **Store domain**
- **Migration modules**
- **Migration data results**
- **View error details** (You can export the error data to facilitate review and troubleshooting)

