# Set up Google data sharing

By connecting your Genstore store to Google, you can use tools like Google Analytics, Google Ads, and Google Tag Manager to track site traffic, analyze ad performance, and understand customer behavior—helping you improve your marketing strategy with data-driven decisions.

::: tip
This feature is **optional**. If you enable data sharing, we recommend updating your [privacy policy](./settings-privacy.md) to clearly explain what data you collect and how it will be used.
:::

You can choose one of the following methods to set up data sharing with Google:

- **Use the built-in Google & YouTube sales channel for automatic data sync** (recommended)
- Manually embed Google tracking code for full control

## Share data using the Google & YouTube sales channel (recommended)

::: tip
The **Google & YouTube channel is a built-in app**. It is automatically installed after your store is created—no manual installation is required. You can find it under **Sales channels** in your admin.
:::

### Steps
1. Log in to Gestore admin.
2. Go to **Sales channels** -> **Google & YouTube**.
3. Click **Connect Google account** and complete the authorization.
4. Under the **Connect your google merchant center account** section, select or create a Google Merchant Center account:
   - If you already have a Google Merchant Center account, select it from the drop-down and click **Connect**.
   - If you don’t have one yet, click **Create new account** to create one.
5. Choose your target country and language.
6. Accept Google’s terms and complete setup.

For detailed guidance, see: [Google & YouTube sales channel setup guide](./expand-sales-channels-google.md)

Once the setup is complete, Genstore will automatically sync store data with your connected Google tools. You can choose to enable Google Analytics, Google Ads, or Tag Manager based on your needs.

## Embed Google tracking code manually

If you prefer more control over which data is tracked and where, you can embed Google tracking scripts directly into your store’s theme files.

### Steps

1. Log in to your Genstore admin.
2. Go to **Store -> Online Store -> Themes**, find your current theme, and click **... -> Edit code**.
3. Open the template file you want to track, and paste your Google tracking code.
4. Click **Save** in the upper right corner.

::: tip
You can embed:
- Google Ads conversion tracking code
- Google Analytics (GA4) measurement ID
- Google Tag Manager container code
:::

### Reference

- [Set up Google Ads conversion tracking](https://support.google.com/google-ads/answer/12216424)

## View your data in Google tools

After setup, you can monitor synced data using the following tools:

|Tool|What it does|Link|
|---|---|---|
|**Google Analytics**|Monitor traffic, page views, user behavior, and ad conversions|[Open Google Analytics](https://analytics.google.com)|
|**Google Ads**|View ad performance, impressions, CTR, and conversion metrics|[Open Google Ads](https://ads.google.com)|
|**Google Tag Manager (GTM)**|Manage and monitor tracking tags and scripts|[Open GTM](https://tagmanager.google.com)|
