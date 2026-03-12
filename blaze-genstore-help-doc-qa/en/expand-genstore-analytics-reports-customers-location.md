# Customers by location

The **Customers by location Report** displays data on new customers organized by geographical location. The system categorizes new customers based on the **default address** associated with their accounts in your Genstore admin.

For each geographical region, the report includes the following metrics:
- Number of new customers who placed their first order within the selected time frame.
- Total number of orders placed by these customers since their first purchase.
- Total amount spent by these customers, including average order value and Amount spent per customer.

:::tip
The order and spending data are based on the **entire order history of new customers** in the report, not just orders placed within the selected time frame.
:::

## Use this report to

This report helps you understand where your purchasing customers are located and how they behave across different regions—empowering you to fine-tune your marketing strategies and customer engagement efforts.

- **Identify top-performing regions**  
	Use the **Top 20 region analysis** to see which countries, states, or cities your customers are coming from. Compare order volume and revenue by location to evaluate your market reach and growth opportunities.
- **Evaluate customer value and repurchase potential**  
	In the **detailed regional breakdown**, review key metrics like order count, total spend, average order value, and revenue per customer. This helps you assess customer buying power and loyalty by region.
- **Support personalized marketing and remarketing**  
	Use customizable fields—such as first order date, marketing opt-in status, or whether a customer is a repeat buyer—to filter and segment customers. Then tailor email or SMS campaigns to drive repeat purchases.
- **Segment new customers by acquisition time**  
	The date filter is based on the customer’s **first order date**, making it easy to analyze newly acquired customers from specific time periods and assess the effectiveness of your acquisition efforts.

::: tip

The date filter is linked to the customer's **first order date**.

:::

## Report data fields

The following columns are in the report:

| Term                     | Definition                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Customer ID              | Unique identifier for each customer.                                      |
| Time (Hour, Day, Week, Month, Quarter, Year, Hour of day, Day of week, Month of year) | The precise timestamp when a customer places an order, adds or updates a line item, or modifies a shipping charge. |
| Customer name            | Name of the customer.                                                      |
| Customer email           | Email address of the customer.                                            |
| Customers                | Each customer ID defaults to 1.                                           |
| First order date         | First payment order date.                                                 |
| Last order date          | Latest payment order date.                                                |
| Accepts email marketing  | Whether the customer's marketing subscription accepts email marketing.     |
| Accepts SMS marketing    | Whether the customer's marketing subscription accepts SMS marketing.       |
| Is returning             | Customers with orders greater than 2 are considered repeat customers.      |
| City                     | The city of the customer's default address.                               |
| Region                   | The region of the customer's default address.                             |
| Country/Region           | The country/region of the customer's default address.                     |
| Amount spent             | Total amount spent by these customers, excluding discounts, including taxes, shipping fees, and all refunds. |
| Orders                   | Total number of orders placed by these customers since their first order and payment. |
| Amount spent per order   | Average amount spent per order.                                           |
| Amount spent per customer| Average amount spent per customer.                                        |
