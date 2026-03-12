# Inventory reports  

**Inventory reports** display a month-end snapshot of your inventory, and help you track the quantity and percentage of inventory sold per day.

:::tip
**Handling deleted products or variants**
- If you delete a product or variant from your inventory, then the analytics data related to that product or variant is preserved for reporting services. This ensures that you can still access historical data even after deletion.
:::

## How to access

1. Log in to your Genstore admin.
2. Navigate to **Analytics** -> **Reports** in the left menu.
3. Locate financial reports under the **Inventory** section on the reports summary page.
4. Click any report title to view comprehensive metrics and granular data.

## Data refresh frequency

It can take **12-72 hours** before inventory changes display in reports.

## Report categories

Common report types include:
- [Out-of-stock alert](./expand-genstore-analytics-reports-inventory-outstock.md)
- [Month-end inventory snapshot](./expand-genstore-analytics-reports-inventory-snapshot.md)
- [Average inventory sold per day](./expand-genstore-analytics-reports-inventory-daily.md)
- [Days of inventory remaining](./expand-genstore-analytics-reports-inventory-remaining.md)
- [Slow-moving Inventory](./expand-genstore-analytics-reports-inventory-slow.md)

## Common terms  

| Term | Description |
|------|-------------|
| Product ID | The unique identifier of the product, used to distinguish different products. |
| Product title | The title of the product. |
| Variant SKU | The stock keeping unit identification code for the product variant option. |
| Variant title | The title of the product variant. |
| Location name | The specific location of the warehouse where the product is stored, such as the warehouse name or address. |
| Product vendor | The brand name to which the product inventory belongs. |
| Cost | The cost per item value for the product variant option. |
| Starting quantity | Quantity of a product variant at the beginning of the first day of the selected time period (might be a negative number), or the variant's starting quantity for variants that were added within the selected time period. |
| Ending quantity | The trackable inventory quantity of a product variant at the end of the last day of the selected time period (might be a negative number). |
| Quantity sold | Number of units of a product variant sold during the selected period (doesn't reflect inventory adjustments such as returns, manual adjustments, or transfer receipts). |
| Quantity sold per day | Average number of items of the product variant sold per day during the selected period (quantity sold divided by number of days in the time period). |
| Percent sold | Percentage of the product variant sold during the selected period, out of the total starting quantity (values greater than 100%, lower than 0%, or N/A are possible). |
| Days of inventory remaining | The total quantity of items still in inventory, divided by the average quantity of items sold per day, to give an estimate of how many days remain before inventory runs out. |
| Inventory value | The total value of the product inventory based on the merchant cost. Any product whose ending inventory quantity value is less than 0 is considered to have a total value (cost) of 0. |
| Retail value | The total value of the product inventory based on the sale price, excluding discounts. Any product whose ending inventory quantity value is less than 0 is considered to have a total value (price) of 0. |
