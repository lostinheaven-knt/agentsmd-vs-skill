# Add product

In the Genstore admin, you can create different types of products. Each product can be configured in detail to optimize its display and sales.

- **Physical products**: Tangible, visible items that can be shipped, such as clothing and electronics.
- **Digital products**: Digital products sold online, such as music, movies, or e-books, which customers can download immediately.
- **Virtual products**: Products that do not require shipping, such as online services or subscriptions. _In Genstore, these are created as digital products without a downloadable file._

## Select product type

1. Log in to the Genstore admin and go to the **Store** -> **Products** page.
2. Click **Add product** in the top right corner, then select **Physical products** or **Digital products** based on your product type.
## Product title and key features

- **Product title**: The title appears as the product’s name in the store. Keep it concise, include key features, and avoid special characters.
- **Key features**: Provides more details or key selling points to help customers better understand the product.
## Images/Videos

Upload product images and videos to give customers a clear visual representation of the product’s appearance and features.

**Note:** Genstore now supports saving products without images, making it easier to create drafts quickly and speed up the product entry process.

- Upload multiple images
- Drag and drop to rearrange image order
- The first image will be used as the main image

## Product description

The **Description** section is used to **provide a comprehensive introduction to the product**, supporting rich text editing with images, links, and tables. It should clearly explain key details such as the product’s purpose, features, materials, and dimensions.

**Display location**:

- Desktop: Shown to the right of the product image
- Mobile: Shown above the product highlights section
## Product category

Product categories are used to group and organize products—for example, “Clothing,” “Furniture,” or “Electronics.” Each category can be assigned a set of **category attributes** to help manage shared information across similar products.

- Each product can be assigned to only one category
- If no category is set, the product will be marked as “Uncategorized”
- Multi-level category structures are supported, e.g.:
   **Apparel & Accessories > Clothing > Tops > Shirts**

## Category attributes

After selecting a category for a product, some categories may offer additional attribute settings. Category attributes are key characteristics associated with a specific product category. For example, when you select the “Shirts” category, the system will predefine attributes such as:

- **Color** – You can define attribute values like white, blue, etc.
- **Pattern** – You can set values such as stripes, print, solid, plaid, etc.

In addition to these, the system allows you to flexibly add more attributes based on the actual product features. For example, under the “Shirts” category, you can add attributes like age group, button features, and more.

You may keep or remove these attributes as needed.

::: tip

Product categories and attributes not only support classification, search, and display, but can also be linked to product variants, allowing you to quickly create multiple variants and purchase options. See the [Variants and attributes](#variants-and-attributes) section for more details.

:::

## Product highlights

The **Highlights** section is used to **emphasize key selling points and appeal**, helping users quickly understand what makes the product special. Use concise language or a bulleted list to grab attention and drive conversions. You can click the **pencil icon** next to **Highlights** to edit.

## Product variants

Product variants describe different versions of a product based on attributes like size, color, capacity, or fabric.

Genstore offers two variant options:

- **Single variant**: A product with a fixed attribute combination and no variations.
- **Multiple variants**: A product with multiple attributes (e.g., size, color, fabric, capacity) that customers can choose from.

### Add variants

You can set up multiple variants, supporting up to 100 variants per product, with a maximum of 5 variant attributes.

**Steps:**

1. On the **Products** page, locate the **Variants** section.
2. Click the **+ Add options like size or color** button.
   - If the product has an assigned category with configured attributes, you can select the desired variant option directly from the dropdown list. If attribute values have been set, the system will automatically populate the corresponding variant options—you can adjust them as needed.
   - If the product is uncategorized, you can manually enter the variant option name and values (e.g., variant name: "Size"; values: "Small", "Medium", "Large").
      **Note:** Variant values under the same variant must be unique. Values can be repeated across different variants.

For example, for a men’s shirt, you can set up:

- **Size**: S, M, L, XL
- **Color**: White, Blue, Black
- **Fabric**: Cotton, Blended

### Configure variant details

After adding variants, you can set details such as images, prices, compare-at prices, HS codes, country of origin, barcodes, and stock levels.

**Steps:**

1. Click on a variant to edit details like images, pricing, HS code, country of origin, and inventory.
2. Use the bulk editing option to apply changes to multiple variants at once.

## Variants and attributes

To improve efficiency and consistency, Genstore supports automatic linking between product variants and category attributes.

### Link variants and attributes

When a product has a selected category and that category includes configured attributes:

- The system will automatically link variants to the attributes and sync attribute values as option values.
- You can manually add or remove variant values. These changes will also sync with the attribute values.
- Each variant or attribute can only be linked to one corresponding attribute or variant.

::: tip

In addition to commonly preset options like color, pattern, and size, you can also define custom variant options based on the product’s actual features. For example:

- For shirts, you can add custom variant options like “Style,” “Button type,” or “Sleeve length” on top of the default attributes.
- Custom variants will not affect the original category settings. They can also be used to create product SKUs and support price configuration and inventory management.

The system will save your custom variant options and values, which can be used independently without linking them to attributes.

:::

### Manage linked attributes

You can view and manage the link status in the variant settings:

- Click the link icon next to a variant to view its linked attribute, or choose **Unlink**.
- Once unlinked, variants and attributes will no longer sync, and you can edit them independently.
- Previously linked values will be retained but won’t update automatically. If any of these values no longer match the current variant or attribute, the system will prompt you to manually clean up the invalid entries.

## Product pricing

Pricing determines the selling price of a product and directly affects sales and profitability. A well-thought-out pricing strategy considers factors such as costs, market competition, and profit margins.

### Pricing logic

On Genstore, pricing is determined by:

- **Cost price**: The amount paid to produce or purchase the product. Ensuring the selling price is higher than the cost price is key to profitability.
- **Market expectations**: Consider the target audience's price acceptance and competitor pricing.
- **Profit margin**: Adjust pricing to ensure a sustainable profit.

### Set pricing

Genstore allows merchants to set the following:

- **Price**: The actual selling price.
- **Compare-at price**: The pre-discount price, shown to highlight discounts.
- **Cost per item**: The manufacturing or purchase cost, excluding shipping and other fees.
- **Profit**: Calculated as selling price minus cost price.
- **Profit margin**: Formula: `(Price - Cost) × 100 / Price`.
  ::: tip
  If the product is taxable, profit details will not be displayed.
  :::

## Inventory management

Merchants can track stock using:

- **SKU (Stock Keeping Unit):** A unique identifier for a product used to distinguish different products and their variants (such as size, color, etc.). Each SKU corresponds to a specific variant of a product, and merchants can use it to manage inventory and sales.
- **Barcode (ISBN, UPC, GTIN, etc.):** A machine-readable graphic code (such as a 1D barcode or QR code) that allows for quick retrieval of product information through scanning devices. Common barcode types include UPC (Universal Product Code) and EAN (European Article Number).
  - Barcodes typically consist of numbers and bars, and can be recognized by barcode scanners.
  - They are globally recognized product identifiers, applicable for supply chain, logistics, and retail transactions.
  - Barcode codes are usually generated by authoritative organizations, such as GS1.

### Inventory options

- **Continue selling when out of stock**: Allow customers to order products that are out of stock
- **Track inventory**: Set stock quantity and track inventory changes in real time
- **Inventory quantity**: Enter based on actual stock levels

### Multi-location inventory

If you manage inventory across multiple locations, the product quantity for each location will be displayed. You can click **Manage location** to adjust the inventory locations for this product.

- **Unavailable:** The quantity of units that cannot be sold.
- **Committed:** The quantity of products in orders that have not been shipped yet. Draft orders do not count towards the committed quantity until they become actual orders.
- **Available:** The quantity of units that are available for sale.
- **On-hand:** The total quantity of units available at a specific location, including the committed, available for sale, and unsellable products.
- **Incoming:** The quantity of products incoming to a specific location. For more information, refer to the [inventory status](./operate-inventory-manage-status.md).

## Shipping

Set shipping-related details such as product weight, country of origin, and HS code.

> To add customs information (such as HS code, country of origin, material, etc.), check the **Add customs details** box.

### Packaging

To accurately calculate shipping costs and ensure product safety, you can set up packaging information for your products. You can use default packaging or create custom packaging.

- If you need to manage packaging materials or create custom packaging, click **Manage package** or refer to the [package management](./operate-fulfillment-manage-package.md) documentation for more details.

## Search engine listing

Optimize your product title, description, and URL to help search engines better crawl your product pages, increasing visibility.

### Steps

1. On the **Product details** page or while creating a product, locate the **Search engine listing** section and click the **pencil icon**.
2. In the **Title** field, enter a descriptive title for the product. This title will appear as a link in search engine results.
3. In the **Meta description** field, enter a brief product description.
4. In the **URL handle** field, you can modify the product's URL segment. **Note:** The URL cannot contain spaces.

## Quick settings (right panel)

### Product status

Adjust the product’s status:

- **Draft**: Not yet published.
- **Active**: Available for purchase.
- **Unlisted**: Hidden from storefront; only accessible for purchase via shared direct link.

### Channels & Markets

The **Channels & Markets** section defines the **sales channels** and **markets** where a product can be sold.

#### Sales channels

1. In the **Sales channels** section on the right side of the Product details page or the create product page, the system will automatically display the current sales channel, with **Online Store** set as the default.
2. To add a sales channel, click the pencil icon next to the **Sales channels** title, then check the desired channel in the pop-up window and save.
3. To set a publish time for a specific channel, click the calendar icon next to that channel and select the publish time (based on the store’s time zone). Once the scheduled time is reached, the product will be automatically published to the specified sales channel.
    - **Note**: The publish time cannot be earlier than the current time.
4. To remove an added sales channel, click the pencil icon next to the **Sales channels** title, uncheck the desired channel in the pop-up window, and save.

#### Markets

1. When a store is created, the system automatically generates a **primary market** and assigns all products to it. When you add a new market, all products are also automatically assigned to that market.
2. On the **Product details** page or the **Create product** page, go to the **Channels & Markets** -> **Markets** section on the right to view and adjust market assignments.
    - By default, the list displays both inactive and active markets.
3. To add or remove a market, click the **pencil icon** next to the **Markets** title. In the pop-up window, check or uncheck markets as needed.
### Product information

This section provides additional fields for internal management and backend operations:

- **Vendor**: Identifies the product’s manufacturer or supplier
- **Tags**: Add multiple keywords to support backend search, filtering, and automation
- **Display tags**: Highlight key features and selling pointsa, shown above the product title by default. You can add multiple tags, which will appear in the configured order. To adjust their display position, go to the [product page template in the theme editor](./operate-store-design-themes-edit-guide-page-product.md).
- **Custom product type**: A custom label for product classification, separate from system categories, used for internal organization
- **Collection**: Group products into a set such as “New Arrivals” or “Summer Collection” for easier front-end display and marketing management
  - When a store is newly created, the system automatically generates a default product collection. When adding products, they will be linked to this default collection to help you quickly publish and organize products in bulk.
     For more details, see [Product collections](./operate-product-collections.md).

### Product template

In the **Theme template** section, you can update the template associated with the product to enhance its presentation on the customer-facing side.

 For more details, see the [Theme editor guide](./operate-store-design-themes-edit-guide.md).
