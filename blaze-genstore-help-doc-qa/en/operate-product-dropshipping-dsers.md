# DSers Dropshipping

[DSers](https://www.dsers.com/) is the official dropshipping partner of AliExpress, widely used by global dropshipping merchants for managing product imports, bulk ordering, and logistics synchronization.

To help merchants use DSers more efficiently, Genstore provides the official integration app **DSers Dropshipping**. With this app, you can seamlessly connect your Genstore store to the DSers platform, automating the entire workflow from product sourcing to order fulfillment and shipment tracking — enabling faster cross-border operations and business growth.

## Key features

- **Fast product sourcing and publishing**: Quickly import products, bind multiple suppliers, and publish in bulk to your store.
- **Automated order management**: Streamline operations with automation, bulk processing, and real-time data sync.
- **Real-time shipment tracking**: Automatically sync tracking numbers after dispatch.
- **Multi-platform expansion**: Integrate with third-party supplier platforms such as AliExpress, Temu, and more.
## Before you begin

Before installing and using the Genstore DSers app, make sure you’ve completed the following:

- You have a valid DSers account.
- Your DSers account is linked to an AliExpress account.
    - This is required for order fulfillment and logistics synchronization.
    - Reference: [How to link AliExpress](https://help.dsers.com/edit-account-link-dsers-to-aliexpress/)
- You may optionally link other supplier platforms (e.g. Temu, Tmall, TikTok Shop) to expand sourcing channels.
    - Reference: [Connect multiple platforms](https://help.dsers.com/connect-multiple-platforms/)
## Install the app

1. Go to **Apps** in the Genstore admin, or visit the [Genstore App Store](https://apps.genstore.ai/) and search for “DSers Dropshipping”.
2. Click **Install** on the app card to enter the permission confirmation page.
3. Review the data access permissions (e.g. products, orders), then click **Install** to proceed.
4. Once installed, you’ll be redirected to the DSers dashboard to complete authorization and account binding.

## Importing products via DSers

You can import products from AliExpress, Temu, and other supported platforms into your Genstore product catalog. DSers currently supports three methods:

- Import via keyword search
- Import via product link
- Import using the DSers Chrome extension

### Keyword search import

1. In the DSers dashboard, go to **Find Product**.
2. Search by keyword to find relevant products.
3. Select the target products and click **Add to Import List**.
    - If prompted, follow the instructions to install the required browser extension.
4. After syncing, click **Check** to view the products in your **Import List**.
5. Click the **Edit** icon (pencil) on each product to update details like title, images, and description.  
    - Reference: [Edit product details](https://help.dsers.com/edit-products-customize-product-details/)
6. Once confirmed, click **Push to Store** to publish products to your Genstore store.
	- Reference: [Import via Find Suppliers](https://help.dsers.com/import-products-from-find-suppliers/)
### Import via product link (AliExpress / Temu)

For merchants who already have specific product links:

1. Copy the product URL from AliExpress or Temu.
2. In DSers, go to **Import List**.
3. Click the **Import of Search** icon.
4. Paste the link and confirm.
5. The imported product will appear in your list.
6. You can edit it before clicking **Push to Store** to publish it on Genstore.

> Reference: [Import by product link](https://help.dsers.com/import-products-from-aliexpress-temu/)

### Import via DSers Chrome extension

1. Install the DSers Chrome extension in your browser.
2. Visit AliExpress or Temu and use the extension to import products.
3. Complete product editing and publishing in the **Import List** tab.

> Reference: [Import using Chrome extension](https://help.dsers.com/import-products-from-aliexpress-temu/)

## Viewing DSers products in Genstore

- After syncing, you can view the products in **Products** in your Genstore admin.
- **Product status**: Products are published as **Active** by default. You can edit further in the product detail page.  [See Add product for detailed instructions](./operate-product-create.md)
- **Inventory sync**: DSers products are automatically assigned to a DSers-generated **app location** for stock management and fulfillment.

## Syncing Genstore products to DSers

In addition to importing from DSers, you can sync your Genstore products back to DSers:

1. Go to **My Products** in the DSers dashboard.
2. Select your Genstore store at the top.
3. Click **Import Products from DSers**.
4. You can import up to 10 products at a time.
5. Click **Import** to confirm.
6. Synced products will appear under **Unmapped**.
7. Use the **Mapping** icon to bind products to the corresponding AliExpress listings.

> Reference: [Import products to DSers](https://help.dsers.com/import-products/)

## Genstore–DSers Product status mapping

Product status is automatically mapped during sync. Please note the following mapping behavior:

### Genstore → DSers

| Genstore Status | DSers Status |
| --------------- | ------------ |
| Draft           | Draft        |
| Active          | Active       |
| Archived        | Draft        |

> Products marked as Draft or Archived in Genstore will appear as **Draft** in DSers and cannot be fulfilled.

### DSers → Genstore

|DSers Status|Genstore Status|
|---|---|
|Active|Active|
|Draft|Draft|

::: tip
When pushing products from DSers to Genstore, deselect **Also publish to Online Store** to keep the product status as **Draft**. After the push is complete, review and update the product details in your Genstore admin. Once everything looks correct, change the product status to **Active** to start selling.
:::
## Order sync & fulfillment automation

Once products are published, customer orders placed on Genstore will automatically sync to DSers for fulfillment.

### Order sync

1. A customer places an order on your Genstore store.
2. DSers automatically pulls the order data and displays it in the DSers admin.
3. You can manage orders in the **Orders** tab on DSers.

::: tip  
If you’ve connected multiple Genstore stores to DSers, each order will be associated with the corresponding store.  
:::

### Fulfillment methods

You can fulfill orders using either of the following workflows:

#### Method 1: Fulfill from Genstore

1. In Genstore admin, click **Fulfill via DSers** in the order view.
2. Genstore sends the request to DSers.
3. DSers notifies the supplier to ship the product.
4. Tracking number is generated after shipment.
5. DSers automatically syncs tracking details back to Genstore.
6. Genstore updates the order status, and tracking notifications are sent to customers (if enabled).

#### Method 2: Fulfill from DSers

1. In DSers, go to **Open Orders**.
2. Select orders and click **Place Order** to submit them in bulk to the supplier (e.g. AliExpress).
3. Once shipped, tracking details follow the same sync process as above.

::: faq

## FAQ

### Q1: How does Genstore manage inventory for DSers products?

> A: Products imported via DSers are automatically assigned to a dedicated **DSers app location**. This location is used for inventory sync, shipping, and fulfillment. You can view it under **Settings -> Locations** in Genstore.

### Q2: How is tax calculated for DSers products?

>  A: If the DSers app location lacks a detailed address, the system will fall back to:
> 	- Your store's registered address; or
> 	- The default shipping origin (if registration info is missing).

### Q3: How do I set up shipping for DSers products in Genstore?

> A: Go to **Settings -> Shipping and delivery -> Shipping** in Genstore and assign a shipping profile to the DSers app location. Genstore will calculate shipping fees for customers based on this origin.

:::
