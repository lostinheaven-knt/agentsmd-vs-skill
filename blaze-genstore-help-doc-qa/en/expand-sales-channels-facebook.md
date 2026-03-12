# Facebook & Instagram sales channel

In Genstore, you can promote and sell products through the **Facebook & Instagram sales channel**. By connecting your Facebook account, your product information will automatically sync to both Facebook and Instagram Shops. With AI-powered advertising, you can precisely target customers, improve conversion rates, and grow your brand reach.

::: tip

**Facebook & Instagram is a built-in channel**. It is automatically installed after you complete your initial store setup — no manual installation needed. You can find it in the **Sales channels** section of your Genstore admin.

:::

## Key benefits

- Sync product descriptions and images to Facebook and Instagram Shops.
- Leverage social media advertising to boost performance and expand brand exposure.
- Track and analyze eCommerce data with Facebook Pixel for continuous optimization.
- Manage inventory across multiple sales platforms.

## Facebook account requirements

The Facebook & Instagram sales channel is available on all [Genstore plans](./start-understand-pricing-plans.md). Before you start, make sure to:

- Have a **Facebook Business Manager** account with admin access.
- Connect your Business Manager to your Facebook Page and ad account.
- If you already have a personal ad account, link it to Business Manager. If you don’t have one, [create an ad account in Business Manager](https://www.facebook.com/business/help/910137316041095?id=420299598837059).
- Your Facebook Page must be published, and each business Page can only belong to one Business Manager.
- Your Genstore store must be an active online store without password protection. See [how to remove your online store password](./operate-store-design-preference#turn-off-password-protection).

For more information, see:

- [Business Manager overview](https://www.facebook.com/business/help/1710077379203657)
- [ad account guide](https://www.facebook.com/business/help/195296697183682?id=829106167281625).

## Prerequisites

When binding a Pixel, there are two reporting paths. Please confirm your needs first:

- **Pixel reporting (browser-side tracking):** Only Pixel binding is required. No Access Token needed.
- **Conversions API reporting (server-side tracking):** If you want to send events back via the server, you need to additionally configure an Access Token.

::: info  
Pixel binding is required. Access Token configuration is only needed when using the Conversions API, and it can be maintained at any time in the merchant admin after binding.  
:::

### Get an Access Token (optional)

If you want to use the **Conversions API** to send events from the server to Facebook, you must generate and configure an Access Token. If you only use Pixel front-end tagging (browser-side tracking), you generally do not need to fill in an Access Token.

1. Go to **Facebook Business Manager**.
2. Select **Data Sources** -> **Datasets & pixels**, and click **Add** to create a new Pixel.
3. Go to **Events Manager**, click **Connect Data**, and select the data source you want to connect.
4. Select the Pixel data to connect.
5. Click **Settings**, and it is recommended to use the default recommended settings.
6. Select the connected Pixel name, click **Settings**, and find **Set up direct integration**.
7. Click **Generate access token**, then copy and save it securely.

## Set up the Facebook & Instagram sales channel and sync products

1. Log in to your Genstore admin.
2. Go to **Sales channels** -> **Facebook & Instagram**.
3. Click **Connect Facebook account** to sync your Facebook information.
4. On the Facebook authorization page, click **Connect** to complete account connection.
5. Choose or create a **Facebook business asset group** to link.
6. Select or create a **Meta Pixel** for data tracking and ad optimization.
7. Click **Submit for review**.
8. Once the review is complete, products in your store that have the Facebook & Instagram sales channel configured will be automatically synced to the Facebook product catalog. 
   > For instructions on how to configure sales channels for products, please refer to [Configuring Sales Channels for Products](./operate-product-create#sales-channels).

## Set up Instagram Shop

::: tip

Be sure to review the [Facebook & Instagram commerce eligibility requirements](https://www.facebook.com/business/help/2347002662267537?helpref=faq_content) before you start.

:::

### Steps to set up Instagram Shop

1. [Sign up for a Facebook account](https://www.facebook.com/r.php?entry_point=login).
2. Create a Facebook Page linked to your account and make sure you’re the Page admin.
3. [Set up a Meta Business account](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fsettings%2Fpeople%2F61577096798237%3Fbusiness_id%3D750381927420085%26verification_email_status%3Dsuccess) with admin permissions to manage your assets (e.g., ads, Meta Business Suite, Commerce Manager).
4. Complete the Facebook & Instagram sales channel setup in Genstore to sync your products to your Meta product catalog. See [set up the Facebook & Instagram sales channel](#set-up-the-facebook-instagram-sales-channel-and-sync-products).
5. [Sign up for an Instagram account](https://www.instagram.com/).
6. Download the Instagram mobile app, sign in, and convert your account to a [professional account](https://www.facebook.com/business/help/502981923235522?helpref=faq_content). _This step can only be completed on mobile._
7. Create a [Commerce Manager account](https://www.facebook.com/commerce_manager?business_id=1073642577586787) within Meta Business to manage your online store.
8. Follow the [Meta guide to set up your shop on Facebook and Instagram](https://help.instagram.com/1187859655048322), and authorize your Instagram professional account to use store resources (e.g., product catalog).
9. Apply for Instagram Shopping in the Instagram mobile app via **Settings** -> **Shopping**. Approval may take 5-7 business days.
10. Once approved, you can add and feature products on Instagram and start selling. See [manage your shop and add featured products](https://help.instagram.com/601476600985792/Manage%2Byour%2Bshop%2Bwith%2Brecommended%2Bproducts).

## Unlink Facebook account

If you no longer need the Facebook & Instagram sales channel, you can disconnect your Facebook account:

1. Log in to your Genstore admin.
2. Go to **Sales channels** -> **Facebook & Instagram**.
3. Click **Settings** in the top right corner.
4. Click **Disconnect** next to your Facebook account.
5. Confirm the disconnection in the pop-up dialog.