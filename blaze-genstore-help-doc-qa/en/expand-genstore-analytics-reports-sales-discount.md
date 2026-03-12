# Sales by discount

The **Sales by discount report** groups sales data by discount name (e.g., automatic discount titles or discount types), enabling you to evaluate promotional campaign effectiveness, optimize marketing strategies, and improve profitability.

:::tip

**Note**:

- Reported sales include **full order amounts**, not just the discounted portion.
- Orders using combined discounts may appear under multiple entries, as each discount type is listed separately.

:::

## Use this report to

- Analyze application frequency of different **discount methods or types**.
- Identify discounts with the highest conversion rates.
- Measure revenue impact of specific promotions.

## Report data fields

For standard definitions, refer to [Sales Reports - Common Terms](./expand-genstore-analytics-reports-sales.md#common-terms).

**Additional terms specific to this report**:

| Term                             | Definition                                                                                |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| **Discount title**               | Name entered when creating the discount in the admin.                                     |
| **Discount ID**                  | Unique identifier from the discount's admin URL.                                          |
| **Discount level**               | `Shipping`, `Product`, `Order`, or `Unknown`.                                             |
| **Discount method**              | How discounts are applied: `Automatic` or `Discount Code`.                                |
| **Discount type**                | Examples: Percentage-off, Buy-X-Get-Y, Product markdown, Shipping discount.               |
| **Discount code**                | Customer-facing code to claim discounts.                                                  |
| **Auto discount title**          | Name of automatically applied discounts.                                                  |
| **Discount amount**              | Total value of the reported discount.                                                     |
| **Other discounts**              | Total value of additional discounts applied to the same order.                            |
| **Other non-shipping discounts** | Non-shipping discounts applied alongside this discount.                                   |
| **Other shipping discounts**     | Shipping discounts applied alongside this discount.                                       |
| **Non-shipping discount**        | All non-shipping discounts in orders using this discount.                                 |
| **Shipping discount**            | All shipping discounts in orders using this discount.                                     |
| **Non-shipping script discount** | Product discounts via Script Editor.<br>*Reported only if a discount code is also used.*  |
| **Shipping script discount**     | Shipping discounts via Script Editor.<br>*Reported only if a discount code is also used.* |
| **Orders**                       | Number of orders using this discount.                                                     |
| **Total sales**                  | Total sales of all orders using this discount.                                            |
| **Shipping**                     | Shipping fees excluding shipping discounts.                                               |
