# Migrate from Amazon

With the Genstore Migration Tool, you can seamlessly migrate product and order data from your Amazon store to Genstore, helping you synchronize your multichannel operations with ease. Follow the steps below to complete the preparation, authorization, and module setup.

## Preparation

- Ensure you have a valid Amazon seller account with access to the target regional marketplace.
	If not, please visit [Amazon Seller Central](https://sellercentral.amazon.com/) to register.
- The country or region of your Amazon store must match an enabled market in your Genstore account.
- If the market for your Amazon store is not yet added to Genstore, please go to the Genstore admin and [add the corresponding market](./global-market-manage-market.md) before proceeding.
- [Ensure the Genstore Migration Tool is installed](./start-migrate-guide#install-the-genstore-migration-tool).

### Supported Amazon marketplaces

**North America**  
Canada (`amazon.ca`), United States (`amazon.com`), Mexico (`amazon.com.mx`), Brazil (`amazon.com.br`)

**Europe, Middle East & Africa**  
Ireland (`amazon.ie`), Spain (`amazon.es`), United Kingdom (`amazon.co.uk`), France (`amazon.fr`), Belgium (`amazon.be`), Netherlands (`amazon.nl`), Germany (`amazon.de`), Italy (`amazon.it`), Sweden (`amazon.se`), Poland (`amazon.pl`), South Africa (`amazon.co.za`), Egypt (`amazon.eg`), Turkey (`amazon.com.tr`), Saudi Arabia (`amazon.sa`), United Arab Emirates (`amazon.ae`), India (`amazon.in`)

**Asia-Pacific & Oceania**  
Singapore (`amazon.sg`), Australia (`amazon.com.au`), Japan (`amazon.co.jp`)

## Authorize your Amazon store

1. Open the Genstore Migration Tool and select **Amazon to Genstore**.
2. Click **Start migration**.
3. In the **Select market** dropdown, choose your target Amazon marketplace and click **Get link**.
4. Log in to Amazon Seller Central and complete the authorization process.
5. Once authorized, the system will display up to 10 connected Amazon stores.

You can view your connected stores under **Authorized marketplaces**, including:

- Store name
- Marketplace domain (e.g., `amazon.com`)
- **Migrate now** button (to open the module setup page)
- Delete icon (to remove the store authorization)

## Select migration modules

The following modules are currently supported:

|Module|Data included|
|---|---|
|**Products**|Name, price, description, images, variants, categories, status|
|**Orders**|Product details, total amount (with original currency), recipient info, order status|

When the order module is selected, the product module is automatically included.

## Product module settings

### Product type mapping (required)

Instructions:

- When the **product module** is selected, the **Amazon migration product type mapping** section will automatically expand.
- Map each Amazon product type to a corresponding Genstore category.

:::tip
- At least one Amazon → Genstore product type mapping must be completed.  
- Products without a valid mapping will not be migrated.
:::

## Custom filters

### Product filters

- **Product status**: You can choose to migrate only **Salable** products. If no filter is applied, all products will be migrated by default.
- **Target location**: Migration is only supported to locations already enabled in Genstore. The default location is applied if not specified.

#### Order filters

- **Date range**: Filter orders based on **creation time**. The maximum supported time span is one year.
- **Order status**: Currently, only **Completed** orders are supported for migration.

::: faq

## FAQs

### Q1. What should I do if I can’t authorize my Amazon store? 
> A: Please confirm your Amazon seller account has access to the target marketplace and ensure authorization permissions are granted.

### Q2. Why weren’t some products migrated?
> A: Please verify that product type mapping was completed. Products without valid mappings are automatically skipped.

### Q3. Can I migrate only selected products?
> A: You can filter by **Product status**. More granular filters (e.g., by SKU or category) are not supported at this time.

:::