# Fulfill via Genstore

Once you have configured your logistics provider, you can begin processing orders and fulfilling shipments through the Genstore platform. Using Genstore Shipping or an authorized Shippo account allows you to complete the entire process from purchasing shipping labels to tracking shipments within a closed loop.

## Step 1: Select orders and purchase shipping labels

After a customer places an order and completes payment, you need to purchase a shipping label for the order.

1. **Access the fulfillment list**: Log in to the admin console and navigate to **Store -> Orders -> Shipping**.
2. **Select orders**: In the **Pending shipment** list, check the box next to the orders you wish to ship.
3. **Click Buy shipping label**: 
    * The system will automatically redirect you to the shipping label purchase interface.
    * **Genstore Shipping users**: The system will display estimated costs, transit times, and services from multiple carriers for easy comparison.
    * **Shippo users**: Click **Get cost** to view shipping details based on your Shippo account.
4. **Confirm and pay**: After verifying that the shipping and receiving information is correct, click **Buy label**.

> **Note**: Switching logistics providers during the label purchase process is prohibited. If you need to make changes, please return to the **Settings -> Shipping and delivery -> Carrier management** page.

## Step 2: Print labels and deliver parcels

After successfully purchasing a label, the order will automatically move to the **In transit** status.

1. **Locate the label**: In the **In transit** or **Shipped** list, find the target order.
2. **Print the label**: Click **Print shipping label** in the **Action** column and securely attach the printed label to the parcel.
3. **Hand over to carrier**: Deliver the parcel to the carrier (e.g., UPS, DHL) according to their specific requirements to complete physical shipment.

## Step 3: Mark as shipped and track logistics

Once the parcel is delivered to the carrier, you must sync the order status and provide tracking information to your customer.

1. **Mark as shipped**: Select the target order in the list and click **More -> Mark as shipped** (or perform this action on the Order Details page).
2. **Trigger notification**: Once marked successfully, the order status will update to **Shipped**, and the system will automatically send a shipping notification email to the customer.
3. **Logistics tracking**: 
    * You can view and copy the tracking number in the **Shipped** list.
    * Customers can use this number to check shipping progress in real-time on the carrier's official website.

## Shipping considerations

* **Phone number required**: To ensure you successfully receive carrier quotes, please fill in the shipping origin phone number accurately.
* **Checkout settings**: It is recommended to go to **Settings -> [Checkout](./settings-checkout.md)** and set the customer shipping phone number to **Required** to ensure complete logistics documentation.
* **Modification restrictions**: Once an order is marked as **Shipped**, the backend does not currently support direct changes to the fulfillment status.