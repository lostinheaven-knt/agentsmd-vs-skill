# Draft order

A draft order is an order that the customer has not yet completed. It includes products the customer has selected, but it hasn’t entered the checkout or payment stages yet. You can view, modify, or delete draft orders in Genstore admin to provide better service.

A draft order may include the following: one or more products (such as physical products, virtual products, or custom products), manually added discounts (like product discounts or order discounts), shipping information, tax information, customer details, tags, market data, and order notes.

You can create a draft order for a customer and send them a link to the checkout page. The customer can complete the payment through this link, or they can pay offline, and you can manually convert the draft order to a paid official order. Here's how:

1. Log in to Genstore admin and click **Store** -> **Orders** -> **Draft orders**.
2. Click **Create order** at the top right of the page to go to the **Draft orders** page.

## Add products

1. On the **Draft orders** page, click **Add product**.
2. In the pop-up **Select products** dialog, check the products you want, set the quantity, and click **Save**.
   **Note**: Please verify the quantities of the products you add. If a product's stock is zero and it doesn't allow overselling, customers will receive an out-of-stock message when attempting to complete the purchase.
3. After successfully adding products, you can remove them using the **Delete** button.

## Add custom products

Custom products are personalized items you add based on specific needs.

1. On the **Draft orders** page, click **Add custom product**.
2. In the pop-up **Add custom product** dialog, you can enter the product name, price, quantity, whether tax is required, whether it is a physical item, and weight.
   **Note**: Please verify the quantities of custom products. If a product’s stock is zero and it doesn't allow overselling, customers will see an out-of-stock message when attempting to complete the purchase.
3. After adding the custom product, you can remove it using the **Delete** button.

## Add discounts

**Product discount**

A product discount applies to a specific product and can either be a fixed amount or a fixed percentage off the price of a single item.

- On the **Draft orders** page, click **Add discount** next to the product price.
- In the pop-up, select the **Discount type** (Amount or Percent), enter the discount amount or percentage, and provide a discount reason. The discount is applied to each individual product, and if you have multiple units of the same product, the discount is automatically calculated based on the quantity.
  **Example**: If you add product A (price $10.00 USD, quantity 2) and apply a $2.00 USD discount per product, the total discount for this product will be $4.00 USD.
- Click **Save** to apply the discount. You will see the discount amount below the product price after saving.

**Order discount**

An order discount applies to the entire order and can be either a fixed amount or a percentage off the total order price.

- On the **Draft orders** page, click **Order discount** in the summary section.
- In the pop-up, select the **Discount type** (Amount or Percent), enter the discount amount or percentage, and provide a discount reason.
- Click **Save**.

## Add customer information

On the **Draft orders** page, click the edit icon next to **Customer**. Search by their name or select from the dropdown menu.

After adding the customer, you can view or edit their name, contact details, shipping address, and billing address.

## Add shipping rate

If the order requires shipping, you can choose from preset shipping fee, create a custom fee, or select local delivery or store pickup. **Note**: You must add customer information before adding shipping fees.

On the **Draft orders** page, click **Shipping** in the **Summary** section:

- **Select existing shipping plans**: Choose a shipping plan that meets the criteria. For local shipping, select **Pickup in store**, then choose a location.
- **Custom shipping fee**: Select **Custom**, then enter the name and amount for the fee.

## Add tax

- On the **Draft orders** page, click **Tax** in the **Summary** section.  In the pop-up, confirm whether to apply tax.

## Add notes and tags

- On the **Draft orders** page, click the edit icon next to **Note** to add notes to the order. The note can be up to 100 characters long.
- On the **Draft orders** page, you can add tags in the **Tags** field. Separate multiple tags with commas, and each tag can be up to 20 characters long.

## Change product market

The default market for a draft order is the store's primary market. To change the pricing for a specific market, you need to activate that market and its local currency. Be sure to understand the impact of price changes before modifying the pricing. Here's how:

- Click the edit icon next to **Markets**.
- Select a market and apply its pricing to the draft order.
- Click **Confirm** to apply the new market and pricing.

::: tip
Due to regional pricing policies and compliance regulations, switching markets requires you to re-select products and update your settings for the new region.
:::

## Save and send draft order

1. Click **Save** to create the draft order and save it for later updates.
2. Send the checkout link to the customer. They can complete the payment through the link.
3. If offline payment is selected, manually mark the draft order as paid once the payment is completed.

## Delete draft order

You can delete both **Incomplete** and **Completed** draft orders:

1. In Genstore admin, click **Store -> Orders -> Draft orders**.
2. Select the draft orders to delete.
3. Click **Delete order**.

Deleting a completed draft order will not remove the order created through the draft.

::: faq

## FAQs

### Q1. Which fulfillment location is used by default for draft orders?

> A: Draft orders automatically use the default fulfillment location set in your [Locations](./operate-fulfillment-location.md) settings. To update your default location, go to **Settings** -> **Locations** in your Genstore admin.

:::