# View inventory adjustment history

Genstore tracks all inventory changes caused by document updates or manual adjustments, including changes made by modifying inventory quantities directly or by actions like orders, procurement, and stock transfers. This feature allows merchants to track and review inventory adjustments within the past **180 days**, making it critical for maintaining accurate inventory and analyzing stock trends.

## Single-variant products

If a product has only one variant, you can view its inventory adjustment history directly on the product details page.
1. Log in to the Genstore admin, then go to **Store** -> **Products**.
2. In the product list, click the target product, or click **Edit** in the **Action** column to open the product details page.
3. In the **Inventory** section, click **Inventory record** to view the inventory adjustment history.

## Multi-variant products

If a product has multiple variants, inventory adjustment history must be viewed from the details page of the specific variant.

1. Log in to the Genstore admin, then go to **Store** -> **Products**.
2. In the product list, click the target product, or click **Edit** in the **Action** column to open the product details page.
3. In the **Variant details** section, locate the variant you want to review and click to open its details page.
4. On the variant details page, view the inventory records in the **Inventory** section.

All inventory changes for a product variant at a specific location will be recorded by the system and displayed as detailed documents. Different types of documents (e.g., purchase orders, sales orders, stock transfers) will impact various inventory categories (e.g., available inventory, committed inventory, on-hand inventory).

### Inventory adjustment field descriptions

- **Date**: The date of the inventory adjustment document.
- **Activity**: The action that triggered the inventory adjustment, with the user’s name listed.
- **Unavailable**: The adjusted amount of unsellable inventory.
- **Committed**: The number of products in an order that haven't been shipped yet. Note: The inventory used for draft orders isn't counted as committed until the order is finalized.
- **Available**: The adjusted available inventory.
- **On-hand**: On-hand inventory, calculated as `unavailable inventory + committed inventory + available inventory`.
- **Incoming**: The incoming inventory quantity resulting from purchase orders or stock transfers.

## Common inventory adjustment scenarios

### **Scenario 1: Initializing inventory**

**Event**: The product **Clear Moisturizing Cream** (SKU: CTHS-1001) is added with an initial stock of 50 units, and the system records the starting inventory.

| Time                | Operator         | Activity      | Available inventory | Adjusted available inventory | On-hand inventory | Adjusted on-hand inventory |
| ------------------- | ---------------- | ------------- | ------------------- | ---------------------------- | ----------------- | -------------------------- |
| 2025-01-18 10:00 AM | Admin (Jane Doe) | Initial stock | 0                   | 50 (+50)                     | 0                 | 50 (+50)                   |

### **Scenario 2: Purchase order increases stock**

**Event**: The supplier ships products, and the merchant confirms receipt, increasing stock by 30 units.

| Time                | Operator         | Activity                 | Available inventory | Adjusted available inventory | On-hand inventory | Adjusted on-hand inventory |
| ------------------- | ---------------- | ------------------------ | ------------------- | ---------------------------- | ----------------- | -------------------------- |
| 2025-01-18 10:15 AM | Admin (Jane Doe) | Purchase order (order #) | 50                  | 80 (+30)                     | 50                | 80 (+30)                   |

### **Scenario 3: Order reduces inventory**

**Event**: A customer orders 2 units, and inventory is automatically updated.

| Time               | Operator                             | Activity      | Available inventory | Adjusted available inventory | On-hand inventory | Adjusted on-hand inventory |
| ------------------ | ------------------------------------ | ------------- | ------------------- | ---------------------------- | ----------------- | -------------------------- |
| 2025-01-18 3:30 PM | Order fulfillment operator (order #) | Order shipped | 80                  | 78 (-2)                      | 80                | 78 (-2)                    |

### **Scenario 4: Manual inventory adjustment (error correction)**

**Event**: The admin notices an inventory error, correcting the stock from 30 to 28 units.

| Time               | Operator         | Activity                             | Available inventory | Adjusted available inventory | On-hand inventory | Adjusted on-hand inventory |
| ------------------ | ---------------- | ------------------------------------ | ------------------- | ---------------------------- | ----------------- | -------------------------- |
| 2025-01-18 4:00 PM | Admin (Jane Doe) | Manual adjustment (error correction) | 30                  | 28 (-2)                      | 30                | 28 (-2)                    |

### **Scenario 5: Stock transfer to a specific location**

**Event**: The admin creates a stock transfer document, moving 2 units to a specified location, and the adjusted stock is updated accordingly.

| Time               | Operator                | Activity                 | Available inventory | Adjusted available inventory | On-hand inventory | Adjusted on-hand inventory |
| ------------------ | ----------------------- | ------------------------ | ------------------- | ---------------------------- | ----------------- | -------------------------- |
| 2025-01-18 4:30 PM | Stock transfer operator | Stock transfer (order #) | 76                  | 78 (+2)                      | 76                | 78 (+2)                    |
