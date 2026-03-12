# Sales reports

Genstore Analytics provides robust sales reporting capabilities, empowering you to analyze sales data in depth, understand customer purchasing patterns, and identify sales trends.

Through multidimensional breakdowns by product, billing location, sales channel, and more, you gain actionable insights to drive business strategies and enhance sales forecasting accuracy.

## Data update frequency

Sales reports display real-time data updated every **4-5 seconds**, except for the **[Sales by discount report](./expand-genstore-analytics-reports-sales-discount.md)**, which updates once every 24 hours. Refresh your page at any time to access the latest information.

## How to access

1. Log in to your Genstore admin.
2. Navigate to **Analytics** -> **Reports** in the left menu.
3. Locate financial reports under the **Sales** section on the Reports Summary page.
4. Click any report title to view comprehensive metrics and granular data.

## Sales report categories

Analyze sales performance through specialized report types.

Click a report type below to learn more about it.
- **[Average order value over time](./expand-genstore-analytics-reports-sales-time-average.md)**
- **[Sales by traffic referrer](./expand-genstore-analytics-reports-sales-referrer.md)**
- **[Sales over time](./expand-genstore-analytics-reports-sales-time.md)**
- **[Sales by product](./expand-genstore-analytics-reports-sales-product.md)**
- **[Sales by channel](./expand-genstore-analytics-reports-sales-channel.md)**
- **[Sales by product variant SKU](./expand-genstore-analytics-reports-sales-product-sku.md)**
- **[Sales by billing location](./expand-genstore-analytics-reports-sales-location.md)**
- **[Sales by shipping method](./expand-genstore-analytics-reports-sales-shipping.md)**
- **[Sales by discount](./expand-genstore-analytics-reports-sales-discount.md)**

## Common terms

| Metric | Definition |
|--------|------------|
| **Orders** | Total orders placed within the selected date range. |
| **Return quantity** | Number of products returned. |
| **Net quantity** | `Sold Quantity - Returned Quantity`. |
| **Units per transaction** | `Net Quantity / Order Count`. |
| **Gross sales** | Pre-tax value calculated as `Product Price × Quantity` (excluding shipping, discounts, returns). Includes pending/canceled orders. |
| **Net sales** | `Gross Sales - Discounts - Return Amounts`. |
| **Gross profit** | Total profit calculated as `Net Sales - Product Cost`. |
| **Cost** | Aggregate cost of products sold during the period. |
| **Discounts** | 1. Sum of product-level and order-level discounts.<br>2. Reductions applied before taxes, proportionally allocated across order items.<br>3. Includes promotional offers and coupon redemptions. |
| **Returns** | Monetary value of returned products (displayed as negative values on return dates). |
| **Shipping** | `Shipping Charges - Shipping Discounts - Refunded Shipping`. |
| **Taxes** | Total tax amount applied to orders. |
| **Total sales** | `Gross Sales - Discounts - Returns + Taxes + Shipping`. Positive on order dates, negative on return dates. |

## Metrics library

### Dimensions

#### Core information

| Field | Definition |
|-------|------------|
| Time | Exact date/time of order placement or modification. |
| Sales type | Indicates order (sale) or return (refund). |
| Line item type | Classifies items as *Product* or *Shipping*. |
| Product name | Name of purchased/returned product. |
| Product category | Product's assigned category at transaction time. |
| Product variant SKU | The identification code of the product variant. |
| Product variant title | Specific product variant description. |

#### Order details

| Field | Definition |
|-------|------------|
| Order ID | Unique order identifier. |
| Product ID | Unique product identifier. |
| Variant ID | Unique product variant SKU identifier. |
| Price | Pre-discount price per unit. |
| Sales channel | Platform/channel where transaction occurred. |

#### Market & customer data

| Field | Definition |
|-------|------------|
| Market name | Transaction marketplace name. |
| Is canceled | *Yes*: Order canceled; *No*: Active order. |
| Payment status | Current payment state: Pending/Partially Paid/Authorized/Paid. |
| Fulfillment status | Shipping progression: Fulfillable/Partially Shipped/Shipped/Delivered. |

#### Customer & shipping

| Field | Definition |
|-------|------------|
| Billing city | City in billing address |
| Billing region | State/province in billing address |
| Billing country | Billing address country |
| Billing ZIP | Billing ZIP code |
| Customer email | Purchaser's email address |
| Customer name | Purchaser's full name |
| Shipping method | Selected delivery service |
| Shipping city | Destination city |
| Shipping state | Destination state/province |
| Shipping country | Destination country |
| Shipping ZIP | Destination ZIP code |

#### Marketing attribution

| Field | Definition |
|-------|------------|
| UTM campaign content | Content variation identifier in marketing campaigns |
| UTM campaign medium | Traffic medium (e.g., email, social) |
| UTM campaign name | Specific marketing campaign name |
| UTM campaign source | Traffic source (e.g., google, facebook) |
| UTM campaign term | Paid search keywords |

#### Traffic Sources

| Field | Definition |
|-------|------------|
| Traffic referrer host | Domain directing traffic (e.g., google.com) |
| Traffic referrer name | Source name (e.g., Google Search) |
| Traffic referrer path | URL path on referring site |
| Traffic referrer source | Channel categorization: Direct/Search/Email/Social/Unknown |
| Traffic referrer URL | Full referring URL |
| Device platform | User device: Desktop/Mobile/App |
| Referring channel | The method or source through which a customer arrives at your online store |
| Referring category | Traffic source classification |
| Referring type | Traffic type (Organic/Paid) |
| Customer ID | Unique purchaser identifier |

### Metrics

#### Sales performance

| Metric | Definition |
|--------|------------|
| Gross sales | `Product Price × Quantity` (pre-tax, pre-discount) |
| Net sales | `Gross Sales - Discounts - Returns` |
| Total sales | `Gross Sales - Discounts - Returns + Taxes + Shipping` |
| Gross profit | `Net Sales - Cost` |
| Gross margin | `(Net Sales - Cost) / Net Sales × 100` |

#### Order & customer metrics

| Metric | Definition |
|--------|------------|
| Orders| Total orders in date range |
| Ordered quantity | `Net Quantity + Returns` |
| Customers | Distinct purchasers in date range |

#### Pricing & costs

| Metric | Definition |
|--------|------------|
| Discounts | Total discounts applied. Product discount + order level discount share for a collection of sales. |
| Cost | Total product costs for sold items. |

#### Operational efficiency

| Metric | Definition |
|--------|------------|
| Units per transaction | `Net Quantity / Orders` |
| Average units ordered | `Ordered quantity/ Orders` |
| Average Order Value (AOV) | `(Total Sales - Discounts) / Orders` |

## Impact of product changes on reports

The report records the details of orders at the time of sale. If you change a product’s name or category, the sales report may show multiple records for the same product, or it may omit some sales information. This is because the report records both the product information before and after the change separately.

**Example 1**:

Let’s assume you’re selling a pair of sneakers:

- **June 1st**: You sold a pair of sneakers named **Running Shoes - Black.**
- **June 3rd**: You changed the product name to **Black Running Shoes.**
- **June 5th**: You sold the same pair of sneakers again.

When you check the sales report for the period from June 1st to June 5th, the product may appear as two separate records in the report due to the different product names for the two sales dates:

- One entry shows as **Running Shoes - Black.**
- The other entry shows as **Black Running Shoes.**

**Example 2**:

Let’s assume your online bookstore sells *The Miracles of the Namiya General Store*.

- Last year, you sold multiple copies of *The Miracles of the Namiya General Store*, but you did not assign a category to it at the time.
- This year, you started using category labels and added the **Fiction** category to *The Miracles of the Namiya General Store*.

If you view a sales report that spans both last year and this year, and filter for books in the **Fiction** category, the copies of *The Miracles of the Namiya General Store* sold last year will not appear in the report, because they were not classified under the **Fiction** category at that time.
