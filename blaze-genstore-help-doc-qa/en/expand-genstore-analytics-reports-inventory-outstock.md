# Out-of-stock alert

The **Inventory alert report** is an extension of the **[Days of inventory remaining](./expand-genstore-analytics-reports-inventory-remaining.md)**. It is designed to help users quickly identify products with low inventory levels, enabling timely restocking or other management actions.

By default, the report is configured to display product SKUs with **inventory days <= 14 days**. However, users can modify the filter criteria to view product details with different remaining inventory days.

## Report features

1. **Default filter criteria**:
   - By default, the report displays product SKUs with **inventory days <= 14 days**. These products are considered to be in an alert state and require close attention.
1. **Custom filter criteria**:
   - Users can adjust the **inventory days** filter criteria according to their needs, such as viewing products with **inventory days <= 7 days** or **inventory days > 30 days**.
1. **Data presentation**:
   - The report presents key information for each product in a tabular format, including **Product title**, **Variant title**, **Variant SKU**, **Ending quantity**, **Days of inventory remaining*, and **Quantity sold per day**.

## Data calculation

- **Days of inventory remaining**: Calculated using the formula `Ending quantity ÷ Quantity sold per day`.
  - If the **Quantity sold per day** is `0`, the remaining inventory days will be displayed as `N/A`.
  - If the ending inventory is negative, the remaining inventory days will be displayed as `0`.
- **Quantity sold per day**: Calculated based on the product's sales over the past `28` days.

---

## Report data fields

For standardized terms used in this report, see [Inventory Reports - Common Terms](./expand-genstore-analytics-reports-inventory#common-terms).

The following columns are in the report:

| Term | Description |
|--------------|----------------------------------------------------------------------|
| Product title | The title of the product. |
| Variant title | The title of the product variant. |
| Variant SKU | The stock keeping unit identification code for the product variant option. |
|Ending quantity | The trackable inventory quantity of a product variant at the end of the last day of the selected time period (might be a negative number).|
|Quantity sold per day | The total quantity of items of a product variant sold in the selected time period, divided by the number of days that the product variant was active during that time period.|
|Days of inventory remaining | The total quantity of items still in inventory, divided by the average quantity of items sold per day, to give an estimate of how many days remain before inventory runs out.|
