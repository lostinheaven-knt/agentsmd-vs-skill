# Discounts

The **Discounts report** provides a detailed analysis of discounts applied during sales and their impact on revenue. This report helps you evaluate the effectiveness of different discount strategies.

It covers discount details at both **order** and **product** levels, including discount amounts, their impact on revenue, and calculations for returns and net sales.

**Order-level discounts** are proportionally allocated across **items** in the order. All discounts are **applied before taxes**.

## Report data fields

Key components of the report include:

| Term | Definition |
| ---- | ---------- |
| **Date applied** | The date the discount was applied to the product or order. |
| **Sales channel** | The platform or channel where the sale or return occurred. |
| **Product name** | The name of the product. |
| **Gross sales** | Product price × quantity sold, excluding taxes, shipping, discounts, and returns. This is calculated even if the order was incomplete or canceled. |
| **Item-level discount** | The discount amount applied to a specific product. |
| **Order-level discount** | The total discount applied to the entire order, including shipping discounts. |
| **Total discount** | The sum of item-level and order-level discounts. |
| **Return amount** | The total value of returned products, displayed as a negative value on the return date. |
| **Net sales** | Final revenue after subtracting all discounts and returns: `Gross sales - Total discount - Return amount`. |
