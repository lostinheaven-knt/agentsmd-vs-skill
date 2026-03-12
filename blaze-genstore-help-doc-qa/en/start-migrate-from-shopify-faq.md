# Shopify store migration FAQs

::: faq

## General questions

### Q1. Insufficient API permissions

> A: You need to recheck the Shopify API access permissions and make sure that all Read permissions are checked.

### Q2. Data format incompatibility

> A: Some field formats may need to be adjusted manually, please check the error details for specific information.

### Q3. Network connection exception

> A: It is recommended to check whether your network connection is normal, or try changing the network environment, or try again later.

### Q4. Incomplete data after migration

> A: Please carefully check the error details in the migration log to confirm whether any data migration failed. If you have any questions, please contact Genstore customer support.

### Q5. Can I operate the Shopify store during the migration process?

> A: In order to ensure data consistency, it is recommended to avoid large-scale data modification to the Shopify store during the migration process.

### Q6. What checks need to be done after migration?

> A: After the migration is complete, please be sure to carefully check the store, product, customer, and order data in the Genstore admin to ensure data integrity and accuracy.

## Store module related FAQs

### Q1. Incompatible billing addresses

> A: If the billing address from Shopify falls outside the countries or regions supported by Genstore, it will not be migrated.

### Q2. Media migration failures

> A: Media files will fail to migrate in the following cases:
> 	- [File format is not supported](./settings-media.md) (e.g., unsupported image or video types)
> 	- File size or duration exceeds the allowed limits
> 	- Your current store plan's media storage capacity has been reached

### Q3. Unsupported languages

> A: The following applies to language migration:
> 	- Languages not supported by Genstore will be skipped
> 	- Associated translation content will not be migrated

### Q4. Location limit exceeded

> A: The number of locations supported depends on your Genstore plan. Any locations beyond the limit will not be migrated.

### Q5. Why weren't some locations migrated?

> A: Locations linked through third-party apps are not migrated. These locations are not managed by Shopify's native system, so the migration tool automatically skips them. If needed, you can manually add the relevant locations in the Genstore admin after the migration.

## Customer module related FAQs

### Q1. Duplicate customer records

> A: If a customer's email or phone number matches an existing one in your Genstore store, that customer will not be imported. The system will log the duplication. To merge customer information with the same email, simply choose **Overwrite** in the **Customer** section of the migration settings.

### Q2. Phone number format requirements

> A: Customer phone numbers must follow the international E.164 format (e.g., +12025550123). If the country code is missing, the system will automatically add +1 (US/Canada). Numbers that do not meet the format will not be imported.

### Q3. Customer tax exemption settings

> A: The following rules apply to customer tax exemption settings during migration:
> 	- Only customers marked as `fully tax-exempt` or `non-exempt` will be migrated. Customers under special tax rules will not be migrated automatically.
> 	- These customers will be flagged in the migration log. You can manually update or add their tax settings in Genstore after the migration to ensure data completeness.

### Q4. Customer account passwords

> A: For security reasons, passwords cannot be migrated. After migration, customers can log in using email verification or reset their password.
>::: tip
> 	**Recommended**: After migration, send a password reset email to customers. You can also pair this with a marketing campaign (e.g., offer discount coupons) to encourage customers to set a new password.
>:::

## Product module related FAQs

### Products

#### Q1. Field mapping and validation

> A: During the product migration process, the system performs field mapping and validation based on the following rules:
> 	- Field length must comply with Genstore limits
> 	- Field type and format must meet Genstore requirements
> 	- Any invalid field content may result in failure to migrate that specific field or the entire product. Details will be logged in the migration report

#### Q2. Product pricing and currency

> A: The following rules apply to product pricing and currency during migration:
> 	- Product prices will be migrated based on the **primary market currency** of the Shopify store. Prices in other markets are not supported during migration
> 	- Multi-market pricing is not included in this migration. After the migration is complete, merchants can manually configure pricing for each market in the **Market Settings** section of the Genstore admin

### Product inventory

#### Q1. Physical products

> A: Inventory data will be migrated for each location, including available stock, in-stock quantity, and unavailable inventory

#### Q2. Digital products

> A: Only available stock quantity will be migrated. Inventory locations are not included

### Collections

#### Q1. What type of product collections can be migrated?

> A: Genstore supports migrating Shopify collections using either manual or automated product assignment.
> 	- **Manual collection migration rules**
> 		- Collection titles and descriptions will be migrated
> 		- Products manually assigned to a collection will be matched with products in Genstore
> 		- If a product in the collection does not match any product in Genstore, it will be skipped and not included in the migrated collection
> 	- **Automated collection migration rules**
> 		- Automated collection titles and descriptions will be migrated
> 		- Collection filter conditions will be migrated as well, and Genstore will attempt to match products based on these rules
> 		- If the conditions are incompatible with Genstore’s product structure, the collection will fail to migrate and will be noted in the migration log

### Gift cards

#### Q1. Why migrate gift cards?

> A: Migrating gift cards ensures that customers retain their remaining balance when switching to a new platform. This helps protect customer assets, build trust, and increase the likelihood of repeat purchases.

#### Q2. What migration options are available?

> A: We offer two migration methods:
> 	1. Migrate with the last four digits of the original code
> 		- The new gift card code will be different, but the last four digits of the original code will be preserved.
> 		- Helps customers recognize and trust that this is a continuation of their old gift card.
> 		- Recommended when customer experience and trust are a priority.
> 	2. Generate completely new codes
> 		- A new batch of gift card codes will be generated by the new platform.
> 		- Gift cards are emailed directly to customers using the new codes.
> 		- Suitable for merchants who do not require a visible link between the old and new cards.

#### Q3. Which method should I choose?

> A: You can choose between the following card code generation methods:
> 	- Choose the “last four digits” method if you want customers to recognize the card as a continuation of their previous one.
> 	- Choose the “new codes” method if you're starting fresh or want to automate the distribution using new platform capabilities.

#### Q4. Will customers lose their balance?

>A:  No. The remaining balance from the original gift card will be fully transferred, regardless of the migration method.

## Shipping rate related FAQs

#### Q1. During migration, does the system support product-level or variant-level rules?

> A: The system currently supports migrating shipping rates **by product (SPU)**, but not **by variant (SKU)**. After migration, we recommend reviewing each product’s shipping settings to ensure accuracy.

#### Q2. What happens if some products or shipping origins fail to migrate?

> A: If certain products or shipping origins fail to migrate, their associated shipping rules **will not be transferred**. After migration, you’ll need to **manually add or update** these rules to prevent missing rates or calculation errors.

## Order module related FAQs

#### Q1. Order functionality limitations

> A: Imported orders in Genstore are **view-only**. They appear in the merchant and customer order lists but do not support any fulfillment actions such as payment, shipping, cancellation, return, or exchange.

#### Q2. Currency and amount are preserved

> A: Orders will retain their original currency and amount. Genstore does not perform currency conversion.

#### Q3. Order timestamps are unchanged

> A: Order creation time and time zone are preserved as recorded in Shopify.

#### Q4. Sales market settings remain unchanged

> A: Orders will retain their original market information regardless of whether the corresponding market is enabled in Genstore.

#### Q5. Recommended migration sequence for customer and product data

> A: Order migration does not strictly depend on customer or product data. However, it is recommended to migrate products and customers first.
> 	- If product and customer data already exist in Genstore, imported orders will link to them.
> 	- If product and customer data have not yet been imported, the order will be stored using the original data without linkage to Genstore records.

## Discount module related FAQs

### Q1. Discount limited to "one use per order"

> A: In Shopify, some discounts can be set to apply **only once per order**, even if multiple eligible products are in the cart. **Genstore does not currently support this limitation**. After migration, if an order contains multiple eligible items, the discount may be applied multiple times—resulting in a higher discount amount than expected.
> 	**Recommendations:**
> 	- Temporarily adjust the discount value to accommodate potential multiple applications
> 	- Narrow the scope of applicable products to keep total discount costs under control

### Q2. Discount channel limitations

> A: In Shopify, discounts can be limited to specific sales channels (e.g., Online Store or POS). **Genstore currently supports only online store orders and does not support POS or other offline channels.**
>
> Please note:
> 	- All migrated discounts will automatically apply to all online orders on your Genstore site.
> 	- POS-related settings (such as “POS only” or “exclude online”) cannot be replicated.
> 	- We recommend pausing discounts limited to offline use or adjusting your strategy to fit Genstore’s sale channel features

### Q3. Discount types that cannot be migrated

> A: The following types of discounts are **not supported for migration** in the current version of Genstore. Please pause or reconfigure them before migrating:
> 	- Discounts with **customer segmentation** conditions
> 	- Discounts limited to **POS or other offline channels**
> 	- Discounts with the **“one use per order”** limitation
> 	- A discount campaign **with 0% off**
> 
> These settings are not currently supported in Genstore and may lead to unexpected behavior if migrated. Please review and revise your promotion strategy as needed.

## Store design module related FAQs

### Q1. Why wasn’t my theme migrated?

> A: The migration tool only supports official Shopify themes, including: Dawn, Spotlight, Sense, Trade, Refresh, Craft, Studio, Ride, Taste, Origin, Crave, Publisher, and Colorblock. If you're using a third-party or custom theme, it won't be migrated. After the migration, please manually configure your storefront design and content.

### Q2. How can I migrate store policy pages (e.g. return policy, privacy policy)?

> A: To ensure your Shopify store’s policy pages (such as return policy and privacy policy) are successfully migrated, please enable the corresponding pages in Genstore before starting the migration. Go to **Settings** -> **Policies** in your Genstore admin and activate the relevant pages.

:::
