# Manage shipped orders

On the **Shipped** page in Genstore, you can view all orders that have been successfully shipped. This page provides detailed order information and shipping status updates, helping you track shipments and manage post-shipping operations. This guide will walk you through the features of the **Shipped** page.

## Page overview

The **Shipped** page displays a list of all completed shipments. Each order includes the following details:

- **Order ID** – A unique identifier for each order.
- **Order time** – The date and time the customer placed the order.
- **Product information** – The names and quantities of the items in the order.
- **Customer name** – The name of the customer who placed the order.
- **Order channel** – The platform or channel where the order was placed.
- **Package information** – The package’s weight, dimensions, and other relevant shipping details.
- **Ship from** – The merchant’s shipping address.
- **Ship to** – The customer’s delivery address.
- **Shipping** – The selected carrier and shipping method.
- **Actions** – Action buttons that allow you to manage shipment-related tasks.

## Order list

On the **Shipped** page, you can click an **Order ID** to open the **Order details** page and access more detailed information about that order.

### View product details

Click **Product details** to see a breakdown of the order’s items, including product names, quantities, and unit prices.

### View tracking information

Click **Shipping** to access the order’s tracking number, shipping carrier, recipient address, package details, and tracking history.

The package details include:

- **Shipping information** – Such as the shipping date and shipping method.
- **Product details** – The list of products included in the shipment.

The **Tracking history** allows you to monitor the real-time status of the package.

> Possible tracking statuses:
> - **Awaiting pickup** – The package is ready but has not yet been collected by the carrier.
> - **In transit** – The package is on its way to the customer.
> - **Delivered** – The package has been successfully received by the customer.
> - **Issue detected** – The shipment has encountered a problem (e.g., delay or lost package) and requires attention.

## Action buttons

### Print label

If the order was fulfilled using **Genstore’s integrated shipping service** (by purchasing a shipping label through an authorized carrier), you can click **Print shipping label** to print the shipping label and attach it to the package. The **Print shipping label** button is only available for orders shipped via Genstore’s logistics service.

### Print packing list

If the order was shipped using **Genstore’s integrated shipping service**, you can click **Print packing list** to generate a packing slip. This helps warehouse staff verify the contents of the package before shipping. The **Print packing list ** button is only available for orders fulfilled through Genstore’s shipping service.

### Print pick list

Regardless of whether you are using **self-fulfillment** or **Genstore’s integrated shipping**, you can click **Print pick list** to generate a pick list. This helps warehouse staff efficiently pick the correct items for the order.

## Shipping methods

- **Self-fulfillment** – You manage the shipping process manually and need to upload tracking numbers yourself.
- **Genstore’s integrated shipping** – The platform provides a shipping service through an authorized carrier. You must purchase a shipping label, and a tracking number will be generated automatically.

::: faq

## FAQs

### Q1. Why don’t I see the print shipping label button?
> A: If your order was shipped using **self-fulfillment**, the **Print shipping label** option will not be available. You will need to manually enter and upload tracking information. If your order is still in the process of purchasing a shipping label but the shipping status has already been updated, you may need to wait until the label purchase is completed before the **Print shipping label** button becomes available.

### Q2. Can I edit shipping details after an order has been shipped?
> A: No, shipping details cannot be modified after an order has been marked as shipped. Be sure to verify all information before finalizing the shipment.

### Q3. How do I track a package’s shipping status?
> A: On the **Shipped** page, click **Tracking information** to view the order’s tracking number, carrier details, and real-time shipment status.

### Q4. Does the shipment tracking support multiple languages?
> A: Yes, but the view differs between the Customer and the merchant:
>   - **Customer**: The system automatically displays tracking updates in the language used at checkout. For example, if a customer places an order in Spanish, they will see the tracking details in Spanish. **Note: If the customer’s language is not one of the following—Simplified Chinese, Traditional Chinese, English, Spanish, French, German, Japanese, Portuguese, or Russian—the tracking information will be shown in English by default.**
>   - **Merchant**: The merchant dashboard displays the original tracking data provided by the carrier (usually in English or the origin language) to ensure accuracy.


:::