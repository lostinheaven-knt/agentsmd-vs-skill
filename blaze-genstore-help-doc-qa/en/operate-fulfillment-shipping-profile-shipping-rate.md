# Shipping rates

Shipping rates are the charges you apply to customers at checkout and the cost of the ordered items. You can set up one or more shipping options for customers to choose from during checkout. For more details on how to configure shipping, refer to [Configure shipping profiles](./operate-fulfillment-shipping-profile-configuration.md).

## Flat rate

A flat rate means the shipping cost stays the same regardless of the number of items or types of products in the customer’s order. If you want to offer customers multiple shipping options with varying shipping services and shipping rates, you can add multiple fixed shipping rates.

Example: If you want to offer two shipping options
- Standard Shipping for $8
- Expedited Shipping for $15

You can set up two fixed shipping rates options:
- "Standard" with a fee of $8
- "Expedited" with a fee of $15. 

Customers will see both options during checkout.

## Rate by price

Shipping rates based on product price allow you to set different fixed shipping rates for different order total price ranges. For example, you can set: 
- A shipping fee of $20 for orders under $100
- $15 for orders between $100 and $500
- Free shipping for orders over $500.

Note:

- The order price only includes the total price of the products and does not include taxes, shipping rates, or other additional charges.
	- Example: If Customer A orders 3 hats and 1 pair of gloves, with the hats priced at $30 each, the gloves at $25, and a 10% tax, 
		- Actual paid amount will be: `((3 × 30) + (1 × 25)) × (1 + 10%) = $126.50`
		- Order price for shipping calculation is: `(3 × 30) + (1 × 25) = $115`
		- Shipping fee will be calculated based on the `$115` amount.
- The order price is based on the sales price of the products.

## Rate by weight

Shipping rates based on weight allow you to set different fixed shipping rates for orders within specific weight ranges.

For example, you can charge:
- $5 shipping for orders weighing less than 10kg
- $15 for orders between 10kg and 50kg
- $30 for orders over 50kg

**Note:**

- For weight-based shipping, the system adds up the weight of all items to calculate the total weight, which is then used to determine the shipping fee.
	- Example: If Customer A orders 2 boxes of apples (8kg each) and 1 box of oranges (12kg),
		- Total order weight is: `2 × 8 + 12 = 28kg`
		- Shipping fee will be calculated based on the 28kg total
- Since the weight attribute is optional, **if any item in the order is missing a weight configuration, the system will assume its weight is 0**. Therefore, if you use **weight-based shipping**, make sure to configure the weight attribute for all applicable items.
- Weight is based on the product weight only and **does not include** packaging weight.

## Rate by quantity

Shipping rates based on product quantity allow you to set fixed shipping rates based on the number of products in an order.

For example, you can charge
- $5 shipping for orders with less than 100 products
- $15 for orders with 100 to 500 products
- Free shipping for orders over 500 products.

## Shipping fee consolidation

Genstore allows you to define your store’s shipping strategy through [shipping profiles](./operate-fulfillment-shipping-profile.md). When you configure multiple shipping profiles, and a customer’s order contains products that apply to different shipping profiles, the system will merge the shipping fees for those items. Understanding shipping fee consolidation helps you create more efficient shipping rate strategies that balance shipping costs while offering attractive fees to customers.

**Prerequisites for shipping fee consolidation:**

Consolidation occurs when all of the following conditions are met:

1. There is at least one non-default shipping profile (if only the default profile is used, consolidation will not occur).
2. The customer’s order contains items that are covered by different shipping profiles (if the order contains only one product or all items are covered by the same profile, consolidation will not occur).

### Shipping fee consolidation rules

#### 1. Consolidate shipping fees with the same name

When items come from different shipping profiles, shipping fees with the same name across profiles will be merged and displayed to the customer during checkout.

*Example: You have two different shipping profiles for T-shirts and hats. Both profiles offer Standard and Expedited shipping options with the same names. When a customer orders both a T-shirt and a hat, the shipping fees will be consolidated.*

| T-shirt profile                                         | Hat profile | Shipping options at checkout |
| ---- | ---- | ---- |
| \- Standard shipping: $4 <br/> - Expedited shipping: $8 | \- Standard shipping: $5 <br/> - Expedited shipping: $10 | \- Standard shipping: $9 <br/> - Expedited shipping: $18 |

:::tip

1. When fees with the same name are consolidated, there are no restrictions on the type of fee calculation method.
	- For example, when the fee names are identical, Flat rate can be consolidated with Rate by price.
2. If any fee consolidation includes an **additional description** and the descriptions match exactly, the merged shipping options will still display that description. If the descriptions are different, they will not be displayed.
3. If multiple fees with the same name exist across different profiles, the system will choose the one with the lowest fee amount to consolidate. 
	- Example: The T-shirt profile has a standard shipping fee of $4 and the Hat profile has standard shipping fees of $5 and $7.
		- The system will consolidate the $4 and $5 fees, so the customer will pay a total of `$4 + $5 = $9`.

:::

#### 2. Consolidate different named shipping fees by choosing the cheapest option

When items come from different shipping profiles and the fee names are different, **the system will choose the cheapest shipping fee from each profile and consolidate them**.

Example: 
- You have two shipping profiles for T-shirts and hats. 
- Both profiles offer standard and expedited shipping, but with different names. 
- When a customer orders both items, the system will choose the lowest shipping fee from each profile.

| T-shirt profile                        | Hat profile                                               | Shipping options at checkout |
| -------------------------------------- | --------------------------------------------------------- | ---------------------------- |
| - Standard: $4  <br /> - Expedited: $8 | - Regular shipping: $5  <br />  - Expedited shipping: $10 | - Shipping: $9               |

:::tip

1. There are no restrictions on the types of shipping fee calculation methods when consolidating rates with different names.
2. Once fees with different names are consolidated, the final shipping option will be labeled as **Shipping**, and no additional description from individual fee will be displayed.

:::

#### 3. Merge both same-named and different-named fees from multiple profiles

If multiple profiles contain both same-named and differently named shipping fees, the system will first consolidate the same-named fees, and then select the cheapest differently named fee from each profile for consolidation.

| T-shirt profile                                              | Hat profile                                                  | Shipping options at checkout          |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------- |
| - Standard: $4 <br/>  - Expedited: $8  <br/> - Next-day: $20 | - Regular shipping: $5 <br/>  - Expedited shipping: $10 <br/> - Next-day: $20 | - Shipping: $9 <br/>  - Next-day: $40 |

:::tip

1. If the consolidation of the same-named fees results in a higher total than the consolidated different-named fee, the different-named fees will not be displayed at checkout.
2. If there are missing fees in the different-named categories during consolidation, those fees will be excluded from the final consolidated amount.

*Example: If the T-shirt profile has three options (A, B, C) and the Hat profile has two options (A, C), the customer will only see the merged option A and C at checkout.*

:::
