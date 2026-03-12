# Google & YouTube sales channel

Genstore supports the Google & YouTube sales channel to help you promote and sell products by syncing product information to Google Merchant Center. With AI-powered intelligent ad placement, you can efficiently reach your target audience across multiple platforms including Google Search, YouTube, Google Maps, and Google Shopping to optimize conversion rates and enhance brand influence.

:::tip
**The Google & YouTube channel is a built-in system app** that is automatically installed after completing the initial store setup, requiring no manual installation. You can find this channel in the **Sales channels** page of your merchant admin.
:::

## **Key benefits**

- **Easy integration** – Sync your store with Google Merchant Center for product listings.
- **Better conversions** – Use Google’s AI and media resources to improve campaign performance.
- **Smarter insights** – Connect with Google Analytics to analyze eCommerce data.

## Prerequisites

### Genstore online store requirements

Before using the Google & YouTube sales channel, your online store must meet Google Merchant Center requirements:

- Your Genstore store must be publicly accessible [without password protection](./operate-store-design-preference#turn-off-password-protection).
- Add a valid [payment service provider](./operate-payments.md) in your Genstore backend.
- Your store must provide a [refund policy and terms of service](./settings-policy.md), and ensure these policies are in your footer menu.
- Your online store must include [contact information](./start-genstore-account-create-manage#manage-store-name-and-contact-information) with at least one contact method (such as email, phone, mailing address, or contact form).
- Your store must support shipping to [supported countries/regions](./operate-fulfillment.md) and sell in currencies appropriate for those countries/regions.
- You need to [set up shipping rates](./operate-fulfillment-shipping-profile-shipping-rate.md) based on your sales regions to ensure compliance with Google Merchant Center requirements.

During the setup process, Genstore will provide a checklist to help you complete all prerequisites.

### **Google account requirements**

To use the Google & YouTube sales channel, you need a Google account and must create a Google Merchant Center account. Google Merchant Center is primarily used to store your store and product data and supports Google Ads and other services.

If you don't have a Google account, you can create one when setting up the Google & YouTube sales channel.

## Google Merchant Center account sync considerations

After successfully connecting to Google Merchant Center, the following information will sync from Genstore to Google:

- Store products with the Google & YouTube sales channel configured. For instructions on how to configure sales channels for products, refer to [Configuring Sales Channels for Products](./operate-product-create#sales-channels).

If your Merchant Center account already has product feed data, the system will overwrite this data to maintain consistency with your Genstore store.

## Connect to Google Merchant Center

Before using the Google & YouTube sales channel, you need to link your Google account and Google Merchant Center to sync products with Google.

1. Log in to your Genstore merchant admin.
2. Click **Sales channels** -> **Google & YouTube** to enter the Google & YouTube sales channel authorization page.
3. Click **Connect Google account** and complete the Google account authorization.
4. In the **Connect your Google Merchant Center account** dropdown, select or create an account:
   - Select an existing Merchant Center account and click **Connect**. Note: The Google account you link should be an admin account for the Google Merchant Center account you want to connect.
   - If you don't have a Merchant Center account, you can click **Create new account** to create one.
5. Select the target country/region and language for your product listings.
6. After confirming all information, click **Complete setup**.

## Product sync settings
### Set up product upload rules for Google
1. Click **Manage products** to enter the product management page.
2. Click **Product upload rules** to enter the rules management page. Confirm and adjust the **Basic rules** and **Product rules** to determine the scope of products uploaded from your store to GMC and the rules for syncing products to GMC. After confirmation, click **Save rules**.
3. After saving the rules, data will be retrieved from your store to the application according to your rules. This process requires some time (the duration depends on the amount of data being retrieved).
4. After data retrieval is complete, the system will notify you with a Tips message. You can see the product data in the product list of the **Product management** page. Click to view product details.

### Enable product upload
1. After product upload rules are set and data retrieval is complete, you can see product data in the product list of the **Product management** page.
2. After confirming the data, click **Enable auto upload**, and the system will start uploading the data from the list to GMC. This upload process requires some time (the duration depends on the amount of data being uploaded).
3. Products uploaded to GMC that are approved/not approved/pending review will display their corresponding status in the product management list. Products that are not approved will receive specific error reason prompts.
4. After the data upload results are available, the system will notify you with a Tips message. You can see the upload status of products in the product list of the **Product management** page.

Note: Data upload is not executed in real-time. For products with modifications and updates, the system will perform timed synchronization, executed once every hour.

## Disable product upload
1. Click **Manage products** to enter the product upload management page.
2. If you are currently in the product upload enabled state and need to disable product upload, click **Disable auto sync**, and the system will stop syncing products from your product management list to GMC.

## Get product feed link
1. Click **Manage products** to enter the product upload management page.
2. After product retrieval is complete, the system will generate a feed XML file.
3. Click **Copy feed link**. After the feed XML file is generated, you can copy the URL of the feed XML file to Google GMC and import product information to GMC through XML.

## Set up Google data tracking

1. Log in to your Genstore merchant backend.
2. In the left navigation bar, click **Sales channels** -> **Google & YouTube** to enter the **Settings page** of the Google & YouTube sales channel.
3. On the **Data tracking** tab, you can click **Add data tracking** and choose from:
   - **Google Ads**: Track behaviors such as add to cart, visit online store homepage, submit checkout, and submit orders, and set **Conversion ID** and **Conversion tag**.
   - **Google Analytics**: Create a Measurement ID to track user behavior.
   - **Google Tag Manager**: Create a **Container ID** to manage marketing tags.

## Disconnect Google account

If you no longer need the Google & YouTube sales channel, you can disconnect your Google account:

1. Log in to your Genstore merchant admin.
2. In the left navigation bar, click **Sales channels** -> **Google & YouTube** to enter the **Overview page** of the Google & YouTube sales channel.
3. Click **Settings** in the top right corner of the page.
4. Click the **Disconnect** button next to your Google account.
5. The system will display a confirmation window. After confirming the disconnection action, the Google account connection will be disconnected.

After disconnecting, the associations with Google Merchant Center, Google Ads, and data tracking will also be removed.