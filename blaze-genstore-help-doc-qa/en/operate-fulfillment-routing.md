# Order routing

Order routing rules determine the shipping location for the products in each customer order. You can add, edit, delete, and rearrange these rules to prioritize shipping locations. Additionally, you can configure routing options based on common preferences, such as always shipping from the closest location to the delivery address or prioritizing the nearest warehouse.

::: tip  
You only need to configure routing rules if **multiple fulfillment locations** are set up. If your store has only one fulfillment location, routing rules are not required.  
:::

## Add order routing rules

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. In the **Order routing** section, click to view the configured rules.
3. Select the rule you want to add.
4. If you want to add multiple rules, repeat steps 2 and 3. The rules will run in order of priority from top to bottom. You can drag the **Drag** icon next to each rule to adjust its priority.
5. Click **Save**.

## Manage order routing rules

### Edit shipping location priority

When multiple shipping locations are configured, you can choose to prioritize the shipping locations by distance or to manually configure the priority.

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. In the **Order routing** section, you can see how many rules are configured. Click to open the settings page.
3. Click **Configure rule** and add **Shipping location priority**. Then choose either **Prioritize by distance** or **Set priority manually**:
   - If you select **Set priority manually**, click the **Edit** icon to arrange the shipping location priority.
   - If there is only one fulfillment address, go to **Settings → Locations** to add another address before adjusting the priority.
4. Click **Save** to apply your changes.

### Delete order routing rules

1. In the **Genstore** admin, go to **Settings** -> **Shipping and delivery**.
2. In the **Order routing** section, click to enter the setting page.
3. Click the **Trash** icon next to the rule you want to delete.
4. Click **Save**.

## Common order routing configurations

Here are some recommended order routing configurations that you can set based on your needs:

1. **Try to avoid splitting shipment**
   - All items in the same order should ship from the same location to avoid splitting the order. Order splitting should only be considered when products cannot be delivered from a single shipping location.
2. **Shipping location priority**
   - The shipping location should be selected based on distance or manually set priority order. We recommend organizing priorities to ensure smooth fulfillment and timely logistics.
3. **The same-market principle**
   - Prioritize fulfillment locations in the same market as the delivery address to reduce cross-market shipping costs and improve delivery efficiency.
4. **Principle of adequate inventory**
   - Prioritize locations with sufficient stock. If a location cannot fulfill the order, select another location with enough inventory to ensure timely order delivery.

::: faq
## FAQs

### Q1. Which fulfillment location is used by default for draft orders?

> A: Draft orders automatically use the default fulfillment location set in your [Locations](./operate-fulfillment-location.md) settings. To update your default location, go to **Settings** -> **Locations** in your Genstore admin.

:::