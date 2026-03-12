# Genstore logistics service

Genstore logistics service is a comprehensive fulfillment solution that allows you to manage the entire shipping lifecycle—from real-time rate calculation at checkout to label purchasing and tracking—directly within your Genstore admin.

## Key benefits

* **Seamless fulfillment**: Handle every step of the process, including purchasing labels, printing packing slips, and marking orders as shipped, in one integrated dashboard.
* **Smart rate comparison**: Automatically compare real-time rates and transit times across major carriers like UPS and USPS based on your specific origin and destination.
* **Automated shipping rates**: Provide customers with the most cost-effective shipping options at checkout using carrier-calculated rates.
* **Fallback rate protection**: Built-in fallback rates ensure your checkout remains functional even if a carrier's real-time API experiences a temporary outage.

## Logistics service comparison

Genstore supports two primary logistics models. You can toggle between these at **Settings -> Shipping and delivery -> Carrier management**.

| Feature | Genstore Shipping (Official) | Shippo (Authorized) |
| :--- | :--- | :--- |
| **Onboarding** | No additional registration required; ready to use immediately. | Requires an existing Shippo account and platform authorization. |
| **Account fees** | Available to subscribed stores in good standing; no external account needed. | Requires a valid payment method to be linked within your Shippo account. |
| **Real-time quotes** | Displays live carrier rates to customers during the checkout process. | Requires manual rate retrieval within the admin for label purchasing. |
| **Switching logic** | Becomes the default active service once selected. | Switching to Shippo will automatically downgrade checkout rates to manual fallback rates. |

## Core fulfillment workflow

1. **Select your logistics provider**: Choose Genstore Shipping or authorize your Shippo account under the logistics provider management section.
2. **Configure shipping rates**: Set up manual or carrier-calculated rates in your shipping profiles. 
   > **Note**: Always configure fallback rates to ensure customers can complete orders if real-time carrier data is unavailable.
3. **Purchase shipping labels**: Once an order is paid, navigate to **Store -> Orders -> Shipping** and click **Buy shipping label** in the pending shipments list.
4. **Print and ship**: Generate your shipping label, attach it to the parcel, and drop it off at the selected carrier's location.
5. **Mark as shipped**: Manually update the status to **Shipped** to automatically sync the tracking number and notify your customer.

## Important considerations

* **Required information**: Accurate carrier quotes require a valid origin phone number; we recommend setting the customer phone number as "Required" at [checkout](./settings-checkout.md).
* **Account restrictions**: Label purchases via Genstore Shipping are currently not supported for development stores.
* **Status adjustments**: Once an order is marked as "Shipped," the fulfillment status cannot be directly modified within the admin panel.