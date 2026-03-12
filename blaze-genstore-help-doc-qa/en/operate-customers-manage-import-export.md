# Import/Export customers

Effectively managing customer data is crucial for quickly responding to market changes. With Genstore's customer import feature, you can batch add customer information to quickly build and update your customer database. The export feature allows you to back up customer data securely and use it for analysis, marketing strategies, and business decisions.

## Import from local file

The import feature lets you batch add customers to the system, improving data processing efficiency and reducing errors. To ensure smooth data import, we recommend downloading and using the **import template** to edit customer information.

### Prepare the import file

Follow these steps:

1. Log in to the **Genstore admin** and navigate to **Store -> Customers**.
2. Click **Import**, and in the pop-up window, click **Download import template**.

**Explanation of import template columns**

| Column                        | Field Requirements                                           |
| ----------------------------- | ------------------------------------------------------------ |
| First Name                    | Max 200 characters. Required if last name, email, or phone is empty. |
| Last Name                     | Max 200 characters. Required if first name, email, or phone is empty. |
| Email                         | Must be in email format. Required if first name, last name, or phone is empty. |
| Phone                         | Must follow phone number format. Required if first name, last name, or email is empty. |
| Accepts Email Marketing       | Enum values: <br/>- SUBSCRIBED <br/>- NOT_SUBSCRIBED (default) <br/>- PENDING_CONFIRMATION <br/>- UN_SUBSCRIBED <br/>If blank, defaults to NOT_SUBSCRIBED. |
| Accepts SMS Marketing         | Enum values: <br/>SUBSCRIBED <br/>NOT_SUBSCRIBED (default) <br/>If blank, defaults to NOT_SUBSCRIBED. |
| Default Address Company       | Optional, max 1000 characters                                |
| Default Address Address1      | Optional, max 1000 characters                                |
| Default Address Address2      | Optional, max 1000 characters                                |
| Default Address City          | Optional, max 200 characters                                 |
| Default Address Province Code | Follow ISO 3166-1 two-letter country code (e.g., California, US = CA). Case-insensitive. |
| Default Address Country Code  | Follow ISO 3166-1 two-letter country code (e.g., US = US). Case-insensitive. |
| Default Address Zip           | Max 60 characters                                            |
| Default Address Phone         | Follow the correct phone format for each country. Max 60 characters. |
| Tags                          | Case-insensitive, use commas to separate multiple tags (e.g., vip, free). |
| Note                          | Max 1000 characters                                          |
| Tax Exempt                    | Enum values: yes/no (case-insensitive). <br/>- yes: customer is tax-exempt in all regions. <br/>- no (default): customer is not tax-exempt. If blank, defaults to no. |
| Language                      | Must follow ISO-639-1 language code (e.g., English = en). Case-insensitive. |

### Execute import

1. On the **Store -> Customers** page, click **Import**.
2. Click **Add file** and choose your CSV file. Note: Only CSV format is supported, and file size must be under 50MB.
3. Check the **Overwrite existing customer data if emails match** option to confirm whether to overwrite existing data when the email matches.
4. Click **Import customer**. Note: If the previous import task has not finished, you cannot start another import.

The import may take some time. You can leave the page and later check the import progress by clicking your profile icon in the top-right corner, then selecting **Task center**.

## Import from Shopify

Genstore allows you to directly import customer CSV files exported from your Shopify store—no manual adjustments required. This makes it easy to migrate and consolidate customer data in bulk.

### Prepare the import file

1. Log in to your Shopify admin, go to the **Customers** menu, select the customers you want to migrate, and export them as a CSV file.
2. If needed, you can edit the exported CSV file to update customer information, then save it.
3. Log in to your Genstore admin, go to the **Store -> Customers** page, click **Import**, select **Import from Shopify**, upload the file, and click **Import customer**.
4. Alternatively, you can use a template for Shopify imports. In the **Shopify import** tab, click **Download Shopify customer template**, fill in the customer data, and then upload the file to import.
5. The import process may take some time. You can leave the page and check the progress later via **Task center** in the bottom-left corner of Genstore admin.

## Export customers

The export feature allows you to batch save customer information to an external file, making it easier for data analysis and backup.

### Steps to export

1. Log in to the **Genstore admin** and navigate to **Store -> Customers**.
2. Click **Export**.
3. Choose the export range:
   - **Export data matching filter criteria**: Export customers based on the current filter criteria. You can adjust the fields you wish to export.
   - **Export all**: Export all customer information in your store.
4. Click **Export customer** to start the export process.
5. Once complete, you can download the file directly or check **Task center** to view and download it.
