# Automated product collection filters

The **Genstore** [automatic product collection feature](./operate-product-collections-auto.md) allows you to automatically add products that meet certain criteria into the appropriate collections. By setting conditions, you can filter products based on attributes like product type, title, key features, description, price, and inventory, and automatically assign them to a collection. This feature is especially useful for managing large volumes of products, improving product classification efficiency, and saving time on manual tasks.

:::tip

- You can add multiple conditions to filter products. Each automatic collection can include up to 60 conditions.
- Each condition can be set to match **all conditions** or match **any condition**, depending on your needs.
  - If you choose all conditions, products must meet all the conditions to be included in the collection.
  - If you choose any condition, products only need to match one condition to be included in the collection.

:::

## Filter by product type

You can filter products by type and automatically add them to the collection. Multiple conditions can be matched.

| Term   | Description                                                                                          |
| ------ | ---------------------------------------------------------------------------------------------------- |
| Equals | Select the product type (physical product, digital product, gift card, etc.) from the dropdown menu. |

## Filter by product title and key features

You can filter products by their title or key features and match the appropriate products. You can add multiple conditions.

| Term             | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Equals           | The product title or key features must exactly match the entered value. |
| Not equals       | The product title or key features must not match the entered value. |
| Starts with      | The product title or key features must start with the entered value. |
| Ends with        | The product title or key features must end with the entered value. |
| Contains         | The product title or key features must contain the entered value (at least 3 characters long, and cannot start or end with a space). |
| Does not contain | The product title or key features must not contain the entered value (at least 3 characters long, and cannot start or end with a space). |

## Filter by product description

You can filter products by their description and match the appropriate products. Multiple conditions can be added.

| Term             | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Contains         | The product description must contain the entered value (at least 3 characters long, and cannot start or end with a space). |
| Does not contain | The product description must not contain the entered value (at least 3 characters long, and cannot start or end with a space). |

## Filter by product category

You can filter products by category and automatically add products of a specific category to the collection. To set this condition:

1. In the first dropdown, select **Equals**.
2. In the second dropdown, select the specific product category.

## Filter by product price, original price, inventory, or weight

You can filter products by price, original price, inventory quantity, or weight. Conditions can be set for exact matches, range matching, or other comparisons.

| Term                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Equals                   | Exactly matches the specified value.             |
| Not equals               | Does not match the specified value.              |
| Greater than             | Greater than this value.                      |
| Less than                | Less than this value.                         |
| Greater than or equal to | Greater than or equal to this value.          |
| Less than or equal to    | Less than or equal to this value.             |

## Filter by product tags

You can filter products by tags and include products with matching tags in the collection. Set this condition by following these steps:

1. Select **Product tags** in the first dropdown.
2. Choose **Equals** in the second dropdown.
3. Select the tag from the dropdown menu.

## Filter by product vendor

You can filter products by their vendors and automatically add products from a specific manufacturer to the collection. To set this condition:

1. Choose **Product vendor** in the first dropdown.
2. Select **Equals** in the second dropdown.
3. Select the specific vendor.
