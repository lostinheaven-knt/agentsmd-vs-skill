# Month-end inventory snapshot

The **Month-end inventory snapshot report** displays the quantity of each product variant you had in stock at the end of each month.

For this report, **Available** inventory excludes:

- Committed inventory for orders pending fulfillment
- Incoming units that are a part of a transfer

## Report data fields

For standardized terms used in this report, see [Inventory Reports - Common Terms](./expand-genstore-analytics-reports-inventory#common-terms).

The following columns are in the Month-end inventory snapshot report:

| Term | Description |
|--------------|----------------------------------------------------------------------|
| Product title | The title of the product. |
| Product ID | The unique identifier of the product, used to distinguish different products. |
| Variant title | The title of the product variant. |
| Variant SKU | The stock keeping unit identification code for the product variant option. |
| Product vendor | The brand name to which the product inventory belongs. |
| Location name  | The specific location of the warehouse where the product is stored, such as the warehouse name or address. |
| Cost | The cost per item value for the product variant option. |
| Ending quantity | The trackable **Available** inventory quantity of a product variant at the end of the last day of the selected time period (might be a negative number). This excludes **Incoming** and **Committed** inventory.|
| Total inventory value | The cost per item multiplied by the ending quantity amount for each product variant option. The sum of these values displays in the **Summary** row. |

## Negative inventory numbers

A negative value may appear in the **Ending quantity** column of the **Month-end inventory snapshot** report for the following reasons:

- **Inventory tracking is enabled and a variant is oversold**  
	- When inventory tracking is enabled, and the number of orders in a day exceeds the starting inventory, a negative ending quantity may occur.  
	- For example: if the starting inventory is `5` and you receive `8` orders during the day, the ending quantity will be `-3`, indicating that `3` units were oversold.
- **Inventory tracking is not enabled**  
	- When inventory tracking is turned off, the system sets the default quantity to `0`, and each order reduces the available quantity by `1`.  
	- For example: if a new product is added with a default inventory of `0` and you receive `2` orders, the ending quantity will be `-2`.
