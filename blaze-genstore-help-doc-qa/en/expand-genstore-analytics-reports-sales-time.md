# Sales over time

The **Sales over time** displays order volume and total sales within specified date ranges. **Group data by hour, day, week, or month** for granular analysis, and compare performance across periods using metrics like Total Sales, Gross Sales, Orders, Returns, Shipping, and Taxes.

## Use this report to

- **Trend Analysis**: Track metric fluctuations across time cycles.
- **Multidimensional Insights**: Analyze data by product, region, or customer segment.
- **Custom Metrics**: Select specific KPIs for targeted analysis.
- **Transaction Details**: Drill down into individual sales records.

## Report data fields

The sales reports use several [common terms](./expand-genstore-analytics-reports-sales#common-terms).

**Additional terms specific to this report**:

### Daily Sales

| Field | Definition |
|-------|------------|
| Day | Date when the order was created. Displays **daily** sales metrics. |

### Weekly Sales

| Field | Definition |
|-------|------------|
| Week | Calendar week of order creation. Shows **weekly** aggregated data. |

### Monthly Sales

| Field | Definition |
|-------|------------|
| Month | Month of order creation. Presents **monthly** summarized metrics. |

### Hourly Sales

| Field | Definition |
|-------|------------|
| Hour | Hour of order creation (00-23). Provides **hourly** sales trends. |

## Impact of order edits

Edited orders will be displayed as **new entries** in this report, even if modifications occur post-transaction. The system retains both original and revised records.

## Impact of custom columns

Adding custom columns to the report may:

- Alter default grouping logic
- Create new rows for each product variant in an order
- Increase loading times for complex queries
