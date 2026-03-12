# Track inventory

Genstore automatically tracks changes to product inventory to help you monitor stock levels and reduce the risk of overselling or inventory discrepancies.

When a product is sold, restocked, transferred, or manually adjusted, the system updates the inventory quantity and records the corresponding inventory change for review and management.

## How inventory tracking works

When inventory tracking is active:

* Inventory quantities are automatically updated based on orders and inventory-related actions
* Each inventory change generates a corresponding inventory record
* Inventory quantities can be managed separately by product variant and fulfillment location

All inventory changes, including sales, restocking, and inventory transfers, are recorded.
For details on how to view inventory records, see
**[View inventory adjustment history](./operate-inventory-view-history.md)**.

## Set inventory quantities

Inventory tracking is enabled automatically. To start tracking inventory changes, simply set inventory quantities for your products.

### Set inventory for single-variant products

1. Log in to the **Genstore admin**, then go to **Store** -> **Products**.
2. In the product list, click the target product, or click **Edit** in the **Actions** column.
3. On the product details page, locate the **Inventory** section and enter a value under **Available**.
4. If you ship from multiple locations, click **Manage location** to add locations and set inventory quantities for each location.
5. Click **Save** to apply your changes.

### Set inventory for multi-variant products

1. Log in to the **Genstore admin**, then go to **Store** -> **Products**.
2. In the product list, click the target product, or click **Edit** in the **Actions** column.
3. In the **Variant details** section:
   * Locate the target variant and enter inventory quantities under **Available**.
   * To update multiple variants at once, select the variants, click **Bulk edit**, and enter values in the **Available** column.
4. If you ship from multiple locations, click **Manage location** and use the location selector to set inventory for each location.
5. Click **Save** to apply your changes.

If you don’t need to manage inventory for a product, you can uncheck **Track inventory** in the **Inventory** settings for the product or its variants.

## Selling when inventory reaches zero

When inventory reaches zero, you can control how the product behaves in your store:

* Allow customers to continue purchasing when inventory is zero
* Prevent purchases when inventory is zero

You can adjust this setting by selecting **Continue selling when out of stock** on the product details page.
For multi-variant products, this option is available in the variant details section or via **Bulk edit**.

