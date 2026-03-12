# Tax settings

When operating a business on Genstore, proper tax configuration is essential for ensuring legal compliance and protecting your profit margins. This guide provides a comprehensive overview of how to manage your tax collection regions and select the tax calculation method that best aligns with your business requirements.

## Tax areas

Tax areas are related to your shipping regions. By default, the system synchronizes countries or regions from your [Shipping and delivery](./operate-fulfillment-shipping-profile-configuration.md) templates.

- **Add region**: If your target country or region is missing from the tax settings list, go to **Settings** -> **Shipping and delivery**, add the region in **Logistics and delivery**, save it, and then return to the tax page to set it up.
- **Stop collecting tax**: To temporarily stop collecting tax for a specific country or region, you can turn off its **Tax collection switch**.
- **Remove region**: You can only remove a region from the tax list if it has been removed from your shipping regions. After removing it from the shipping region, you can click **Actions** -> **Remove** in the tax list to remove the region. For information on how to remove locations from a shipping region, see [Logistics and delivery](./operate-fulfillment-shipping-profile-configuration#configure-shipping-location).
- For countries or regions that are no longer in your shipping regions, the system will display a message: "This country is not included in your logistics and delivery regions." You can choose to keep or remove the region.

## Choose a tax calculation mode

Genstore supports flexible tax configuration services for different countries or regions. You can switch between the following three modes based on the complexity of the tax system in your target market:
- [Genstore Tax](./taxes-setting-genstore-tax.md)
- [Manual tax](./taxes-setting-manual-tax.md)
- [Avalara Tax](./taxes-setting-avalara-tax.md)

::: tip
When switching between different tax services, your historical tax data will not be lost.
:::

## Additional settings

### Configure tax display settings
After completing your tax configuration, you also need to set whether your product prices include tax:
1. Navigate to **Genstore** -> **Settings** -> **Taxes and duties**.
2. Choose whether product prices should be **tax-inclusive** or **tax-exclusive**.

## How tax is calculated

- **Based on address**: Genstore calculates taxes using the **customer’s shipping address** for both manual and automated tax settings. Both self-pickup products and virtual products, the **billing address** is used. Currently, merchants cannot modify this setting.
- **Based on product price**: Genstore calculates taxes based on the discounted product price (`Discounted product price = Product price - Product discount - Order discount`). The order tax is the sum of all product taxes. **Note:** The portion paid with a gift card is not included in the deducted discount amount.

### Tax rounding method

Genstore currently applies a **product-level tax rounding principle**, meaning that taxes are calculated individually for each product. **The calculated tax amount is rounded to two decimal places**, and the total tax amount is determined by summing the rounded values of all products.

**Note:** The decimal places for rounding are retrieved from **Settings -> Markets -> Preferences -> Price rounding** by default. If you need to adjust this setting, please update it in this section.

### Tax calculation rules for different order types

When processing orders, the platform applies different tax calculation logic based on the order type, as follows:

#### Orders involving virtual products

- The **billing address** is used as the primary basis for tax calculation.

#### Orders with in-store pickup as the delivery method

- The **billing address** is used as the primary basis for tax calculation.
- If the billing address is empty, the **pickup address** will be used as the fallback tax reference.

#### Orders with merchant delivery as the delivery method

- By default, the combination of each product’s **shipping address (warehouse address)** and the **shipping destination address (customer’s delivery address)** is used for tax calculation.
- If the product is shipped using a third-party fulfillment app and the shipping address synced to Genstore is empty, the **store’s Billing Address** will be used as the default tax reference.

#### Dropshipping orders
- Genstore Dropshipping (Marketplace sourced products): Tax calculation is based on the product warehouse location (provided by the system) as the origin shipping address.
- Genstore Print on Demand (POD): Since the supplier's shipping address cannot be retrieved, the Store Billing Address is used as the origin shipping address for tax calculation.
- Other Dropshipping Apps (e.g., DSers): Similarly, because the supplier's shipping address is unavailable, the Store Billing Address is used as the origin shipping address for tax calculation.

