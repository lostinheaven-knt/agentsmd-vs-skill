# Add a metafield definition

To start using metafields, you first need to create a **metafield definition**—a template that sets the field’s name, data type, validation rules, and which part of your store it applies to (e.g., products, variants, or customers). Once defined, you’ll be able to add values to this field for specific items.
## Before you begin

We recommend reviewing the following first:
- [Definition components](./settings-metafield-definitions-parts.md): Learn how namespaces, keys, and validation rules work
- [Metafield data types](./settings-metafield-definitions-types.md): Understand which data formats are available (text, date, file, etc.)

## Operation steps

1. In your Genstore admin, go to **Settings -> Metafields**.
2. Choose the module where the field will be used (e.g., **Products**).
3. Click **Add definition**.
4. Enter a **Name** for the field (this appears in the UI).
5. Enter a **Namespace and key** (used to uniquely identify the field).
6. _(Optional)_ Add a **Description** to guide users when entering values.
7. Click the **Type** dropdown and select the appropriate data type.
8. _(Optional)_ Check **Value list** if you want to allow multiple entries (e.g., multiple tags or files)
9. _(Optional)_ In the **Validation** section, set rules to control input—such as max characters or allowed formats, based on the data type
10. _(Optional)_ In the **Options** section, choose visibility:
    - **Readable** – Allow this field to be accessed via Liquid templates or the Storefront API
    - **No access** – For internal use only (not exposed to storefront)
11. Click **Save**
## What’s Next?

After creating a metafield definition, you can:
- [Pin or unpin definitions](./settings-metafield-pin-unpin.md) to control which fields are shown by default and in what order
- [Add values to metafields](./settings-metafield-adding-values.md) for individual products, variants, or customers