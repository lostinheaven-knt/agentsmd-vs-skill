# Manage packages

In the **Genstore** admin, you can set up and manage various packaging options, allowing you to quickly select the most suitable package when purchasing shipping labels. Based on your shipping rate settings (such as weight-based or carrier rates), you can also select a default package to ensure accurate shipping cost calculation at checkout.

> **Note**: Each SKU can only be bound to one package type. The system provides basic packaging by default, and merchants can also create custom packaging plans.

## Add custom package

You can add custom-sized packages based on your needs to ensure they fit various types of products.

### Steps:

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. Click to show **More settings**. Then in the **Saved packages** section, click **Add**.
3. Enter a name for the package (e.g., "Small Box," "Standard Envelope," etc.).
4. Choose the type of package (e.g., box, bag, etc.).
5. Enter the **dimensions** and **weight** of the package.
6. Click **Confirm** to save. The custom package will be added to the package list for future use.

To set this package as the default for automatic shipping cost calculation at checkout, turn on the **Default** toggle in the list.

## Add carrier packages

Carrier-supplied packaging (such as USPS, UPS) comes with predetermined sizes and is suitable for specific shipping needs. To use these packages, you must first authorize your **Shippo** or another platform’s logistics account to ensure the system can integrate with the carrier’s platform and retrieve the latest package options.

### Steps:

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. Click to show **More settings**. Then in the **Saved packages** section, click **Add**.
3. Choose **Carrier standard package**.
4. Select a package type provided by the carrier.
5. Click **Confirm** to save the package.

## Set default package

Setting a default package is crucial to ensuring accurate shipping cost calculations. At checkout, the default package will automatically be added to the total weight of the order, affecting the final shipping cost. You can set and adjust your store's default package in Genstore admin.

### Steps:

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. Click to show **More settings**. Then in the **Saved packages** section.
3. Locate the package you want to set as default, click **...** and click to choose **Set as default**.

**Note**: The system will only use one package for shipping cost calculations, so make sure to choose the most appropriate package.

## Edit and delete packages

If you need to change or delete an existing package, you can easily adjust it in the **Genstore** admin. Please note that default packages cannot be deleted.

### Edit package:

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. Click to show **More settings**. Then in the **Saved packages** section, locate the package you want to edit, click **...** and then click the **Edit** button.
3. Modify the package’s name, dimensions, weight, etc., and click **Confirm** to save the settings.

### Delete package:

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. Click to show **More settings**. Then in the **Saved packages** section, locate the package you want to delete, click **...** and then click the **Remove** button. Confirm the deletion.

## Carrier packages and Shippo account authorization

When adding carrier-supplied packages, you need to connect your **Shippo** account. Shippo is a third-party carrier supported by **Genstore** that helps you access and use shipping label services from multiple carriers.

### How to authorize your Shippo account:

1. Go to **Genstore admin** -> **Settings** -> **Shipping and delivery**.
2. In the **Carrier management** section, click **Authorize** near Shippo.
3. Enter your **Shippo account information** to authorize the connection.
4. Once authorized, you will have access to carrier packaging and shipping labels and can select the most suitable shipping options at checkout.

## Assign packages to products

Genstore allows you to assign specific packages to products and their variants (SKUs) during product creation or management. This helps ensure accurate shipping cost calculations based on the actual packaging used for each item.

### Single variant products

1. Go to **Store** -> **Products** -> **Add product**.
2. In the **Shipping** module, you will see **Default package** selected automatically.
3. To use a custom package, click the dropdown menu and select from your saved packages.
4. To manage your packages, click **Manage packages** to navigate to the package management page.
5. Complete the rest of the product information and click **Save**.

### Multi-variant products

For products with multiple variants, you can specify different packages for each SKU:

1. In the product detail page, select multiple SKUs in the **Variant specification** section.
2. Click **Bulk edit**.
3. If the **Package** field is not visible, click **Columns** and check the **Package** option.
4. Select the desired package for the selected SKUs.
5. Click **Save** to update all selected SKUs.

If you want to assign the package for one of the product variant, you can click the variant title to enter its detail page. Then in the **Shipping** module, you can select the package for this variant.

### Package assignment during product import

When importing products via CSV, you can specify the default package for each product. The system will apply this package to all SKUs of the imported product unless otherwise specified.
