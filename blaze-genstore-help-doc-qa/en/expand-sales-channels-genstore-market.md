# Genstore Market app

The Genstore Market app allows you to connect your products to multiple marketplaces and manage all products and orders centrally from your Genstore admin.

- **Unified multi-channel management**: Manage products and orders from multiple marketplaces through a central hub—no more switching between platforms
- **Smart order import logic**: Import orders based on status and specific marketplaces to reduce noise and keep your data clean
- **Real-time sync**: Sync product data and order status across platforms to ensure consistency and avoid errors
- **Built-in time zone and currency handling**: Automatically converts time zones and currency rates for cross-border transactions
- **Bulk operations**: Easily link, import, and sync products in bulk to save time

> Currently supported marketplace: **Amazon**

## Install and authorize Genstore Market

1.  Go to the [Genstore App Store](https://apps.genstore.ai), search for `Genstore Market`. 
   	> If you already in Genstore admin, click **Apps** on the left navigation panel, search for  `Genstore Market`.
2. Click the app card to open the details page.
3. Click **Install** to return to your Genstore admin.
4. Review the requested permissions, then click **Install** in the top-right corner to complete the installation.
5. [Optional] Pin the app to your sidebar for quick access by clicking the pin icon next to its name.
6. On the **Overview** page, click **Connect** next to your target marketplace.
7. Select the marketplace you want to connect and click **Confirm**.
   - If you don’t have a professional Amazon Seller account, click **Create account** to get started.
8. You’ll be redirected to Amazon—follow the steps to complete the authorization.
9.  Once authorized, connected marketplaces will appear under **Overview -> Connected marketplaces**.

## Configure Genstore Market

After authorization, go to the **Settings** page to configure how orders are imported and synced:

- **Order import range**: Choose to import orders from all marketplaces, specific marketplaces, or even specific stores within those marketplaces.
- **Order import strategy**: Choose whether to import only **paid** or **completed** orders, or not import any at all.
- **Auto import**: When enabled, newly created orders will be automatically imported to Genstore.

> Time zone and currency conversion are handled based on your store’s settings. No extra configuration is required.

## Manage channel products (Amazon)

Channel products refer to items synced from Amazon into Genstore via Genstore Market. You can manage them in the **Channel products** tab.

### Link products

If your Genstore store already has the product, you can link it to the matching Amazon product.

**When to use**: You’ve already created the product in Genstore.

**How to link**:
- Open the Genstore Market app and click **Orders**.
- Use the dropdown to select your Amazon store.
- In the **Channel products** tab, find the product row and click **Link product**.
- In the popup, select the matching Genstore product and click **Confirm**.
- To link in bulk, select multiple rows and click **Link products** in the top-right corner.

### Import products

If a product exists only in Amazon, you can import it into your Genstore store and map product types during the process.

**When to use**: You want to bring products from Amazon into Genstore.

**How to import**:
- Open the Genstore Market app and click **Orders**.
- Use the dropdown to select your Amazon store.
- In the **Channel products** tab, find the product row and click **Import product**.
- In the popup, select the Genstore inventory location.
- Map the Amazon product type to a Genstore product type.
- Click **Confirm** to complete the import.
- To import in bulk, select multiple products and click **Import products** in the top-right corner.

## Manage Genstore products

Genstore products refer to items that already exist in your store. You can push product updates to connected marketplaces from the **Genstore products** tab.

### Sync products to marketplace

When you update a product in Genstore (e.g. title, price, inventory), you can sync those changes to Amazon to keep everything aligned.

**When to use**: You’ve made updates in Genstore that need to reflect in Amazon.

**How to sync**:
- Open the Genstore Market app and click **Orders**.
- Use the dropdown to select your Amazon store.
- Go to the **Genstore Products** tab.
- In the product row, click the **Sync to Channel** icon.
- In the popup, click **Confirm**.
- To sync multiple products at once, select them and click **Sync to Channel** in the top-right corner.

## Import orders

If auto import is not enabled, or if you want to bring in historical orders, you can manually import orders from Amazon into Genstore.

**When to use**:
- Auto import is not enabled
- You need to sync older orders into Genstore
- Some orders failed to auto-import and need to be added manually

**How to import orders**:
- Open the Genstore Market app and click **Orders**
- Use the dropdown to select your Amazon store
- In the orders list, find the order row and click **Import order**
- In the popup, click **Confirm**
- To import in bulk, select multiple orders and click **Bulk import** in the top-right corner
