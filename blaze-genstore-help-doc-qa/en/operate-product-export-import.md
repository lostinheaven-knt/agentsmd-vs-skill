# Import/Export products

Genstore offers import and export features for products, enabling merchants to manage large amounts of product data efficiently. With export, you can bulk extract product information for backup, analysis, or integration with other systems. The import feature allows you to quickly upload new products or update existing ones, streamlining the process.

## Import products

### Prepare the import file

Follow these steps to download and prepare your CSV file:

1. Log in to your Genstore admin and go to the **Store** -> **Products** page.
2. Click the **Import** button at the top of the product list.
3. In the **Import products** popup, download the import template.

Next, fill out the product details according to the template fields. Be sure to confirm whether your products are single-variant or multi-variant products. **Product variants** refer to different variations of the same product, such as size, color, or model. For example, a T-shirt might have different sizes (S, M, L) and colors (Red, Blue, Green). Each variation corresponds to a unique SKU and inventory.

- **Single-variant products**: Only one version of the product, with all details filled out in a single row.
- **Multi-variant products**: Have multiple options (like size or color). Fill in the basic product details and the URL for the first image in the first row. Then, for each variation, list the options and skip any unnecessary columns (like Title, Body, Vendor, Tags).

**Import template column descriptions**

| Column                                             | Description                                                  |
| -------------------------------------------------- | ------------------------------------------------------------ |
| Handle                                             | The product’s unique URL identifier. For multi-variant products, the handle stays the same. |
| Title                                              | Product title (max 255 characters)                           |
| SubTitle                                           | Product key features (max 255 characters)                        |
| Body (HTML)                                        | Product description (max 255 characters)                     |
| Product Type                                       | Product type: <br/>- normal: physical product <br/>- virtual: digital product |
| Vendor                                             | Manufacturer or vendor of the product                        |
| Product Category                                   | Product category. If not filled, defaults to **Uncategorized**. You can use category IDs like hg-15-1-2 for more precise categorization. |
| Tags                                               | Product tags, separated by commas                            |
| Collections                                        | Product collections, separated by commas                     |
| Images                                             | Image URLs. Each URL needs its own row. To add multiple images, add new rows. |
| Image Position                                     | Image order (e.g., 1 for the main image). Default is 1. The order must be continuous integers without any gaps. If not specified, it defaults to 1. |
| Image Alt Text                                     | Image alt text (max 300 characters)                          |
| Multiple Variants                                  | Whether the product has multiple variants: <br/>- True: multiple variants <br/>- False: single variant |
| Option1 Name                                       | Option name 1 (e.g., color, size)                            |
| Option1 Value                                      | Option value 1 (e.g., black, L)                              |
| Option2 Name                                       | Option name 2 (e.g., color, size)                            |
| Option2 Value                                      | Option value 2 (e.g., black, L)                              |
| Option3 Name                                       | Option name 3 (e.g., color, size)                            |
| Option3 Value                                      | Option value 3 (e.g., black, L)                              |
| Variant SKU                                        | SKU code                                                     |
| Variant Barcode                                    | SKU barcode (e.g., UPN)                                      |
| Variant Weight                                     | Weight (unit can be g, kg, oz, or lb)                        |
| Variant Inventory Tracker                          | Whether inventory is tracked: "TRUE" (track) or "FALSE" (don’t track) |
| Variant Inventory Qty                              | Inventory quantity (required if inventory tracking is enabled, default is 0) |
| Variant Inventory Policy                           | Purchase policy when out of stock: "continue" (allow) or "deny" (don’t allow) |
| Variant Price                                      | SKU price (no currency symbol)                               |
| Variant Compare At Price                           | SKU original price                                           |
| Variant Cost per Item                              | SKU cost price                                               |
| Variant Image                                      | SKU variant image URL                                        |
| Variant Weight Unit                                | Weight unit for SKU variant                                  |
| Status                                             | Product status: <br/>draft: Draft <br/>active: Active <br/>  |
| SEO Title                                          | SEO title for the product                                    |
| SEO Description                                    | SEO description for the product                              |
| Product Metafield Name (product.metafields.custom) | Custom product metadata                                      |

### Import products

1. Log in to your Genstore admin and go to the **Products** page.
2. Click the **Import** button at the top of the product list.
3. Upload your prepared CSV file and click **Upload file**.

## Import products from Shopify

Genstore lets you directly import the CSV file exported from your Shopify store into the Products module. No additional modifications are needed, making it easy to migrate and consolidate customer data in bulk.

### Prepare your import file

1. Log in to your Shopify admin, go to the **Products** menu, select the products you want to export in bulk, and click **Export** to generate a CSV file.
2. If you need to adjust product details, edit the exported CSV file and save it.
3. Log in to your Genstore admin, go to the **Store** -> **Products** page, and click **Import**. Select **Import from Shopify**, then upload your file to start the import process.
4. The import process may take some time. You can leave the page and check the progress later via **Task center** in the bottom-left corner of Genstore admin.

## Export products

The export feature allows merchants to manage and update product data in bulk. The exported data can be used for backups, sales analysis, inventory tracking, and other business decisions. It also makes it easier to sync data across platforms, simplifying large-scale product management and improving overall efficiency.

You can choose which products to export, and the file will be in CSV format. The following export options are available:

- Export current page
- Export all product data
- Export selected product data
- Export based on filter criteria

**Steps:**

1. Log in to your Genstore admin and go to the **Store** -> **Products** page.
2. Click the **Export** button at the top of the product list.
3. In the dialog box, choose the products you want to export.
4. Click **Export**.
