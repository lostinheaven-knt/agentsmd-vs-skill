# Manage payouts

The payouts page allows merchants to transfer funds from their Genstore account to a designated bank account. On this page, merchants can view the latest payout status, estimated arrival time, and bank account details.

This page includes:

- View recent payout records
- Interpret key fields in payout details
- Track the estimated arrival time and status

## How to access

Log in to the Genstore admin, then click **Finance** -> **Payouts** in the left navigation bar. On the payouts page, you can view all payout records and details related to your bank account.

::: tip
You must first activate **Genstore Payments** to use the **Finance** feature.
:::
## Payout overview

At the top of the page, you’ll find an overview of your payouts, giving you a quick summary of the payout status and bank account information:

- **In transfer**: The total amount of payouts currently being processed.
- **Estimated date**: The expected time for the next payout to arrive.
- **Payouts configuration**: Displays your current bank account information, including bank name and account details.
  :::tip
  To update your bank account information, go to **Settings** -> **Payments**. Click **Bank**  under [Genstore Payments](./operate-genstore-payments.md) to modify your account details.
  :::

## Recent payouts

At the bottom of the page, you’ll see recent payout records. Each record includes the following fields:

| Field name               | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Batch                    | The internal batch number of the payout order                |
| Creation date            | The date the payout transaction was initiated                |
| Estimated in             | The expected date the funds will arrive. The actual arrival date may vary depending on the receiving account. |
| Status                   | The status of the payout order                               |
| Payment reference number | The transaction reference number for the payout              |
| Payout amount            | The amount the recipient is expected to receive. If the receiving bank charges additional fees, the actual amount received may be less than the payout amount |

## View payout details

Click the **View** button under **Recent payouts** to access detailed payout information. The payout details include:

| Field name             | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| Payout amount          | The amount the recipient is expected to receive. If the receiving bank charges additional fees, the actual amount received may be less than the payout amount. |
| Date                   | The time the payout transaction was initiated                |
| Recipient bank account | The bank account details for the recipient, as set by the merchant |
| Status                 | The status of the payout order                               |
| Type                   | The type of transfer to the bank account (default is "bank") |
| Priority               | The priority level of the payout (default is "regular")      |
| Statement descriptor   | The transaction description that appears on the receiving bank's statement |
| Estimated date         | The expected date the funds will arrive. The actual arrival date may vary depending on the receiving account. |
