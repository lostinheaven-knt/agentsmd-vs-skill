# Search & Discovery app

This guide shows you how to set up search and filter features in your Genstore storefront. These features help customers find products faster and improve their shopping experience. They’re provided by the official Genstore **Search & Discovery** app. You’ll need to install and configure the app before it appears on your store.

## Storefront preview

Once you finish setting up, your customers will see:

- Filter options on product listing pages, like price and availability.
- A **Sort by** dropdown on listings so they can sort by best-selling, price, date added, and more.
- Search results will intelligently display products that match the configured conditions.

## When to use this app

- Show related products on product detail pages using collections, tags, or custom product types, so customers discover more items they’ll love.
- Add filters to search and collection pages for price, availability, tags, and more, so shoppers find what they want faster.
- Adjust recommendation rules and sorting options to help increase sales.

## Install the app

1. In your Genstore admin or on the **[Genstore App Store](https://apps.genstore.ai/en/)**, search for `Search & Discovery`.
2. On the app page, click **Install**.
3. Review the permissions and click **Install** again to confirm.
4. [Optional] Click the pin icon next to the app name to add it to your admin navigation for easy access later.

## Configuration steps

### Step 1: Open the app dashboard

- In your Genstore admin, Go to **Apps** -> **Installed**, launch the **Search & Discovery** app.  
- The app has two main tabs:
  - **Filter**: manage global filter options.
  - **Related products**: set up recommendation rules and sorting.

### Step 2: Manage filter options (controls the storefront filters)

#### Create filter options

1. In the **Filter** tab, click **Add filter** in the top right.
2. On the creation page, set up:
   - **Filter type**: like product tags, vendors, custom product types, or collections.
   - **Filter name**: what customers will see on your store. You can click **Add name translations** to add the multilingual name for this filter, currently Simplified Chinese, Traditional Chinese, English, and Spanish are supported.
   - **Display format**: choose from the drop list, for example, checkbox, radio, etc.
   - **Logic option**:
     - OR: shows products matching any selected value.
     - AND: shows products matching all selected values.
3. Click **Save** when you’re done.

#### Manage filter options

- Your filters will appear in a list showing:
  - Filter type
  - Filter name
  - Available values
  - Display mode
  - Actions (edit, delete)
- Drag filters up or down to change the order they appear in your storefront.

### Step 3: Set up related products (controls product recommendations on the search results)

#### Enable the filter widgets

Before setting up recommendation rules, you need to insert the **Filter Widgets** section into your product detail page template:

1. In the app’s **Related products** tab, click **Enable now**.
2. Toggle the switch next to **Search & Discovery** to turn it on.
3. In the page selector at the top (defaults to `Home`), use the dropdown to select **Products -> Default Product**.
4. In the left-side template structure, find **Templates**, and click the **Add section** button.
5. In the pop-up section type selector, go to the **Apps** tab, then choose **Filter widgets** from the list.
6. Click **Save** in the top right to apply the section to your product detail page.

Once the filter widgets are enabled, you can go back to the **Associated Products** tab to set up recommendation rules and sorting options.

#### Choose relate rules

In the app’s **Related products** tab, check the recommendation sources you want:

  - **Same collection**: shows products from the same collection.
  - **Same product tags**: shows products with matching tags.
  - **Same custom product type**: shows products of the same custom type.
You can check multiple sources, and the app will combine them when showing recommendations.

#### Apply filter conditions

- You can specify filters that related products must match, using your global filters.

#### Set product sorting options

- In the **Product sorting options** area, pick which sorting options you want to offer customers:
  - Best Selling
  - Product Title (A-Z / Z-A)
  - Highest / Lowest Price
  - Date Added (Newest to Oldest / Oldest to Newest)
- You can choose multiple options so customers can switch between them.
- Click **Save** to apply your rules and sorting choices.

### Step 4: Customize appearance (controls how filters and recommendations look)

Once your filters and recommendation rules are set up, you can customize their look in the Genstore template editor:

1. Go to **Online Store** -> **Themes**, and click **Customize** on your active theme.
2. In the template structure on the left, find the **Filter widgets** section you added earlier and click it.
3. In the style settings, you can adjust:
   - How many recommended products appear per page.
   - Product card styles, like image ratio, button design, and card borders.
   - Whether to show product tags, prices, availability, and other key info.
4. When you’re done, click **Save**. Your changes will show up right away on your store.

## What customers will see

On your store’s search results, collection pages, or product detail pages, customers can:

- Use your custom filters to narrow down products.
- See related products recommended based on your setup.
- Switch product order using your configured sorting options.

All settings take effect as soon as you save, and you can adjust them anytime.

::: faq

## FAQs

### Why don’t my filters show up?
> Make sure you added the **Filter Widgets** section to your product template and enabled it.

### Why are search or recommendation results wrong?
> Double-check your rules and filter settings in the app dashboard.

:::