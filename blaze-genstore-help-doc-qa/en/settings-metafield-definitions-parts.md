# Components of a metafield definition

Before creating a metafield, you’ll need to define its structure and scope. Each metafield definition specifies where the field applies (e.g., products, variants, or customers) and defines its data type, validation rules, and other options.
## Field components

| Field                     | Required | Description                                                                                                                                                                                                                                     |
| ------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                  | Yes      | The display name shown in the Genstore admin, such as `Color`. This is used for UI purposes only and does not need to be unique.                                                                                                                |
| **Namespace & key**       | Yes      | - A unique identifier in the format `namespace.key` (e.g., `custom.color`)  <br>- Use namespaces to group related fields  <br>- Must be unique across your store and contain only letters, numbers, hyphens (`-`), and underscores (`_`)        |
| **Type**                  | Yes      | The data format used for this field, such as text, date, URL, or boolean. This determines the input method shown to users. See [supported data types](./settings-metafield-definitions-types.md) for details.                                   |
| **Description**           | No       | Optional guidance to help users enter values correctly. Appears next to the field in the admin panel. You can include formatting instructions or examples.                                                                                      |
| **Validation**            | No       | Optional input restrictions such as character limits, regex patterns, or predefined values. Only available for certain data types. Some rules are mutually exclusive (e.g., predefined options cannot be used with min/max character settings). |
| **Accept list of values** | No       | Determines whether the field can store multiple values (e.g., multiple tags, colors, or files). Supported only for compatible data types.                                                                                                       |
| **Access options**        | No       | Controls whether this field is available to the storefront via Liquid or the Storefront API:  <br>- **Readable** – The field can be accessed on the storefront  <br>- **No access** – The field is for internal admin use only                  |
## Example

Here’s an example for a `Product expiration date` field:

- **Namespace & key:** `products.expiration_date`
- **Type:** Date
- **Description:** Enter in `YYYY/MM/DD` format
- **Validation:** Accepts only dates between `2025/01/01` and `2030/12/31`