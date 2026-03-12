# Fulfill and ship orders

When a buyer places an order, the system follows your **fulfillment settings** (manual or automatic) to decide whether to automatically submit the order to the supplier.
This process ensures that products are fulfilled and shipped smoothly from the supplier, while tracking updates are automatically synced to your store.

## Why it matters

* Supports both manual and automatic fulfillment for flexible operations
* Automatically syncs supplier shipment status and tracking numbers
* Reduces manual work and improves fulfillment efficiency

## Fulfillment modes

Genstore Dropshipping provides two fulfillment options: **manual** and **automatic**.

### Manual fulfillment

In manual mode, you manually confirm each shipment before the system submits the order to the supplier.
This mode is ideal for merchants with smaller order volumes or those who prefer to verify shipping details.

**Steps**

1. After payment, the order appears as **Unfulfilled**.
2. Go to **Store** -> **Orders**, and find the Dropshipping order.
3. Click **Fulfill via Genstore**, then click **Ship order**. The system will send the order to the supplier.
4. The supplier processes the order and provides a tracking number.
5. The system syncs shipping information back to your store, updating the status to **Fulfilled**.

> **Note:** If an order contains products from multiple suppliers, Genstore automatically splits it into separate sub-orders for fulfillment.

::: tip
You can manage shipping fee calculation rules through shipping profiles. Refer to the [shipping profiles documentation](./operate-dropshipping-shipping-profiles.md) to learn how to configure shipping fees for different regions, weights, or delivery methods.
:::

### Automatic fulfillment

In automatic mode, the system submits the order to the supplier right after payment — no manual action required.
This mode is ideal for merchants with higher order volumes or fully automated operations.

**Steps**

1. The buyer completes payment.
2. The system automatically submits the order to the supplier.
3. When the supplier ships, tracking details are automatically synced.
4. The order status updates to **Fulfilled**.

> **Recommendation:**
> For reliable, ongoing supplier relationships, enable **automatic fulfillment** to improve operational efficiency.

## Shipping information sync

* Once the supplier ships, Genstore automatically retrieves the tracking number and carrier info.
* Shipping updates sync in real time to both the merchant admin and the buyer’s order page.
* Buyers can view shipment status directly from their **Order details** page.