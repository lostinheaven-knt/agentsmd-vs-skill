# Manage payments

The payments page gives users an overview of all orders processed through Genstore Payments. Merchants can check the transaction status of each order and take action on those that need attention. This page includes:

- Key indicators and explanations of the order status dashboard
- Descriptions of the transaction details table

## How to access

To access the payments page:

1. Log in to the Genstore admin.
2. Click **Finance** -> **Payments** in the left navigation bar.

Once on the payments page, you can view detailed transaction information and the associated settlement status for your account. 

::: tip
You must first activate **Genstore Payments** to use the **Finance** feature.
:::

## Dashboard

The dashboard provides an overview of transactions made through Genstore Payments. Key indicators include:

- **Gross**: The total amount of orders within the selected time range.
- **Refunds**: The number and amount of refunded orders within the selected time range.
- **Chargebacks**: The number and chargeback rate of orders within the selected time range.

:::tip

Keep an eye on the total amount and rate of refunds and chargebacks. A high rate could negatively impact the buyer experience and lead to transaction limits, deposit requirements, or other restrictions.

:::

## Payment details

The payment details section shows in-depth information about transactions within the selected time range. Each order entry includes the following fields:

| Field name               | Description                                                                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| Create time              | The time when the payment order was successfully placed                                                                                |
| Payment reference number | The payment reference number for the initiated transaction                                                                             |
| Status                   | The current status of the payment order                                                                                                |
| Order                    | The transaction order number linked to the payment                                                                                     |
| Customer                 | The customer information for the payment order                                                                                         |
| Payment method           | The payment tool used for the transaction                                                                                              |
| Gross                    | The total amount after adjustments, including fees, for the processed payment                                                          |
| Net                      | The amount available for payout after payment adjustments                                                                              |
| Risk score               | The risk score assigned to the payment transaction by Genstore Payments. A higher score indicates higher potential risk (range: 0-100) |

## Filter function

The payment details page includes a filter feature to help you quickly sort settlement records by date and status. To use the filter:

1. Filter by date range.
2. Filter by status, e.g., **Authorized**, **Captured**.

Click **Clear all** to remove all filters and show the full list of records.
