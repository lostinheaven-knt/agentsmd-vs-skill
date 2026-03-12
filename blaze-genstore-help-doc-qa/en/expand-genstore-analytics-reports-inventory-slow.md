# Slow-moving inventory

The **Slow-moving inventory report** is an extended report based on the **[Average inventory sold per day report](./expand-genstore-analytics-reports-inventory-daily.md)**, aiming to help users quickly identify products whose Percent sold is lower than the set threshold, so as to adjust sales strategies in a timely manner or clear the inventory.

By default, this report is configured to filter the details of product SKUs with a **Percent sold < 30%**. However, users can modify the filtering criteria according to their needs and view the details of products with different percentages of units sold.

## Report features

1. Default filtering criteria
	- By default, the report will display the details of product SKUs with a **Percent sold < 30%**. These products are considered to be in a slow - moving state and require special attention.
2. Customizable filtering criteria
	- Users can modify the filtering criteria for the **Percent sold** according to their actual needs. For example, they can view the details of products with a **Percent sold < 20%** or a **Percent sold > 50%**.
3. Data presentation
	- The report presents the key information of each product in tabular form, including **Product title**, **Variant title**, **Variant SKU**, **Starting quantity**, **Quantity sold**, and **Percent sold**.

## Report data fields

For standardized terms used in this report, see [Inventory Reports - Common Terms](./expand-genstore-analytics-reports-inventory#common-terms).

The following columns are in the report:

| Term | Description |
|--------------|----------------------------------------------------------------------|
| Product title | The title of the product. |
| Variant title | The title of the product variant. |
| Variant SKU | The stock keeping unit identification code for the product variant option. |
| Starting quantity | Quantity of a product variant at the beginning of the first day of the selected time period (might be a negative number), or the variant's Starting quantity for variants that were added within the selected time period.|
| Quantity sold | Number of units of a product variant sold during the selected period (doesn't reflect inventory adjustments such as returns, manual adjustments, or transfer receipts). |
| Percent sold |Percentage of the product variant sold during the selected period, out of the total starting quantity (values greater than 100%, lower than 0%, or N/A are possible).|

## Data calculation

**Formula**:

``` 
Percent sold = Quantity sold ÷ Starting quantity
```

This metric represents the percentage of the starting inventory that was sold during the selected time period.

### Special cases

The **Percent sold** value may be less than 0% or greater than 100% due to the following reasons:

- **Inventory tracking is enabled and a variant is oversold**  
	- For example, if the starting inventory is `5` and you receive `10` orders during the day, the **Percent sold** will be `200%`.
- **The starting quantity is negative**  
	- For example, if overselling on the previous day results in a starting inventory of `-5`, and you receive `2` more orders that day, the **Percent sold** will be `-40%`.
- **The starting quantity is 0 (value shown as N/A)**  
	- When the starting quantity is `0`, the system cannot calculate a valid percentage, and the value will be shown as **N/A**.
