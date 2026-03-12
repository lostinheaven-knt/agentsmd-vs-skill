# Manage orders

Orders are purchase requests created and submitted by customers on a merchant's store. They include customer information, purchased products, payment status, shipping details, and more.

In the Genstore admin, you can manage all orders through the **Orders page**. From here, you can view, edit, process, print, and export orders, create draft orders, collect payments, and track abandoned carts. If customers need after-sales service, you can also offer return, refund, and exchange services.

## Search and view orders

Log in to the Genstore admin and click **Store -> Orders** in the left navigation bar to access the **Order list**.
By default, the **Order list** displays all orders, sorted by creation time in descending order (with the most recent orders appearing first). In the order list area, you can:

- Click on the **Order ID** to go to the **Order details** page and view detailed information.
- Click on **Create time** to sort orders by date in ascending or descending order.
- Click on **Product** to view detailed product information (including product image, name, unit price, and quantity).

In the function area above the **Order list**, you can:

- Click **`+`** to customize the order list view to match your business needs.
- Click on the **Search button** to search orders by order number, product name, or customer name.
- Click on **Manage column** to adjust the display content and order of the table header based on your needs.
- Click on **Filter** to sort orders by date, channel, payment status, shipping method, shipment status, product type, tags, and more.
- Click the **Sort** button to arrange orders by **Create time (ascending)** or **Create time (descending)**.

## Edit order details

Click on the **Order ID** to open the **Order details** page, where you can edit the following:

- **Notes**: Click the **Edit button** to add notes. After editing, click **Save** to apply changes.
- **Tags**: Click to add or select existing tags. Click **+** to save the tag, and it will take effect immediately. To delete a tag, click the **x** in the upper-right corner of the tag.
- **Contact info**: Click the **Edit button** to change the contact information. After editing, click **Save** to update the contact details.
- **Shipping address**: Click the **Edit button** to modify the shipping address. After editing, click **Save** to apply the changes.
## Manage orders

In the **Order list**, you can select orders by checking the box next to the order. Here are the options you have for managing orders:

- **Unpaid status**: Select the target order and click **Mark as paid** to manually update the payment status to **Paid**, indicating that the order has been completed and paid for.
- **Authorized status**: Select the target order and click **Capture payment** to transfer the authorized payment amount into your account.
- **Unshipped status**: Select the target order and click **Mark as shipped** to manually update the payment status to **Shipped**, indicating that the order has been shipped. For more details, refer to [Manual shipping](./operate-orders-shipping.md).
### Manage orders in bulk

In the **Order list**, you can select multiple orders by checking the boxes next to them and perform the following bulk actions:

- **Mark as paid**: For multiple orders with an **Unpaid** status. Successfully marked orders will have their payment status updated to **Paid**. Orders that fail will remain unchanged.
- **Mark as shipped**: For multiple orders with an **Unshipped** or **Partially shipped** status. Successfully marked orders will be updated to **Shipped** or **Partially shipped**. Orders that fail will remain unchanged.


## Print orders

You can print orders from either the **Order list** or the **Order details** page:

- **Order list**: Check the box next to the order, select it, and click **Print order**. The print page will pop up, and you can click **Print** to print the order details. On the print preview page, verify the information, and click **Print**.
- **Order details**: Click **More** in the top right corner, then click **Print order**. The print page will pop up, and you can click **Print** to print the order details. In the print preview, confirm the information and click **Print**.

## Modify order shipping information

You can modify shipping information for shipped or partially shipped orders.

::: tip
Shipping information can only be modified once. Please proceed with caution.
:::

1. Log in to Genstore admin and navigate to the **Store -> Orders** page.
2. On the Order list page, locate the order you need to modify and click to open the Order details page.
3. Click the **Edit shipping** button to open the modification window.
4. Identify the shipping details you need to update, and enter the new tracking number and carrier information.
5. Click **Save** to complete the modification.

