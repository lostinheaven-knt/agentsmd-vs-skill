# Order reward points

Order reward points are a powerful marketing tool, which allows merchants to issue points based on the order amount or assign fixed points per order. You can also tailor reward rules for different product categories, effectively refining marketing strategies.

This document outlines how to configure this feature, including use cases and important considerations.

## Configure point rules

**Navigation**: 

1. Log in to Genstore admin and go to **Store** -> **Customers** -> **Loyalty**. 
2. Under the **Points** tab, find the **Earn points** section.
### Setup steps

Click **Add** -> **Place an order** -> **Add**.

- **Rule name**: Provide a name for this reward rule to facilitate easy management.
- **Earning rules**:
  - **Reward points based on the order amount (recommended)**: Customers earn points proportional to the order amount, e.g., 10 points for every $10 spent. Ensure only positive integers are entered.
  - **Award fixed points per order**: Customers earn a set number of points per order, e.g., 100 points.
- **Rule limitations**: Select whether to award points for all products, specific products (up to 20), or product collections (up to 10).
- **Set earning frequency**:  Choose how often points can be earned from orders, such as daily, weekly, monthly, yearly, or only on the first sharing order.

## Preview and publish

Check your settings in the **Summary** section to the right. The system provides a real-time summary here. Once you confirm the details, click **Save** to activate the rule.

You can manage this rule - view, edit, enable, or disable it - via the **Earn points** list

:::tip

Use the status switch to easily toggle this rule on or off.

Genstore Loyalty offers more configuration options, you can click **Store** -> **Customers** -> **Loyalty**, then **Settings** -> **General** to explore. For details, see [Advanced settings](./operate-customers-loyalty-general-setting.md)

:::

::: faq

## FAQs

### Q1. Can I apply order points to specific products?
> A: Yes. Under **Rule limitations**, you can specify applicable products or collections. Note: You can add up to 20 products or 10 collections.

### Q2. Do customers need to reach a specific order amount to earn points?
> A: If you choose to **Reward points based on the order amount (recommended)**, customers must meet a minimum order threshold to qualify for points, e.g., $100 for 100 points.

### Q3. Are points automatically deducted if an order is refunded?
> A: Yes. Points are adjusted according to global return rules if an order is fully or partially refunded. If the refunded amount falls below the minimum threshold, all points issued will be deducted.

### Q4. Do suspended customers earn points on orders?
> A: No. Suspended customers in your membership system do not earn points for any transactions, including orders.

### Q5. How are points calculated and revoked when an order contains both eligible and ineligible items?
> A: You may refer to the table below:

| Scenario            | Points calculation                                           | Points revocation                                            |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Order amount points | Only calculated on eligible items                            | Revoked proportionally based on refunded eligible items      |
| Fixed order Points  | Calculated based on eligible items' proportion of total order | Recalculated based on remaining eligible items' proportion after refund |

:::