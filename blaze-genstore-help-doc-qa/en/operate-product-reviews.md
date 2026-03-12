# Product reviews

**Product reviews** is a built-in customer feedback tool in Genstore. **No installation required**—you can access it directly from the admin menu to manage all review-related settings. This feature helps you collect, display, and manage authentic product reviews, building trust and boosting conversions and repeat purchases.

With Genstore reviews, you can start collecting customer feedback and display product reviews in three ways:
- **Review collection**: Display all reviews on the homepage to enhance user trust and facilitate purchase decisions.
- **Product page review section**: Add a review section to product detail pages, showing star ratings and user feedback to improve visibility and conversion rates.
- **Star rating widget**: Display the overall product rating through star ratings to help users identify quality products.

In addition to customer reviews on the storefront, you can also manually add reviews for products in the Genstore admin or import historical review data from other platforms to enrich review content and enhance product display effectiveness.

## Settings

1. Log in to Genstore admin and go to **Store** -> **Products** -> **Reviews**.
2. Click **Settings** to configure the following:

### Auto-publish reviews by rating
Set whether to automatically publish reviews:
  - **Off** (default): Reviews need manual approval before publishing.
  - **On**: System automatically publishes reviews, only applies to new reviews after enabling. You can also set a minimum star rating, e.g., automatically publish reviews with 3 stars or above.
  - Whether to show the customer's full name.

### Review posting permissions
  - **No restrictions**: All visitors can review or reply to reviews
  - **Login required to post reviews**
  - **Login and purchase required** to post reviews on the product

### Review display settings

For products with no reviews, you can choose the following display methods:
- **Show**: Even without reviews, still display the rating stars.
- **Hidden**: Hide rating stars for products without reviews.

## Import reviews

For reviews from other platforms or applications (such as Shopify, Loox, Judge.me, etc.), you can also import them via CSV files. After filling out and uploading a CSV file in the specified format, you can easily migrate it to Genstore.

You can import reviews in three ways:

1. Log in to the Genstore admin and go to **Store** -> **Products** -> **Reviews**.
2. Click **Import**, select one of the following methods:
	- **Import from supported apps** (e.g., Shopify, Loox, Judge.me)
		- After selecting the platform, download the CSV template provided by the system, fill it out, and upload.
	- **Import from supported platforms** (currently supports Amazon)
		- Import Amazon review content through plugin integration.
	- **Upload local review files (CSV format)**
		- Prepare files according to the template and upload.

After uploading, go to your personal account and click **... -> Task center** in the bottom left corner to view import records:
   - **Success**: Reviews are automatically imported into the system.
   - **Failure**: You can download the failure record and re-upload.

### Import field descriptions

When uploading local review files, please prepare the files according to the following template:
| Field             | Description                | Required |
| -------------- | ------------------- | ---- |
| product_handle     | View the handle field in product search engine | Required   |
| rating         | 1-5 stars, half stars not supported    | Required   |
| title          | Review title, maximum 50 characters         | Required   |
| body           | Review content, maximum 1000 characters       | Required   |
| reviewer_name  | Limited to 100 characters            | Required   |  
| reviewer_email | Email format validation              | Required   |
| review_date    | Format: YYYY/MM/DD    | Optional   |
| reply          | Maximum 1000 characters           | Optional   |
| reply_date     | Format: YYYY/MM/DD    | Optional   |
| Media          | Multiple images separated by `;`          | Optional   |
| market         | The market where you want to display product reviews. Defaults to the primary market if left blank.       | Optional   |
| Status         | Publish, Hidden    | Required   |
| like           | Enter integer, maximum 999999999   | Required   |

## Merchant review publishing

You can also manually publish reviews for products in the Genstore admin, allowing you to showcase user feedback and enhance the product review display style.

Entry: **Store** -> **Products** -> **Reviews** -> **Write reviews**

| Field    | Description             | Required |
| ----- | ---------------- | ---- |
| Select product  | Select the product to publish the review for        | Required   |
| Reviewer name | Enter the reviewer's name, limited to 50 characters          | Required   |
| Review time | Review publishing time          | Required   |
| Review title  | Limited to 100 characters         | Required   |
| Review content  | Limited to 1000 characters        | Required   |
| Rating  | Enter the reviewer's rating for the product, 1-5 stars            | Required   |
| Media  | Limited to 8 images and 1 video, can be used to display product usage effects or scenarios.       | Optional  |
| Like count   | Number of likes for the review, limited to 999999999, integer   | Optional  |
| Select market  | Select the market where the review will be published, e.g., United States      | Required   |
| Verify review  | Choose whether to mark the review as a "verified" review. If left blank, the system will treat the review as 'Unverified' by default. | Optional   |

## Enable review display (theme setup)

After enabling the review feature in the admin, you also need to activate the review module in the theme editor.  
This ensures that customers can leave reviews on the storefront, view feedback from other buyers, and see star ratings on product detail pages.

1. Go to **Store** -> **Online Store -> Themes**, and click the **Customize** button next to your active theme.
2. Under the product page template, click **Add section**, switch to the **Apps** tab in the popup, and select **Product reviews**.
3. Configure display settings, including total number of reviews, star ratings, and overview style.
4. Save to see the review module on product detail pages.

## Review verification

You can mark certain reviews from verified buyers or high-quality reviews as verified reviews. To verify reviews, follow these steps:
- In the review list, click the Edit icon and check **Verify review**.
- You can also batch select the reviews you want to verify, click the **Verify** button, and a verified badge will appear in the list.

Once verified, the verified icon will also be displayed on the product detail page, visible to logged-in customers.

## Customer review submission

Once review display is enabled, customers can submit reviews directly on the storefront, including:  
1. **Star rating** — Rate products on a scale of 1–5 stars.  
2. **Text review** — Share their purchase or usage experience.  
3. **Media upload** — Upload images and videos to show real product usage.

## Show star ratings on products (theme editor)
The star rating widget is a visual component used to display users' overall ratings for products on product detail pages. It typically appears as 1–5 stars, intuitively reflecting product reputation and quality evaluations.
1. Go to **Store** -> **Online Store** -> **Themes** and click the **Customize** button for your current theme.
2. Click the **Style design** icon (third in the vertical nav bar on the left) and find **Rating**.
3. Configure the display style: include icon style and color, and choose whether to hide the star ratings for products with no reviews.
4. You can later control whether to display star ratings on product cards in featured collections, featured products, and search pages. These display rules will follow the global product review settings.

## Show review collection on the storefront (theme editor)

You can add a **review collection** section on the homepage to centrally display reviews from the entire store or specific products. Customers can click on specific reviews to view details. After logging in, they can also interact with reviews by liking, replying, etc.

Steps:

1. Go to **Store** -> **Online Store -> Themes**, click the **Customize** button next to the current theme.
2. On the page where you want to display the review collection, such as the homepage, click **Add section**, switch to the **Apps** tab in the popup, and select **Review collection**.
3. Set the style for this section.
4. After saving, the review collection will be displayed on the homepage.

::: faq

## FAQs

### Q1. Do I need to install the product review app?
> A: **No installation required**. Product reviews are a built-in feature, which is displayed in the backend menu by default.

### Q2. Do I need to manually add the review module in the theme?
> A: Yes. You need to add the **Product reviews** section under the corresponding product template for the review module to be displayed on the storefront.

### Q3. Do I need to set up the review module for each product?
> A: No. If all products share the same template, you only need to set it up once. If you need to configure different display styles for different product templates, you need to set them separately.

### Q4. How to resolve the issue of corrupted characters when importing templates?
> A: When importing reviews via the template on Windows, corrupted characters may appear. If there is any abnormal historical data, you will need to delete it and re-import the data using the latest template we provide. Ensure that you clear the related historical data before importing again and use the most recent CSV template file.

:::
