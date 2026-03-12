# Clone a Genstore store
This guide explains how to use the Genstore Migration Tool to clone data (including store settings, products, and theme customization) from one Genstore store to another.

## Before you begin
Make sure the destination store (the store that will receive the data) has the [Migration Tool](./start-migrate-guide#install-the-genstore-migration-tool) app installed.

## Start cloning your store

### Step 1: Get API access for the source store

To sync data via API during migration, you'll first need to create an app and get an access token for the source store (the store providing the data):

1. Log in to the Genstore admin for your source store and go to **Apps**.
2. Click **Develop apps** in the top right corner, then click **Create an app**.
3. In the pop-up window, enter an **App name**, select an **App developer** (store owner or staff with app development permissions), and click **Create app**.
4. In the **Overview** tab, click **Configure API scopes**, then click **Edit**. Check all permissions that start with `read_`, then click **Save**.
5. Return to the **Overview** tab and click **Install app**.
6. In the confirmation pop-up, click **Install**.
7. The system will redirect to the **API credentials** tab. In the **API access token** section, click **Reveal token once** to get your **Admin API access token**. Note: This access token can only be viewed once, so save it securely.

### Step 2: Switch to the destination Genstore store
Since data will be migrated to the destination store, you need to switch to it for the next steps:
1. In the bottom left corner of the Genstore admin, click the "..." next to your account name and select **Switch store**.
2. Select your destination store from the list of stores.
3. Navigate to **Apps** -> **Installed** and find **Migration Tool**.
4. Open the app, select Genstore as the migration source, and click **Start migration**.

### Step 3: Authorize the source store
1. Enter the domain of your source Genstore store.
2. Enter the access token (your **Admin API access token**).
3. When you're done, click **Next**.

### Step 4: Select modules to clone
Choose which data modules to clone from the source store to the destination store:
| Module | Required | Dependencies |
| --- | --- | --- |
| Store | Required | - |
| Products | Optional | Store |
| Custom Pages | Optional | Store |
| Blog | Optional | Store |
| URL Redirects | Optional | Store |
| Navigation | Optional | Store |
| Theme Template | Optional | Store |

### Step 5: Start cloning
1. Review your settings and start the store cloning process.
2. The system will begin processing the migration. You can track the progress in the app interface. Migration time depends on the amount of data, so please be patient.
3. After cloning is complete, check that all data has been transferred correctly.

## View migration history

After completing the store migration, you can view all migration history records in the Migration Tool app, including:

- **Migration time**
- **Migration platform** (Genstore)
- **Store domain**
- **Migration modules**
- **Migration results**
- **View error details** (with the option to export error data for review and troubleshooting)

## Post-migration checklist

After completing the migration, use this checklist to ensure your store is fully configured and accessible to customers.
- [Post-migration checklist](./start-migrate-checklist.md)