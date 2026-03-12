# Shopify store migration

This guide explains how to use the **Genstore Migration Tool** to migrate your Shopify store data (including customers, products, orders, etc.) to Genstore.

## Preparation

Before migrating, please ensure the following preparations are complete to ensure data integrity and smooth migration:

- **Report payment channels**: If the Shopify store has enabled payment functionality, please notify the payment channel in advance to avoid payment restrictions or risks due to store changes.
- **Confirm store status**: Ensure the Shopify store is operating normally, without freezing, closing, or other abnormal conditions.
- **Check product inventory and order status**: It is recommended to carefully check the product inventory and order status of the Shopify store to ensure data accuracy.
- **Back up Shopify store data**: It is strongly recommended to back up Shopify store data before migration to prevent unexpected situations.
- **Clean up useless data**: You can clean up useless draft orders, canceled orders, etc., to reduce the amount of migrated data and improve efficiency.
- [Ensure the Genstore Migration Tool is installed](./start-migrate-guide#install-the-genstore-migration-tool).

## Start migration

:::tip

- When the amount of store data is large, the migration may take a long time.
- Do not modify API permissions during the migration process, otherwise it may cause the migration to fail.
- Try to avoid large-scale data modifications to the Shopify store during the migration process to prevent data inconsistency.

:::

### Step 1: Obtain Shopify API access permissions

1. Log in to your Shopify admin and go to **Settings** -> **Apps and sales channels**.
2. Click **Develop apps**, then click **Create an app** in the top-right corner. 
3. [First time setup] If this is your first time, the system will prompt you to enable custom app development. Confirm and click **Create an app** again. 
4. In the modal window, enter the **App name** and select an **App developer**. The app developer can be the store owner, or any staff or collaborator account with the **Develop apps** permission. Then click **Create app**.
5. In the **Overview** tab, click **Configure Admin API scopes**, select all permissions that start with `read_`, and click **Save**.
6. Go back to the **Overview** tab and click **Install app**.
7. In the confirmation popup, click **Install**.
8. In the **API credentials** tab, under **Admin API access token**, click **Reveal token once** to get your **Admin API access token**.  
    **Note:** This token can only be viewed once. Please store it securely.

::: tip

Protected customer data access requirements

On the Shopify platform, certain customer information—such as names, addresses, email addresses, and phone numbers—is classified as PII (Personally Identifiable Information) and is considered protected data.  

Only merchants subscribed to the **Shopify Grow**, **Shopify Advanced**, or **Shopify Plus** plans can access this sensitive information through APIs.

In addition to PII, other data such as shipping rates, orders, and gift cards are less restricted. However, access to these types of data still requires authorization.

:::

### Step 2: Open the Genstore Migration Assistant

1. Log in to the Genstore admin and navigate to **Apps**.
2. On the **Installed** tab, find **Migration Tool**.
3. Click **Launch app**, select **Shopify** as the migration source, and click **Start migration**.

### Step 3: Store authorization

1. Enter the Shopify store domain to be migrated.
::: tip
Please enter the full domain ending with `myshopify.com` (e.g., `sample.myshopify.com`). Custom domains (e.g., `brand.com`) are not supported.
:::
2. Enter the access token, that is, **Admin API access token**.
3. After completing the settings, click **Next**.

### Step 4: Select migration modules

Genstore supports migrating the following modules from Shopify to Genstore:

| Module            | Required | Dependencies     |
|-------------------|----------|------------------|
| Store             | ✅ Required | —                |
| Customers         | Optional | Store            |
| Products          | Optional | Store            |
| Orders            | Optional | Customers, Products |
| Discounts         | Optional | Customers, Products |
| Custom pages      | Optional | Store            |
| Blog              | Optional | Store            |
| URL redirects     | Optional | Store            |
| Navigation menus  | Optional | Store            |
| Theme templates   | Optional | Store            |

:::tip

- We recommend migrating your **products** and **customers** first. This ensures that when orders are migrated, they can be properly linked to the corresponding product and customer information in Genstore.
- **Theme migration** supports 13 official Shopify themes, including Dawn, Spotlight, Sense, Craft, Ride, and others. Related content like products, pages, blogs, and menus will be included automatically.
:::

For common questions regarding the migration of each module, please refer to the [FAQ section](./start-migrate-from-shopify-faq.md).

### Step 5: Customize migration settings

You can select specific data for migration based on filter conditions:

- Products: Filter by status (published, draft, archived, etc.).
- Orders: Filter by order creation time (such as 2024-01-01 to 2024-12-31).
- Discounts: Whether to migrate disabled or expired discount codes.

### Step 6: Start migration

1. After confirming all settings, click **Start migration**.
2. The system will start processing the migration, and you can view the migration progress in the application interface. The migration time depends on the amount of data, please be patient.
3. After the migration is complete, you can enter the Genstore admin to further improve the store settings. It is recommended to read [Store Quick Launch Checklist](./start-quick-launch-checklist.md)

## View migration records

After completing the store migration, you can view all migration history records in the Migration Assistant app, including:

- **Migration time**
- **Migration platform** (Shopify)
- **Store domain**
- **Migration modules**
- **Migration data results**
- **View error details (You can export the error data to facilitate review and troubleshooting)**

## Post-migration checklist

After completing the migration, use this checklist to confirm your store is fully configured and accessible to customers.

- [Post-migration checklist](./start-migrate-checklist.md)

## Pre-launch setup

After completing your store migration, follow the steps below to finalize your configuration and get your store ready for launch.

### Step 1: Complete your basic store information

**Path:** **Settings -> General**  
Make sure the following information is accurate:

- Store name and contact details
- **Default currency** (must match your payment system’s currency)
- **Time zone** (affects order timestamps, report analytics, etc.)
- Brand logo, brand colors, and social media links

### Step 2: Set up your domain and URL redirects (if applicable)

**Path:** **Settings -> Domains**

- Connect a custom domain or update the default `.genmystore.com` domain
- Set up **URL redirects** from your old website to preserve SEO rankings and user familiarity

### Step 3: Review product displays and inventory settings

**Path:** **Products**

- Ensure product categories, titles, descriptions, images, pricing, and inventory are correct
- Reorganize products into collections as needed

### Step 4: Choose a theme and customize your storefront

**Path:** **Store -> Online Store -> Themes**

- Select a theme and adjust layout, colors, and content
- Use the theme editor to edit the homepage, product pages, collection pages, etc.
- Use the code editor for advanced customizations (optional)

### Step 5: Create policy pages

- Create pages for privacy policy, return & refund policy, and terms of service: **Settings -> Policies**
- Set up navigation menus: **Store -> Online Store -> Menus**
- Enable the policy pages  **Path:** **Store -> Online Store -> Themes**

### Step 6: Set up shipping and taxes

- **Shipping:** **Settings -> Shipping and delivery**
    - Configure shipping origin, warehouses, shipping zones, and rates
    - (Optional) Connect shipping providers and enable label printing
- **Taxes:** **Settings -> Taxes and duties**
    - Enable automatic tax calculation or manually configure applicable tax rates

### Step 7: Configure payment methods and checkout process

- **Payment:** **Settings -> Payments**
    - Enable **Genstore Payments** or third-party payment providers
- **Checkout:** **Settings -> Checkout**
    - Choose required customer information (email, phone, address)
    - Configure payment authorization (automatic or manual)

### Step 8: Preview your storefront and verify all pages and links

- Check the display of homepage, product pages, cart, and checkout
- Test all navigation links for broken links
- Preview the responsive layout on mobile and desktop
- Confirm **SEO metadata** (titles, descriptions, URLs) on all key pages

### Step 9: Place test orders and verify key features

- Simulate a full order flow: place order, payment, shipping
- Simulate failed transactions, refunds, and cancellations
- Verify that all notification emails (order confirmation, shipping updates, etc.) are sent correctly

### Step 10: Disable password protection and launch your store

- **Path:** **Store** -> **Online Store -> Preferences**
- Remove password protection to allow public access to your store

### Step 11 (Optional): Send customer account activation emails

If you migrated customer data, send bulk password reset links to help customers access their accounts again.

### Step 12 (Optional): Set up SEO, connect sales channels, and launch marketing

- Configure SEO keywords and metadata
- Connect sales channels (e.g., Google, Facebook)
- Launch marketing campaigns such as email marketing, social media promotion, and discount offers

