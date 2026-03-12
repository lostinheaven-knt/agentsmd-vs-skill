# Import/Export inventory

Genstore makes it easy to manage inventory in bulk using **CSV files**. Merchants can import or export inventory data quickly to update stock levels, back up data, or analyze trends.

- **Import inventory**: Upload a local CSV file containing product details (like stock quantity, SKU, price, etc.) to update your inventory in bulk.
- **Export inventory**: Export inventory information (such as stock levels, variants, and product IDs) from the system into a CSV file for backup, analysis, or modification.

## CSV file fields

The inventory CSV file uniquely identifies products and their **variants** (e.g., color, size) across different locations. The format is similar to other CSV files but with specialized fields.

| Field Name        | Required | Description                                                  |
| ----------------- | -------- | ------------------------------------------------------------ |
| **Handle**        | ✓        | A unique product identifier. **No spaces allowed**, only letters, hyphens, and numbers (used in product URLs). |
| **Title**         | ✗        | Product title (optional, can be left blank).                 |
| **Option1 Name**  | ✓        | The name of the first variant (e.g., "Color"). If no variants, enter "Title". |
| **Option1 Value** | ✓        | The value of the first variant (e.g., "Black"). If no variants, enter "Default Title". |
| **Option2 Name**  | ✗        | The name of the second variant (optional, can be left blank). |
| **Option2 Value** | ✗        | The value of the second variant (optional, can be left blank). |
| **Option3 Name**  | ✗        | The name of the third variant (optional, can be left blank). |
| **Option3 Value** | ✗        | The value of the third variant (optional, can be left blank). |
| **SKU**           | ✗        | Product SKU (optional, can be left blank; SKUs can be duplicated). |
| **Location**      | ✓        | The location of the product; inventory for each location must be listed separately. |

> **Multi-variant products** should use a combination of **Handle, Option1 Value, Option2 Value, Option3 Value** to uniquely identify each variant.
>
> **CSV file format requirements**: Files must be in **.csv** format and comply with the field requirements above.

## Import inventory

The import feature allows merchants to update inventory information in bulk by uploading a CSV file, making inventory management more efficient.

**How to import inventory**

1. Log into the Genstore admin, go to **Store** -> **Products** -> **Inventory**.
2. Click **Import**.
3. In the pop-up window, click **Upload file** and select the inventory CSV file.
4. Click **Upload file** to complete the import.

## Export inventory

Exporting inventory lets you save current page data, all inventory data, or filtered data for backup, analysis, or future re-import. Common scenarios include:

- Creating an inventory template that includes unique product identifiers and stock levels for the current location.
- Exporting inventory data for use in other systems or processes.

**How to export inventory**

1. Log into the Genstore admin, go to **Store** -> **Products** -> **Inventory**.
2. Click **Export**.
3. In the pop-up window, select the range of data you want to export, then click **Export**.
