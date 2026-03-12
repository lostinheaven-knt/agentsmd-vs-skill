# Configure shipping profiles

A shipping profile defines how you charge customers for delivery. It is one of the key configurations before launching your store.

- If your store uses the **same shipping rules for all products**, you only need to set up the **General shipping profile**.
- If you need **specific shipping rules for certain products**, create a **Custom shipping profile**.

## Things to consider before configuration

Before configuring your shipping profile, keep the following in mind:

* Be familiar with the zones your store supports for delivery and set up appropriate shipping cost rules accordingly.
* The **General shipping profile** is **automatically created** during initial setup with default zones and rates. Review and adjust it before you launch.
* A product (including product variants) can only be assigned to one shipping profile. If a product is added to a **Custom shipping profile**, it will no longer be available in the **General shipping profile**.
* If multiple products from different shipping profiles are included in the same order, the system will [consolidate the shipping costs](./operate-fulfillment-shipping-profile-shipping-rate#shipping-fee-consolidation), which could result in higher fees at checkout.
* Shipping rate types:
  * Manual rates: Supported by all logistics providers. Rates can be set based on a flat fee, order price, weight, or item count.
  * Carrier-calculated rates: Exclusive to Genstore Shipping. The system retrieves real-time carrier quotes and displays them directly to customers on the checkout page. Note: You must configure fallback rates to ensure customers can still complete their checkout if the carrier interface experiences a temporary outage.

## Differences between general and custom shipping profiles

| Configuration item  | General shipping                      | Custom shipping                           |
| ------------------- | ------------------------------------- | ----------------------------------------- |
| Applicable products | Automatically applies to all products | Must manually select at least one product |
| Priority            | Can be overridden by custom shipping  | Takes priority over general shipping      |

## Edit general shipping profile

Navigation: **Settings** -> **Shipping and delivery**. 

The system automatically creates a default shipping profile that applies to all products. It includes:

- **Fulfillment location**: Default shop location (set during store creation). You can update this anytime under **Settings → Locations**.
- **Shipping zone & rates**: Based on the business area you selected during store setup (e.g., United States – Entire region).
- **Rates**:

| Shipping Method | Profile Name | Description          | Shipping Fee |
| --------------- | ------------ | -------------------- | ------------ |
| By order amount | Economy      | 5 to 8 business days | ≥ 50, Free   |
| Flat rate       | Economy      | 5 to 8 business days | 4.99         |
| Flat rate       | Standard     | 3 to 4 business days | 9.99         |
| Flat rate       | Express      | 1 to 2 business days | 19.99        |

You can edit rates, add new rules, or create additional zones as needed.

## Create custom shipping profile

If you need special shipping rules for certain products, you can create a custom profile and assign products to it:

1. Log in to the **Genstore admin** and go to **Settings → Shipping and delivery**.
2. In the **Shipping** section, click to switch to the **Custom shipping** tab and click **Create now**.  
3. Enter a name for your custom shipping profile.
4. Click **Configure product** to select which products should use this custom shipping rule. Only the products you choose will apply the rates defined in this profile.
5. In the **Not shipping from this location** section, find the shipping location you want to include in this profile and click **Add rate**.
	- Locations listed here come from **Settings → Locations**, not from the product itself.
	- All locations will be listed by default.
	- Once you configure the first rate for a location, it will move to the **Fulfillment and shipping** section.
	- Each location you want to use for fulfillment must have at least one shipping rate.
6. In the popup, configure the following:
	- **Ship to**: Select one or more countries/regions (supports search and bulk selection).
	- **Shipping method**:
	    - **Flat rate**: Charge a fixed amount per order (e.g., $10).
	    - **Rate by price**: Calculate based on the order subtotal.
		- **Rate by weight**: Calculate based on total product weight (defaults to 0 if no weight is set).
	    - **Rate on quantity**: Calculate based on the number of items.
	- **Shipping rates**: Enter the fee. Enter `0` for free shipping.
	- **Rate name**: The label shown at checkout (e.g., “Standard shipping”).
	- **Description (optional)**: Additional info, such as “Delivered within 3–4 business days.” If your store supports multiple languages, you can translate it in the [Translation app](./global-market-language-translate.md).
	- **Checkout preview**: See how the option will appear at checkout.
7. Click **Save** to complete the basic configuration.

::: tip  
Each product can only be linked to **one custom shipping profile** at a time.  
To reassign a product, remove it from its existing profile first.  
:::

## Fulfillment and shipping (location groups)

Once you save the first rate for a location, the **Fulfillment and shipping** section is generated.

In logic, each set of “Shipping location + Shipping zones + Rates” is called a **location group**.

- A shipping profile can contain multiple location groups.
- Each location group is independent in terms of locations, zones, and rates.

**Example**  
If you have three warehouses:

- China warehouse (ships worldwide)
- New York warehouse (ships to US only)
- London warehouse (ships worldwide)

You could configure two groups:

- **Group 1**: China + London → Worldwide
- **Group 2**: New York → United States

::: tip

- If the United States appears in both groups, the system will try to fulfill from multiple groups.
- If you want US orders to be fulfilled only by **Group 2**, remove the US from **Group 1**.  
:::

### Add a fulfillment location

1. In **Fulfillment and shipping -> Fulfillment locations**, click **+ Fulfillment locations**.
2. In the popup, set as follows:
    - All locations created under **Settings → Locations** are listed.
    - Select the locations you want to include in this profile.
    - To add a new location, go to **Settings → Locations** first.
    - You can also set a default location here.
3. Click **Confirm**.

### Add a shipping zone and rates

1. In **Fulfillment and shipping → Shipping zones and rates**, click **+ Zone & rate**.
2. In the popup, configure the same settings as when adding the first rate (zone, calculation method, amount, name, description, preview).
3. Save. The zone will now appear in the list.

::: tip  
Each zone can contain one or more shipping rules.  
:::

### Add a new shipping rate

If you need multiple price tiers for the same zone, click **Add rate** under that zone and configure:

- **Shipping method**: Flat rate / Rate by price / Rate by weight / Rate by quantity.
- **Shipping rates**: Enter the fee (`0` for free shipping).
- **Rate name**: Required. Shown at checkout (e.g., “Standard shipping”).
- **Description (optional)**: Extra details, such as “3–4 business days delivery.”
- **Checkout preview**: Shows how it looks at checkout.

Click **Save**. The new rule will appear under the current zone.

### Edit or delete

- Click the **…** next to a zone or rate to edit or delete.
- Deleting zones or rates affects checkout options. Please operate with caution.

## Unconfigured locations

At the bottom of the page, the system lists **locations without a shipping profile configured**.  
Click **Add rate** for any location to configure it into the current shipping profile.