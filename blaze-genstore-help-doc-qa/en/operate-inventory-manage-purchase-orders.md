# Use purchase orders for restocking

Merchants can directly create purchase orders in Genstore admin, record the stock needed, and its quantities, without relying on external tools. Clear purchase records not only facilitate communication with vendors but also reduce human errors in the purchasing process, improving inventory management efficiency.

## Create a purchase order

1. Log in to your **Genstore admin**, then click **Store** -> **Products** -> **Purchase orders**.
2. Click **Create purchase order**.
3. Click **Select vendor**. If you don't have vendor information, you must first create a vendor. For details, refer to [Add vendor](#manage-vendors).
4. The **Destination** for the purchase can only be an active location.
5. [Optional] Choose payment terms, such as Cash on delivery, Payment upon receipt of invoice, Early payout, or Full payment within N days.
6. Select the vendor's currency.
7. Fill in the delivery-related information, including **Estimated arrival date**, **Tracking number** (optional), and **Shipping carrier** (the system may auto-select this based on the tracking number, but you can adjust it manually).
8. Add products, up to 200 products. Click the **Select purchase products** button, select the products to be purchased from the popup. The selected products will automatically appear in the purchase order product list, where you can adjust **Purchase quantity**, **Vendor SKU** (optional), **Cost per item** (optional), and **Tax rate** (optional).
9. You can add notes to the purchase order for easier future management.
10. Click **Save as draft** to save the purchase order as a draft. When you are ready to place the order with the vendor, click **Order** in the top right corner of the purchase order page to mark the purchase process as started.

### Adjust costs

In the **Cost summary** section of the purchase order, the current purchase quantity and tax information will be displayed. You can click **Add cost items** to adjust the cost management:

- From the **Cost item** dropdown, choose the item to adjust, and enter the amount for that adjustment.
- Click **Add** to add more adjustment items.
- To remove an adjustment item, click **Delete** next to the item.

## Edit a purchase order

Only purchase orders in draft status can be modified, to modify the details of an existing purchase order, go to the purchase order details page, choose the purchase order is in **Draft** status, adjust it directly on the page.

## Receive inventory

When products sent by the vendor arrive, merchants can record the actual received inventory quantity in Genstore admin. **The received inventory will automatically be added to available stock while reducing the incoming stock.**

### Inventory update logic

- If the purchase order is **not received**, incoming stock increases, but on-hand and available stock remain unchanged.
- Once the purchase order **receives inventory**, both on-hand and available stock increase, and incoming stock decreases.
- If the purchase order **rejects inventory**, there is no change in stock quantities.

| Status                 | On-hand stock | Available stock | Incoming stock |
| ---------------------- | ------------- | --------------- | -------------- |
| Draft                  | No change     | No change       | No change      |
| Ordered (Not Received) | No change     | No change       | **Increase**   |
| Ordered (Received)     | **Increase**  | **Increase**    | **Decrease**   |
| Ordered (Rejected)     | No change     | No change       | No change      |

### Related amount calculation explanation

When receiving products from a purchase order, the system calculates and tracks the **received quantity**:

- **Incoming product quantity** changes based on the **actual received quantity**, regardless of whether the product is marked as received or rejected.
- The final amount of the purchase order is calculated based on **unit cost** and **tax rate**.

## Delete a purchase order

A purchase order can only be deleted when it is in **Draft** status. If the order has been marked as **Ordered**, it must first be **Closed** before deletion.

**Steps to delete**

1. Log in to your **Genstore admin**, then click **Store** -> **Products** -> **Purchase orders**.
2. Select the purchase order in **Draft** status and go to the order page.
3. Click **Delete**.

## Close a purchase order

- **Draft** purchase orders cannot be closed, they can only be deleted.
- **Ordered but not received** or **Partially/Receiving completed** (including rejected inventory) orders can be closed.
- **Closing a purchase order will not affect the stock quantity.**

**Steps to close**

1. Log in to your **Genstore admin**, then click **Store** -> **Products** -> **Purchase orders**.
2. Select the target purchase order.
3. Click **Close purchase order**.

## Manage vendors

Merchants can manage vendor information, including adding, editing, and deleting vendors.

### How to access

1. Log in to your **Genstore admin**, then click **Store** -> **Products** -> **Purchase orders**.
2. Click **Create purchase order**.
3. Click **Select vendor**.

### Add a vendor

1. In the **Select vendor** window, click **Add vendor**.
2. Enter the vendor name. Other information, such as country, address, city, detailed address, ZIP code, contact name, email, etc., are optional.
3. Click **Confirm** to complete the creation.

### Edit a vendor

1. In the **Select vendor** window, click **Edit** next to the vendor you want to modify.
2. Update the vendor information in the vendor details page.
3. Click **Save** to complete the update.

### Delete a vendor

1. In the **Select vendor** window, click **Delete** next to the vendor you want to remove.
2. A confirmation window will pop up. Click **Confirm** to proceed with deletion.
3. After deleting a vendor, any purchase orders associated with that vendor must have the vendor selected again.
