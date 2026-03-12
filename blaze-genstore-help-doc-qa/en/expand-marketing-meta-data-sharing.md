# Set up Facebook data sharing

By sharing your Genstore store data with Facebook, you can use advanced tools like Meta Pixel and the Conversions API to track traffic, improve ad targeting, and increase conversion performance.

::: tip
This feature is **optional**. If you enable data sharing, we recommend updating your [privacy policy](./settings-privacy.md) to clearly explain what data you collect and how it will be used.
:::

You can choose one of the following methods to connect your store to Facebook:

- **Use the built-in Facebook & Instagram sales channel to sync data automatically** (recommended)
- Manually embed the Meta Pixel code for custom tracking

## Share data using the Facebook & Instagram sales channel (recommended)

::: tip
The **Facebook & Instagram channel is a built-in system app**. It is automatically installed after your store is set up—no manual installation is needed. You can find it in the **Sales channels** section of your Genstore admin.
:::

### Steps

1. Log in to your Genstore admin.
Go to **Sales channels** -> **Facebook & Instagram**.
2. Click **Connect Facebook account** to sync your Facebook information.
3. On the Facebook authorization page, click **Connect** to complete account connection.
4. Choose or create a **Facebook business asset group** to link.
5. Select or create a **Meta Pixel** for data tracking and ad optimization.
6. Click **Submit for review**.
Once the review is complete, products in your store that have the Facebook & Instagram sales channel configured will be automatically synced to the Facebook product catalog.

For a full walkthrough, see: [Facebook & Instagram sales channel setup](./expand-sales-channels-facebook.md)

Once complete, Genstore will automatically sync store traffic and order data to Facebook.

## Embed Meta Pixel manually using the code editor

If you prefer to customize which pages and actions are tracked, you can manually add the Meta Pixel code to your store templates.

### Steps

1. Log in to your Genstore admin.
2. Go to **Store -> Online Store -> Themes**.
3. Find your current theme and click **... -> Edit code**.
4. Open the template where you want to add tracking, and paste the Meta Pixel code.
5. Click **Save** in the top-right corner to publish your changes.

### Additional resources

- [Meta Pixel conversion tracking guide](https://developers.facebook.com/docs/meta-pixel/implementation/conversion-tracking#standard-events)
- [Standard events reference](https://developers.facebook.com/docs/meta-pixel/reference#standard-events)

## View shared data in Facebook

Once your data sharing setup is complete, you can track your store’s performance using the following tools:

|Tool|What it does|Link|
|---|---|---|
|**Meta Ads Manager**|Track ad budget, performance, and conversion rates|[Go to Ads Manager](https://www.facebook.com/adsmanager)|
|**Events Manager**|Monitor Pixel events, Conversions API data, and user behavior tracking|[Go to Events Manager](https://www.facebook.com/events_manager)|
