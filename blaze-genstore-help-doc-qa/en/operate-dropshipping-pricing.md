# Set up automated pricing rules

In **Genstore Dropshipping**, you can configure **bulk pricing rules** to automatically calculate and update product prices, reducing manual work.
The system uses your chosen markup logic — either a **fixed amount** or a **percentage multiplier** — and optionally includes shipping cost in the calculation.


## Why use automated pricing

* Automatically calculate and update product prices across your catalog.
* Choose fixed or percentage markups to match your profit strategy.
* Apply tiered pricing by cost range for more granular control.

## Pricing rule hierarchy

Genstore supports two types of pricing rules that work together:

* **Product pricing** – A global rule applied to all products.
* **Tiered pricing rule** – Specific markup rules for defined cost ranges.

When both are configured, **tiered pricing rule takes priority**.
The system first applies tiered rules where conditions are met; products outside those ranges use the default product pricing rule.

## Product pricing

In the **Product pricing** section, you can set a single markup rule that applies to all Dropshipping products, including **product price** and **compare-at price** (strikethrough price).
When products are pushed to your store, the system automatically calculates both **price** and **compare-at price** based on cost.

### Pricing types

| Pricing type            | Description                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------- |
| **Cost/Compare-at price + fixed amount** | Adds a fixed amount to the product cost/compare-at price (e.g., cost + $3).                          |
| **Cost/Compare-at price × multiplier**   | Multiplies the cost/compare-at price by a percentage to define the selling price (e.g., cost × 150%). |
| **Include shipping**    | If select **Include shipping**, the system includes shipping cost in the price calculation.            |

### Steps

1. Go to **Settings -> Product pricing**.
2. Select a pricing type (**Cost/Compare-at price + fixed amount** or **Cost/Compare-at price × multiplier**).
3. Choose whether to **include shipping** in the calculation.
4. Click **Save** — the system will automatically calculate the selling and compare-at prices.

> **Note:**
> Updated rules only apply to newly pushed products. Existing products will not update automatically.


## Tiered pricing rules

Genstore also supports custom price levels for both the **product price** and the **compare-at price**, giving you total control over how your discounts appear to different customers.

### How it works

* **Product price** – The price customers actually pay.
* **Compare-at price** – The original or crossed-out price shown on your storefront.
  Each can have separate cost ranges and markup logic. The system applies the appropriate rule automatically based on product cost.

### Rule types

| Pricing type                   | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **Fixed markup by range**      | Adds a fixed amount for each defined cost range (e.g., cost + $3).    |
| **Percentage markup by range** | Multiplies cost by a percentage within each range (e.g., cost × 150%). |

> Both rule types allow you to include or exclude shipping costs.

### Steps

1. Go to **Settings → Tiered pricing rule**.
2. Under **Product price** or **Compare-at price**, click **Add rule**.
3. Enter the price range (e.g., $0–$100 / $100–$300).
4. Set the markup amount or percentage, and choose whether to include shipping.
5. Click **Save** — the system will apply the rules automatically when products are pushed.

### Example

| Cost range | Product price markup | Compare-at price markup |
| ---------- | -------------------- | ----------------------- |
| $0–$50     | +50%                 | +80%                    |
| $50–$100   | +30%                 | +50%                    |


## Price display optimization

To make prices more visually appealing and psychologically consistent (e.g., $9.99 or $19.95), enable **price display optimization**.
The system automatically rounds and adjusts the decimal portion of the calculated price.

### Steps

1. Check **Set price decimals** or **Set compare-at price decimals**.
2. Enter your preferred decimal pattern (e.g., .99 or .95).
3. Click **Save** — the system applies this rule to all newly calculated prices.

## Primary shipping country

The **primary shipping country** determines which shipping cost is used as the base for price calculations.
The system uses this country’s shipping rates to estimate total landed cost and profit margin.

> For example:
> If your primary shipping country is **United States**, the system will automatically use shipping costs to the U.S. as the calculation basis.
