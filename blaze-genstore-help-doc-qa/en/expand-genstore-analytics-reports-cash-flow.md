# Finances reports

You can view key finances information for your business in the Finances reports.

## How to access

1. Log in to your Genstore admin.
2. Navigate to **Analytics** -> **Reports** in the left menu.
3. Locate financial reports under the **Finances** section on the Reports Summary page.
4. Click any report title to view comprehensive metrics and granular data.

## Data refresh frequency

Reports are automatically refreshed every **4 - 5 seconds**. You can also manually refresh the page to ensure you are viewing the latest financial data.

## Finances report categories

Click on the report types below to learn more:

- **[Total sales](./expand-genstore-analytics-reports-cash-flow-total.md)**
- **[Taxes](./expand-genstore-analytics-reports-cash-flow-taxes.md)**
- **[Payments](./expand-genstore-analytics-reports-cash-flow-payments.md)**
- **[Shipping](./expand-genstore-analytics-reports-cash-flow-shipping.md)**
- **[Returns](./expand-genstore-analytics-reports-cash-flow-returns.md)**
- **[Discounts](./expand-genstore-analytics-reports-cash-flow-discounts.md)**

## Payment amount vs sales amount

**Payment amount** refers to the total amount of funds received from customers, as displayed in **Finances reports**. This includes actual payments made by customers through various methods (e.g., credit cards, bank transfers). Finances reports reflect cash inflows based on these settled payments.

- **Gross payments** = Gross sales - Discounts + Taxes + Shipping fees
- **Net payments** = Gross payments - Net returns

**Sales amount** represents the total income from all created orders, as shown in the **[Sales report](./expand-genstore-analytics-reports-sales.md)**. It calculates revenue generated from sales activities, including adjustments such as gross sales, discounts, returns, taxes, shipping fees, and other charges. Total sales reflects business performance, not actual cash flow.

- **Total sales** = Gross sales - Discounts - Return amount + Taxes + Shipping fees + Other charges
- **Gross sales** = Product price × Quantity ordered
- **Net sales** = Gross sales - Discounts - Returns

:::tip

Since **Total sales** includes returns, it may display negative values. For example, if returns on a given day exceed sales, **Total sales** for that day will be negative.

:::

### Differences between payment amount and total sales

The discrepancies between **Total sales** and **Payment amount** are primarily due to:

- **Reporting focus**:
  - **Total sales (Sales report)**: Focuses on sales data from all created orders, including gross sales, discounts, returns, etc.
  - **Payments (Finances report)**: Focuses on actual settled payments, reflecting customer **payment status**, regardless of whether orders are fully paid.
- **Time frame differences**:
  - **Total sales** and **Payment amount** may fall into different reporting periods. For example, a customer places an order in May and completes payment, but the funds might settle in June. In this case, the order’s **Total sales** appears in May’s Sales report, while the **Payment amount** is reflected in June’s Finances report.
