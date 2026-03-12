# Average inventory sold per day

The **Average inventory sold per day  report** displays the average number of items of inventory sold per day by product variant.

## Report data fields

For standardized terms used in this report, see [Inventory Reports - Common Terms](./expand-genstore-analytics-reports-inventory#common-terms).

The following columns are in the report:

| Term | Description |
|--------------|----------------------------------------------------------------------|
| Product title | The title of the product. |
| Variant title | The title of the product variant. |
| Variant SKU | The stock keeping unit identification code for the product variant option. |
| Starting quantity | Quantity of a product variant at the beginning of the first day of the selected time period (might be a negative number), or the variant's **Starting quantity** for variants that were added within the selected time period.|
| Ending quantity | The trackable inventory quantity of a product variant at the end of the last day of the selected time period (might be a negative number).|
| Quantity sold | Number of units of a product variant sold during the selected period (doesn't reflect inventory adjustments such as returns, manual adjustments, or transfer receipts). |
|Quantity sold per day | Average number of items of the product variant sold per day during the selected period (quantity sold divided by number of days in the time period).|
|Percent sold | Percentage of the product variant sold during the selected period, out of the total starting quantity (values greater than 100%, lower than 0%, or N/A are possible).|

## Data calculation

**Formula**:

``` 
Percent sold = Quantity sold ÷ Starting quantity
```

This metric reflects the proportion of the starting inventory that was sold during the selected time period.

### Special cases

The **Percent sold** value might be below 0% or above 100% in the following scenarios:

- **Inventory tracking is enabled and a variant is oversold**  
	- For example, if the starting inventory is `5` and you receive `10` orders in a day, the **Percent sold** is `200%`.
- **The starting quantity is negative**  
	- For example, if overselling on the previous day causes the starting quantity to be `-5` the next day, and you sell `2` more units, the **Percent sold** for that day is `-40%`.
- **The starting quantity is 0 (shown as N/A)**  
	When the starting quantity is `0`, the system cannot calculate a valid percentage, and the value will be displayed as **N/A**.
