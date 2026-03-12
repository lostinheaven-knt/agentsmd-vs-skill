# Manage product variants (SKUs)

In Genstore, you can create multiple variants (SKUs) for a product to cover different combinations of attributes such as size, color, or material. Using the variant management tools in Genstore admin, you can flexibly **edit**, **bulk update**, **disable**, or **delete** variants to match different stages of your product lifecycle.

## How to access

1. Log in to your Genstore admin.
2. From the left-hand menu, go to **Store** -> **Products**.
3. Click the target product to enter its detail page.
4. Scroll down to the **Variant specification** section to view and manage SKUs.

## Edit individual SKU information

In the **Variant specification** section, you can edit each variant's properties individually. Available fields include:

- Product image
- Price / Compare-at price / Cost
- SKU, barcode
- Inventory settings (quantity, tracking, and continue selling when out of stock)
- HS code, country/region of origin
- Weight
- Metafields

## Customize SKU fields

Genstore now supports personalized configuration of variant fields. You can control which fields are displayed and their display order according to different product sources and management needs:

1. In the **Variant specification** section, click the **Columns** icon in the top-right corner.
2. In the dropdown menu, check/uncheck fields to control visibility.
3. Drag and drop field names to customize their display order.
4. The system will save your preferences per product.

> **Note**: Customization settings are applied at the product level, allowing you to have different configurations for different products.

## Bulk edit SKU information

To apply the same value to multiple variants (e.g. set a unified price), you can use the **bulk edit** feature.

### Steps

1. In the **Variant specification** section, check the SKUs you want to update (multi-select supported).
2. Click **Bulk edit** at the top.
3. In the popup editor, modify the relevant fields.
4. If some fields are missing, click **Columns** in the top-right to add them to the view.
5. Once done, click **Save**.

**Tip**: In addition to the bulk editor, Genstore offers a quick-edit menu. You can efficiently update key fields like price, inventory, images, and barcodes for selected SKUs—without entering each variant detail page individually.

## Bulk edit SKU prices

For products with multiple variants, Genstore supports bulk price editing.

1. Log in to the Genstore admin and go to the **Store** -> **Products** page.
2. Open the target product, select the SKUs you want to edit in the variant details table, and click **Edit price**.
3. Genstore provides two options:
    - **Adjust price**: Set a new price directly for the selected variants.
    - **Adjust from current price**: Increase or decrease by a fixed amount or percentage on the existing price. For example:
        - `-5` → subtract $5 from each item’s current price
        - `+15%` → add 15% to each item’s current price

## Delete or disable SKUs

During the product lifecycle, you may need to stop selling certain variants. Genstore offers two options:

| Action      | When to use                        | Effect                                                      |
| ----------- | ---------------------------------- | ----------------------------------------------------------- |
| **Delete**  | When the variant is no longer sold | Permanently removes the variant and all related data        |
| **Disable** | For temporarily paused sales       | Hides the variant from the storefront, retains all settings |

### Delete SKU

If a variant is permanently discontinued, you can delete it completely. This action is irreversible.

#### Steps

1. Go to your Genstore admin.
2. Navigate to **Store** -> **Products**.
3. Click to open the target product page.
4. Scroll to the **Variant specifications** section.
5. Select the SKUs you want to delete.
6. Click **More actions (···)** -> **Delete SKUs**.
7. Confirm the deletion in the popup by clicking **Confirm**.

#### Notes

- This action cannot be undone. All associated data (inventory, pricing, barcodes, etc.) will be removed
- If a product has only one remaining variant, deletion is not allowed
- Deleted variants will no longer appear in either the admin or storefront

### Disable SKU

If a variant is only temporarily unavailable, we recommend disabling it instead of deleting it.

#### How it works

- Disabled SKUs remain visible in the admin but are hidden from the storefront.
- All configuration data is preserved and can be re-enabled at any time.
- Ideal for stockouts, seasonal pauses, or limited-time availability.

#### Steps

1. Log in to the Genstore merchant admin, and click **Store** -> **Products**.
2. Click to open the target product detail page. Scroll to the **Variant specification** section.
3. You can disable the SKU in one of the following ways:
   - Check a single SKU, then click More actions (···) -> **Disable SKU**.
   - Click the title to enter the specification detail page, then click the **Disable** button in the top-right corner of the page.
4. The disabled SKU will appear in **grayed-out** style and will be hidden on the storefront.
5. To reactivate it, select the SKU, click More actions (···) -> **Enable SKU**.
