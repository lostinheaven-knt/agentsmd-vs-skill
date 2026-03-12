# Choose logistics carrier

Before you begin shipping, you must select a logistics provider and manage your preferred carriers for different regions.

## Select a logistics provider

Genstore supports two types of logistics fulfillment services, allowing you to choose the best fit for your business needs:

* **Genstore Shipping**: The official logistics service that supports real-time carrier-calculated rates at checkout.
* **Shippo**: A third-party integration. If you have an existing Shippo account, you can use their services within Genstore after authorization.

### How to switch providers

1. Navigate to **Settings -> Shipping and delivery -> Carrier management**.
2. Select the provider you wish to use from the list.
3. **Risk warning**: If you switch from Genstore Shipping to Shippo, and your shipping settings were originally set to **Carrier-calculated rates**, the system will automatically downgrade them to **Manual fallback rates**.

## Manage preferred carriers (Genstore Shipping only)

**Note: This feature is only available when the Genstore Shipping service is active.** It allows you to configure which specific carriers are prioritized for different shipping regions.

### Configuration steps

1. On the **Carrier management** page, click the **Manage preferred carriers** button.
2. The system will display a list of countries by shipping region. Click a specific country (e.g., Germany) to expand the list of available carriers.
3. **Select preferences**: Check the boxes for the carriers you trust or wish to use (e.g., DPD, DHL, UPS).
4. Click **Save** to complete the setup.

### Setup results

* **Checkout display**: Customers will only see and be able to select shipping services from the carriers you have enabled.
* **Label purchasing**: When purchasing shipping labels in the admin, the system will prioritize your selected preferred carriers.

## Shippo account authorization

If you choose to use Shippo, you must complete the account connection process:

1. Navigate to **Settings -> Shipping and delivery -> Carrier management** and select Shippo.
2. Click **Go to authorize** to log in to an existing account or register a new one.
3. Upon successful authorization, you will be redirected back to Genstore with a "Successful Authorization" notification.
4. **Important**: Please ensure your Shippo account has a payment method linked; otherwise, you will be unable to purchase shipping labels.

## Configure shipping rates at checkout

You can set different shipping rate types for countries within each shipping zone to determine the costs shown to customers.

### 1. Carrier-calculated rates
*Exclusive to Genstore Shipping.* At checkout, the system calculates shipping costs based on the customer's address and the order's weight and dimensions.
* **Set fallback rates (Required)**: If you select carrier-calculated rates, you **must** set fallback rates. This ensures that if shipping costs cannot be retrieved from the carrier, customers can still complete their purchase without obstruction.
* **Reference**: For setting up fallback rates, please refer to [Configure shipping profiles](./operate-fulfillment-shipping-profile-configuration.md).

### 2. Manual rates
The system calculates shipping based on pre-defined rules you set. Manual shipping options include:
* **Flat rate**: A single fixed price for the zone.
* **Based on order price**: E.g., free shipping on orders over $50.
* **Based on weight**: Tiered pricing based on total package weight.
* **Based on item count**: Pricing based on the number of items purchased.

### Check shipping bills
To view specific costs incurred from using Genstore Shipping, please navigate to: **Settings** -> **Billing** -> **Past bills**. click to view the billing details, and you can find this information under **Genstore shipping label fee**.

::: faq
## FAQs

### Q1: Why can't I use "Carrier-calculated rates"?
> **A**: This service is currently only available when using **Genstore Shipping**. If you switch to Shippo, please ensure you have configured manual rates.
### Q2: Can I delete my preferred carrier settings?
> **A**: Yes. If you delete a specific shipping region, the corresponding preferred carrier settings for that region will also be removed.
### Q3: Can I temporarily switch logistics providers while purchasing a label?
> **A**: No. Switching logistics providers during the label purchase process is prohibited. To make changes, please go to the **Carrier management** page.

:::