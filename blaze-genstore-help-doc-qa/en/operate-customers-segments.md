# Customer segmentation

As e-commerce grows, customer groups are becoming more diverse, with differing needs, behaviors, and preferences. Traditional one-size-fits-all marketing no longer works, making customer segmentation crucial for effective marketing.

Customer segmentation lets you group customers based on their information and behaviors, enabling you to create more targeted marketing strategies. This leads to:

- **Better marketing effectiveness**: Send relevant content to the right customers, improving conversion rates.
- **Enhanced customer experience**: Offer personalized recommendations and services, boosting satisfaction and loyalty.
- **Higher revenue**: Refined marketing encourages repeat purchases, increasing Customer Lifetime Value (CLV).
- **Cost efficiency**: Targeted marketing reduces waste in ad spend and promotional activities.

Genstore offers several preset templates for quick setup, and you can also create custom segments to fit your needs. You can edit or delete existing segments as well.

## Create customer segments

Genstore provides 4 preset customer segments for quick start:

- **Customers who have placed more than 3 orders in the last 90 days**: High-value customers with frequent purchases.
- **Abandoned checkouts in the last 30 days**: Customers who started but didn't complete checkout.
- **Customers who haven't purchased yet**: Customers with no orders.
- **Customers who have email subscription**: Customers who have opted in for email marketing.

You can edit these segments or create new ones using various filter conditions based on your store's needs.

### Operation steps

1. Log into your Genstore admin, click **Store** -> **Customers** -> **Segment**, then click **Create segment**.
2. **Add filter conditions**: Click **Add filter** to define segments by customer info, purchase behavior, store behavior, product preferences, email marketing, or metadata. Genstore also suggests common filters like customer creation time, last order time, total orders, and total spending.
3. **Use templates and advanced filters**:
   - **Templates**: Genstore offers segment templates for targeting potential customers, re-engaging old ones, focusing on key customers, or segmenting by behavior. Simply apply a template to filter and create a segment.
   - **Advanced filters**: Use combination filters with **AND**/ **OR** logic. Drag and drop conditions from the left to the right to build your segment.
4. **Create the segment**: After applying the filters, Genstore shows a matching customer list. Click **Create segment** to build your segment.

## Manage customer segments

Once created, view and manage your segments under **Store -> Customers** -> **Segments**. You can:

- **View segment details**: Click to see the conditions and customer list.
- **Search segments**: Quickly find segments by name.

You can also perform the following actions on each segment:

- **Edit**: Modify the segment's conditions or create a new one.
- **Duplicate**: Duplicate a segment by giving it a new name.
- **Delete**: Remove a segment. If it’s used in active campaigns, pause those first.
- **Export customer**: Export customer data from the segment by selecting the desired fields.

## Use customer segments

Customer segmentation allows you to target specific customer groups based on their needs and preferences, enabling more effective and personalized marketing campaigns. In Genstore, you can leverage segments through **email**, **discounts**, and **SMS marketing** to drive better engagement and conversion.

### Send email campaigns

You can send marketing emails to selected customer segments using **Genstore Email**. There are two ways to initiate an email campaign:

- In **Store** -> **Customers** -> **Segment**, select a target segment, and select **Send email**. You’ll be redirected to the **Email marketing** module where you can select and customize an EDM template.
- In **Marketing** -> **Email marketing**, create a campaign and select the segment as the recipient group.

:::tip

Only customers who have subscribed to your emails will receive the messages. Genstore Email validates the email addresses and sends messages to only one valid address. Therefore, the actual number of customers receiving emails may be lower than the segment count.

:::

### Create Discounts

You can create tailored discount campaigns based on customer segments to improve conversion. There are two ways to apply a discount to a segment:

- In **Store** -> **Customers** -> **Segment**, select a segment, click **Create discount**.  You’ll be redirected to the **Marketing -> Discounts** module. Choose a discount type, and apply it to that segment. Genstore supports various discount types, including
	- [Product discount](./expand-sales-discounts-product.md)
	- [Buy X get Y](./expand-sales-discounts-buy-x-get-y-free.md)
	- [Fixed bundle](./expand-sales-discounts-fixed-bundle.md)
	- [Order discount](./expand-sales-discounts-order.md)
	- [Shipping discount](./expand-sales-discounts-shipping.md)
- Or go to the **[Discounts](./expand-sales-discounts.md)** module, create a discount and select the target customer segment as the scope of the discount.

### Send SMS campaigns

You can also send SMS marketing messages to specific segments using **Genstore SMS Marketing**. Here’s how to initiate an SMS campaign from the segmentation module:

- Go to **Store** -> **Customers** -> **Segment**, select the desired segment, then click **Send SMS** to enter the **SMS marketing** module.
- The system will automatically populate the recipient group with the selected customer segment to streamline your setup.

::: tip

Before launching SMS campaigns, you must register your SMS sending workflow and obtain a verified sender number. Without completing this step, SMS campaigns cannot be initiated from the segment view. For setup instructions, see [SMS marketing](./expand-marketing-sms.md).

:::