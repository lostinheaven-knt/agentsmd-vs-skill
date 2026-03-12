# Buy Button

**Genstore Buy Button** is a lightweight sales tool that allows merchants to embed purchase buttons on any webpage, enabling customers to complete purchases without leaving the current page. This guide covers key benefits, installation and authorization, step-by-step creation and configuration, and FAQs to help you use Buy Button effectively and boost conversion rates.

## Key benefits

Buy Button provides the following features to optimize the shopping experience and drive sales:

- **Seamless purchase experience**: Embed the button on any page (e.g., blog, website, social media, partner sites) so customers can purchase instantly.
- **Centralized order management**: All Buy Button orders are tracked and managed in the Genstore admin, simplifying sales analysis.
- **Flexible customization**: Multiple display styles and design options adapt to your page layout and brand identity.
- **Multi-channel reach**: Embed Buy Button in your website, social media, landing pages, or email campaigns to quickly turn traffic into sales.

::: tip
We do not recommend using Buy Button on your Genstore online store or Genstore blog to avoid affecting the checkout experience.
:::

## Install and authorize

1. Visit the [Genstore App Store](https://apps.genstore.ai).
2. Search for `Buy Button` and open the app detail page.
3. Click **Install**. The system will redirect you to your Genstore admin.
4. Follow the prompts to complete installation and authorize the Buy Button channel.
5. _(Optional)_ Pin the app to your sidebar for easier access later.

## Create and configure Buy Button

### Step 1: Access Buy Button

- In your Genstore admin, go to **Apps -> Buy Button**.
- If not pinned, navigate to **Apps -> Installed apps**, find **Buy Button**, and click **Launch app**.

### Step 2: Select target products or collections

On the app page, click **Create** next to **Product** or **Product collection**, then select the product or collection you wish to generate a Buy Button for.

Note: Before selecting a product or collection, you must add the **Buy Button** sales channel to the target product or products in the target collection. For detailed steps, refer to [Products](./operate-product-create.md#sales-channels).

### Step 3: Set layout style and preview

- In the left **Layout style** panel, choose your preferred layout:
    - **Basic**: Only displays the Buy Button.
    - **Classic**: Shows product image and price.
    - **Full**: Includes product details, image, and price.
- The center preview updates in real time. You can switch device views (desktop, mobile) at the top of the preview.

### Step 4: Configure button behavior and interactions

Under **Button click action**, choose what happens when customers click the button and configure behavior-specific settings:

- **Add to cart** (default)
    - Customize cart appearance, including title, helper text, button label, cart background color, and text color.
- **Checkout now**
    - Configure how the checkout page opens:
        - **Open in a new window**
        - **Open in the current window**
- **View product details**
    - Customize the product details pop-up, including button label, quantity selector, and typography (font, size, and color for product name and price).

### Step 5: Global style design

Beyond the click behavior styles above, you can use the **Design** module to customize overall styles, including:

- **Button styles**: background color, text color, border radius, font, and font size.
- **Global layout**: alignment of text and button, and quantity selector toggle.
- **Cart**: cart title, subtotal price, button label, and empty cart message.
- **Checkout**: how the checkout page opens (in a new window or current window).
  > Note: If embedding Buy Button on a Wix page, set checkout to open in a new window.

::: tip  
These settings apply only to the generated Buy Button. They will not affect your original product page or store theme.  
:::

## Embed the code

* After completing your setup, click **Next step** to generate the embed code.
* Copy the code and paste it into your webpage’s HTML editor (e.g., blog platform, CMS, or static website). Here are detailed embedding steps for popular platforms:

### Shopify
1. Go to **Content -> Blog Posts** in your Shopify admin.
2. Open an existing blog post or create a new one.
3. In the content editor, click the `Show HTML` icon on the far right of the rich text editor toolbar.
4. Paste the Buy Button embed code into the HTML.
5. Click **Save**.

### Wix

1. Log in to Wix, go to My Sites, select the site you want to edit, and click **Edit Site**.
2. In the Wix editor, click the `+` button, select **Embed Code -> Embed HTML**, and add an HTML widget to your page.
3. Click the newly added widget, open **HTML Settings**, select **Code**, paste the Buy Button code into the input box, and click **Apply**.
4. Resize the HTML widget to ensure the Buy Button displays completely.
5. Click **Publish** when done.

Note: Due to platform limitations, Buy Button cannot use the **Open in current window** option on Wix. Customers will complete purchases in a new window.

### WordPress

1. In your WordPress dashboard, go to the post or page you want to edit.
2. Create new content or edit existing content.
3. In the block editor, click the `+` button, search for `Custom HTML`, and insert the block.
4. Paste the Buy Button code into the Custom HTML block.
5. (Optional) Adjust the button's position:
     - Move the block: Use the arrow buttons in the block toolbar or drag the block.
     - Preview: Click **Preview** in the block toolbar.
6. When done, click **Save draft**, **Preview**, or **Publish**.

If using the WordPress Classic Editor, no custom HTML block is needed. Switch the editor to **Text mode** and paste the code in the editor.

::: faq
## FAQs

### Q1. Will Buy Button content adjust automatically based on customer location?

> A: Yes. Genstore identifies the customer’s market via their IP address and checks if the selected product is available there. If it’s unavailable, a message will appear during checkout and the order cannot be completed. Ensure your product is enabled in the [target market](./global-market-settings-product-pricing.md).

### Q2. Can I edit the Buy Button style after embedding it on my page?

> A: No. The style is fixed when the embed code is generated. To change the style, reconfigure the button in your Genstore admin and replace the embed code.

### Q3. Can I embed multiple Buy Buttons on a single page?

> A: Yes, you can. We recommend setting consistent click behaviors (e.g., all using **Add to cart** or **Checkout now**) to maintain a smooth, unified purchasing experience.

:::