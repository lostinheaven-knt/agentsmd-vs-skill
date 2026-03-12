# Create gift card

Genstore offers a gift card feature, which is a prepaid card that customers can use to purchase products or services in your store. It’s commonly used for gifts or as rewards and can be applied at checkout to reduce the order total.

## Manually create a single gift card

This method is suitable when the merchant initiates the gift card issuance, such as for promotional giveaways or customer service compensation. You can set the amount, add a note, and associate a customer for easier sending and tracking.

1. Log in to your Genstore admin and go to **Store** -> **Products** -> **Gift cards**.
2. Click **Create gift card** in the top right corner.
3. In the pop-up window, enter the initial gift card amount.
4. *(Optional)* **Expiration date**: Select whether to set an expiration date for the gift card.
   > **Note**: Please ensure compliance with local regulations regarding gift card validity periods.
5. *(Optional)* **Associate customer**: In the **Customer** section on the right, enter a customer’s name, phone number, or email to create or search for a customer. You can also add a customer later.
   - The customer must provide **at least one contact method** (email or phone) to receive the gift card code via email or SMS.
   - If both email and phone are provided, the gift card will be sent via **email**.
6. *(Optional)* Add internal notes in the **Note** section on the right.
7. Click **Save** to finish creating the gift card.

## Create a purchasable gift card product

If you'd like customers to purchase gift cards directly from your online store and have the system automatically generate and deliver the code, follow these steps:

1. Log in to your Genstore admin and go to **Store** -> **Products** -> **Gift cards**.
2. Click **Create gift card product** in the top right corner.
3. Enter the product title, key features, upload an image, and add a product description.
4. Set an expiration date if applicable.
5. The product category defaults to **Gift card**.
6. In the **Variants** section, define the available gift card denominations.
7. Use the variant table to configure different options by denomination. Refer to the **[Product variants](./operate-product-create#product-variants)** section for detailed setup.

For other settings, refer to the [Add products](./operate-product-create.md) guide.

Once created, you can filter and view gift card products in the product list, or go to the **Gift cards** page and click **View gift card product** to jump directly to the filtered results.

## Export gift cards

You can export all gift card data to a file for data analysis, backup, or offline review.

**Steps:**

1. Go to **Store -> Products -> Gift cards**.
2. Click **Export gift cards** in the top right corner.
3. In the pop-up, choose an export scope:
   - Export gift cards on the current page
   - Export all gift cards
   - Export selected gift cards
   - Export based on current filters/search results
4. Click **Export gift cards** to begin file generation.
5. Once complete, the file will be available for download from the current page or the **Task center**.

## Redeem gift card online

Customers can redeem a gift card when checking out by entering the unique code in the corresponding field. Note: Gift card codes are not case-sensitive.

### Redemption rules

- **Sufficient balance**: If the gift card balance is greater than or equal to the order total, the customer can click **Pay now** to finalize payment.
- **Insufficient balance**: If the gift card balance is less than the order total, the system will prompt the customer to choose another payment method to cover the remaining balance, such as adding another gift card.

### Usage restrictions

- Gift card balances can be used for multiple orders until the balance is fully spent.
- The gift card balance applies to the total order amount, including taxes and shipping fees.
- Gift cards can be used alongside discount codes.
- A single order can use multiple gift cards.
