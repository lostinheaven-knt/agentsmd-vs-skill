# Metafield data types

Each metafield type supports specific data formats. Choose the type that best fits your use case and how you want to display or manage data in your store.

Metafield types are grouped into the following categories:

- Text
- Numbers
- Date and time
- Measurement
- Reference
- Other
## Text fields

|Data type|Description|Example|
|---|---|---|
|**Single-line text**|Supports plain text in one line. Can be limited to predefined values.|Add short notes or product tags.|
|**Multi-line text**|Supports longer text with optional character limits and regex validation.|Add shipping notes or return policies.|
## Number fields

|Data type|Description|Example|
|---|---|---|
|**Integer**|Whole numbers only|Page count, inventory stock|
|**Decimal**|Supports decimals and whole numbers|Product weight in carats, rating values|
## Date and time fields

| Data type       | Description                     | Example                                                              |
| --------------- | ------------------------------- | -------------------------------------------------------------------- |
| **Date**        | ISO 8601 format (`yyyy-mm-dd`)  | Product expiration date, customer birthday  <br>e.g., `2025-05-28`   |
| **Date & time** | ISO 8601 format + UTC timestamp | Product launch time, campaign start  <br>e.g., `2022-01-01T12:30:00` |
## Measurement fields (Metric and Imperial)

|Data type|Description|Example|
|---|---|---|
|**Weight**|Accepts decimals or whole numbers in units like `kg`, `g`, `lb`, or `oz`|Raw material weight, e.g., `500g`|
|**Dimension**|Accepts decimals or whole numbers in `mm`, `cm`, `m`, `inch`, etc.|Product height, e.g., `80cm`|
|**Volume**|Accepts values in `ml`, `l`, `m³`, `us_qt`, and other units|Cup capacity, e.g., `350ml` or `1 us_qt`|
## Reference fields (Link to store resources)

| Data type      | Description                                                                                                | Example                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Customer**   | Reference a customer in your store                                                                         | Link a field to a specific customer (e.g., sales rep) |
| **Product**    | Reference another product (for related or bundled items)                                                   | Set a “Frequently Bought Together” product            |
| **Variant**    | Reference a specific product variant (e.g., color or size)                                                 | Link to other products with matching styles           |
| **Collection** | Link to one or more product collections                                                                    | Create “Complete the Look” sections                   |
| **File**       | Reference files from your media library (see [Media requirements](./settings-media#contents-requirements)) | Upload instructions, certificates, PDFs               |
## Other field types

|Data type|Description|Example|
|---|---|---|
|**Color**|Accepts RGB values in `#RRGGBB` format|Set primary color, e.g., `#FF9900`|
|**Money**|Decimal value with store currency code|Cost price or wholesale price, e.g., `$10.50`|
|**URL**|Accepts `http://` or `https://`, can be limited by domain|Link to brand site or product video|
|**True / False**|Boolean value (toggle or checkbox)|Enable engraving: `true`|

::: tip

- Each data type supports different input controls, validations, and frontend behaviors.
- Choose the type based on your data format, user needs, and storefront display requirements.

:::