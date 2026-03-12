# Split, merge, and multi-warehouse shipping

Genstore provides flexible parcel handling features to help you manage complex warehouse and delivery requirements.

## 1. Split shipments
This is applicable when a single order contains multiple products that need to be shipped in separate packages.
* **Operation**: Go to the order details from the **Pending** shipments page and select the specific products and quantities you wish to ship in this batch.
* **Result**: Each split package will have its own independent logistics information and shipping costs, allowing you to set different shipping methods for each.

## 2. Merge shipments
Combine multiple orders from the same customer and address into a single package to save on shipping costs.
* **Operation**: When the system identifies eligible orders, a **Merge order** prompt will appear at the top of the page.
* **Requirements**: The recipient, shipping address, and sales channel must be exactly the same.
* **Reversal**: If a merge is performed by mistake, you can click **... -> Cancel merge order** in the **Pending** shipments list.

## 3. Multi-warehouse shipping (Multi-location fulfillment)
When inventory is distributed across different warehouses, the system uses intelligent routing logic to handle the fulfillment.
* **Automatic splitting**: The system automatically recommends a shipping origin based on where the items are stocked. If an order contains items from different warehouses, it will automatically be split into multiple packages.
* **Manual modification**: You can manually modify the system-recommended shipping warehouse within the fulfillment details if necessary.

::: faq

## FAQs

### Q1. What is the priority between splitting and merging?
> A: Splitting and merging are mutually exclusive operations; you can only perform one of these actions on a single order.

### Q2. How does merging affect shipping costs?
> A: Merged packages will have their total shipping cost recalculated as a single unit. You will need to re-confirm your preferred logistics method.

### Q3. Are there restrictions for dropshipping?
> A: Genstore Dropshipping orders currently do not support split shipments or merging with other orders, as these are fulfilled directly by third-party suppliers.