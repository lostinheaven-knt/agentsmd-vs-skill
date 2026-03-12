# Days of inventory remaining

The purpose of this report is to give an overall sense of how long your tracked inventory is estimated to last, based on your **average sales rates** for each variant, and the **amount of inventory** you have left.

The report includes two main components:
- **Chart view**:  Visually displays the distribution of product variants across different inventory durations, such as those expected to run out soon (**0 days**), those with **0–30 days** of inventory remaining, and those with **91+ days**.
- **Detailed table**:  Lists the days of inventory remaining for each SKU. The calculation formula is:
	- `Ending quantity (Total quantity of items still in inventory) ÷ Quantity sold per day`
	- A product variant's average quantity of items sold per day is calculated based on its sales over **the last 28 days.**

**Special cases**

- If a SKU had **no sales** during the selected time period (average quantity of items sold per day = 0), the **Days of inventory remaining** will show as **N/A**, indicating insufficient data to make a prediction.
- If a SKU’s **ending inventory is negative**, the **Days of inventory remaining** will be shown as **0**.

## Report data fields

For standardized terms used in this report, see [Inventory Reports - Common Terms](./expand-genstore-analytics-reports-inventory#common-terms).

The following columns are in the Days of inventory remaining report:

| Term | Description |
|--------------|----------------------------------------------------------------------|
| Product title | The title of the product. |
| Variant title | The title of the product variant. |
| Variant SKU | The stock keeping unit identification code for the product variant option. |
| Ending quantity | The trackable inventory quantity of a product variant at the end of the last day of the selected time period (might be a negative number).|
| Quantity sold per day | The total quantity of items of a product variant sold in the selected time period, divided by the number of days that the product variant was active during that time period.|
|Days of inventory remaining|The total quantity of items still in inventory, divided by the average quantity of items sold per day, to give an estimate of how many days remain before inventory runs out.|
|Inventory value|The total value of the product inventory based on the **merchant cost**. Any product whose ending inventory quantity value is less than 0 is considered to have a total value (cost) of 0 USD.|
|Retail value  |The total value of the product inventory based on the **sale price**, excluding discounts. Any product whose ending inventory quantity value is less than 0 is considered to have a total value (price) of 0 USD.|
