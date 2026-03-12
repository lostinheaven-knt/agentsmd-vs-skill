# Inventory status

Genstore provides a comprehensive inventory status management system to help merchants and customers track stock levels in real time, ensuring a smooth shopping experience and preventing overselling. Inventory applies to both **physical and digital products**. Inventory status varies based on product type and business scenario, categorized as follows:

| **Inventory type**        | **Physical products** | **Digital products** |
| ------------------------- | --------------------- | -------------------- |
| **Available inventory**   | ✓                     | ✓                    |
| **On-hand inventory**     | ✓                     | ✗                    |
| **Committed inventory**   | ✓                     | ✓                    |
| **Unavailable inventory** | ✓                     | ✗                    |
| **Incoming inventory**    | ✓                     | ✗                    |

Below are detailed explanations of each inventory type and its business applications.

## Available inventory

**Available inventory** refers to the real-time stock quantity that is ready for customer orders (**excluding committed inventory**). This applies to both **physical and digital products**.

For example, if a merchant has **100 classic white T-shirts** in stock, with **10 reserved** and **5 ordered but not yet shipped**, the **available inventory** is calculated as:

`100 - 10 - 5 = 85`

| **Item**                    | **Quantity (units)** | **Description**                                    |
| --------------------------- | -------------------- | -------------------------------------------------- |
| **Total inventory**         | 100                  | Total number of products in stock                  |
| **Reserved inventory**      | 10                   | Inventory reserved but not yet paid for or shipped |
| **Ordered but not shipped** | 5                    | Items that have been ordered but not yet shipped   |
| **Available inventory**     | **85**               | Inventory ready for purchase                       |

## On-hand inventory

**On-hand inventory** refers to the number of products that have arrived at the warehouse and are ready for immediate shipment. This applies **only to physical products** and offers several key benefits:

- **Warehouse management** – Helps warehouses manage stock levels and restocking decisions.
- **Pre-orders** – If available inventory reaches **zero**, merchants can enable pre-orders if an incoming shipment is scheduled.
- **Returns processing** – Returned products enter on-hand inventory before being restocked for sale.

| **Product name**               | **On-hand inventory** | **Description**                                  |
| ------------------------------ | --------------------- | ------------------------------------------------ |
| **Wireless Bluetooth earbuds** | 100                   | Stock that has arrived and is ready for shipment |

## Committed inventory

**Committed inventory** refers to stock that has been ordered but not yet shipped. It applies to both **physical and digital products**.

For example, if a merchant has **200 remote control cars**, with **50 ordered but not yet shipped** and **30 reserved**, the **committed inventory** is:

`50 + 30 = 80`

| **Item**                    | **Quantity (units)** | **Description**                                              |
| --------------------------- | -------------------- | ------------------------------------------------------------ |
| **Total inventory**         | 200                  | Total number of products in stock                            |
| **Ordered but not shipped** | 50                   | Inventory that has been ordered but not yet shipped          |
| **Reserved inventory**      | 30                   | Pre-reserved inventory that has not yet been paid for or shipped |
| **Committed inventory**     | **80**               | Inventory that is locked and temporarily unavailable for sale |
| **Available inventory**     | **120**              | Stock available for customer orders                          |

> Once the order is shipped, the system updates the committed inventory accordingly.

## Unavailable inventory

**Unavailable inventory** refers to stock that cannot be sold, usually because it has been set aside for special cases. This applies **only to physical products** and ensures that the normal sales inventory remains unaffected.

For example, if a merchant has **500 products**, with **20 reserved for customers**, **10 held in draft orders**, and **15 damaged or expired**, the **unavailable inventory** is:

`20 + 10 + 15 = 45`

| **Item**                        | **Quantity (units)** | **Description**                               |
| ------------------------------- | -------------------- | --------------------------------------------- |
| **Total inventory**             | 500                  | Total number of products in stock             |
| **Customer-reserved inventory** | 20                   | Inventory reserved for specific customers     |
| **Draft order inventory**       | 10                   | Stock held in draft orders, not yet finalized |
| **Damaged/expired inventory**   | 15                   | Inventory that cannot be sold                 |
| **Unavailable inventory**       | **45**               | Temporarily unsellable inventory              |
| **Available inventory**         | **455**              | Stock available for customer orders           |

## Incoming inventory

**Incoming inventory** refers to stock that has not yet been received, as it is still in transit or processing. This applies **only to physical products** and is used for managing purchase orders and inventory transfers.

For example, if a merchant has **50 running shoes in stock** and an additional **100 in transit**, the **total estimated inventory** is:

`50 + 100 = 150`

| **Item**                      | **Quantity (units)** | **Description**                         |
| ----------------------------- | -------------------- | --------------------------------------- |
| **Current inventory**         | 50                   | Stock currently available               |
| **Incoming inventory**        | 100                  | Inventory in transit or being processed |
| **Estimated total inventory** | **150**              | Current stock + incoming stock          |
