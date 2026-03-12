# Payout period

The payout period is the time between a completed transaction and when you actually receive the funds. This timeline is determined by several factors, including your specific country or region, your account's risk level, and other regulatory constraints.

When using Genstore Payments, funds move through three distinct stages from the moment of purchase to the final deposit:

1. Clearing (payment confirmation): After a customer pays, the funds enter the payment network to be verified and processed.
2. Settlement (funds entry): Once cleared, the money is officially transferred from the customer’s bank to the Genstore merchant account and added to your "settleable balance."
3. Payout (transfer to your bank): When your scheduled payout cycle arrives, the system automatically sends your settleable balance to your linked bank account.

::: tip
- Other providers: If you use third-party payment gateways, their rules and payout frequencies may vary. We recommend contacting those providers directly for their specific terms.
- Settlement timing: The minimum time it takes to settle funds depends on your location, your business risk profile, and the payment methods used.
- Adjustments: Certain transactions, like refunds and chargebacks, may process faster than standard sales, but they will reduce your final payout amount.
:::

If a payout is taking longer than expected, please take the following steps:
- Check your Genstore admin: Look for any banners, alerts, or notifications regarding your account status.
- Review your email: Check the inbox of the store owner for any emails from Genstore regarding payment or verification issues.
- Contact support: If the cause is still unclear, contact Genstore customer service. Our team can help you understand your account status and provide instructions on how to resolve any issues causing the delay.

## View payment amount

You can check the payment amount and status directly through your store's admin. Here’s how:

1. In Genstore admin, find **Finance** -> **Payouts** in the left-hand menu.
2. In the **Recent payouts**, click **View** in the **Actions** column. A new window will pop up where you can see the latest payment batch, payment amount, payment status, and transaction details.

::: tip
You must first activate **Genstore Payments** to use the **Finance** feature.
:::

### Additional fees

**Third-party transaction fees**

When processing payments through **Genstore Payments**, you won’t incur any third-party transaction fees. **Note**: You’ll still need to pay credit card processing fees, depending on your Genstore subscription plan.

If you use a third-party payment provider, you may incur additional transaction fees, especially for credit card payments. The issuing bank, acquiring institution, and credit card company may charge their own fees.

## Set payment cycle

When you use **Genstore Payments**, all successfully settled funds can be automatically paid out to your bank account based on the payout frequency you choose. Here’s how to set up your payment cycle with **Genstore Payments**:

1. In Genstore admin, under **Settings**, find the **Payments** menu.
2. Under Genstore Payments, Click **Bank**. Then go to the **Payout schedule** settings.
3. You can choose to have payments sent to your bank account every business day, Tuesday, Thursday, the 1st of each month, or the 15th of each month.

## Payout waiting period

The payout waiting period is vital for maintaining payment security and building customer trust. This period allows our banking partners to verify your business information and reduces the risks associated with processing transactions for specific business types.

When you begin processing transactions with Genstore Payments, funds are typically sent at least 5 business days after the transaction date to help prevent fraud. However, the actual timing may vary based on your account's security level and risk profile.

For newly activated Genstore Payments accounts, there may be an initial waiting period of up to 21 calendar days between your first customer payment and your first payout. After this initial period is complete, your funds will be settled according to your pre-set payout schedule.

## Public holidays and payment cycle

Public holidays can impact when you receive payments. If a sales day, payment day, or any day in between falls on a holiday, it could cause delays. Here’s how public holidays might affect your payment cycle:

| Sales day                   | Public holiday        | Payout    |
| :-------------------------- | :-------------------- | :-------- |
| Monday                      | -                     | Wednesday |
| Monday                      | Tuesday and Wednesday | Friday    |
| Thursday                    | Monday next week      | Tuesday   |
| Friday, Saturday and Sunday | Monday                | Wednesday |

**Here are the public holidays in 2026**

| Currency | Country/Region | Date     | Day  | Holiday name                         |
| -------- | -------------- | -------- | ---- | ------------------------------------ |
| USD      | US             | 20260101 | Thu  | New Year's Day                       |
| USD      | US             | 20260119 | Mon  | Martin Luther King Jr. Day           |
| USD      | US             | 20260216 | Mon  | Presidents' Day                      |
| USD      | US             | 20260525 | Mon  | Memorial Day                         |
| USD      | US             | 20260619 | Fri  | Juneteenth National Independence Day |
| USD      | US             | 20260704 | Sat  | Independence Day                     |
| USD      | US             | 20260907 | Mon  | Labor Day                            |
| USD      | US             | 20261012 | Mon  | Columbus Day                         |
| USD      | US             | 20261111 | Wed  | Veterans' Day                        |
| USD      | US             | 20261126 | Thu  | Thanksgiving                         |
| USD      | US             | 20261225 | Fri  | Christmas                            |
| HKD      | HK             | 20260101 | Thu  | New Year's Day                       |
| HKD      | HK             | 20260217 | Tue  | Lunar New Year 1                     |
| HKD      | HK             | 20260218 | Wed  | Lunar New Year 2                     |
| HKD      | HK             | 20260219 | Thu  | Lunar New Year 3                     |
| HKD      | HK             | 20260403 | Fri  | Good Friday                          |
| HKD      | HK             | 20260404 | Sat  | Holy Saturday                        |
| HKD      | HK             | 20260406 | Mon  | Easter Monday                        |
| HKD      | HK             | 20260407 | Tue  | Ching Ming Festival                  |
| HKD      | HK             | 20260501 | Fri  | Labour Day                           |
| HKD      | HK             | 20260525 | Mon  | Buddha's Birthday*                   |
| HKD      | HK             | 20260619 | Fri  | Tuen Ng Day*                         |
| HKD      | HK             | 20260701 | Wed  | SAR Establishment Day                |
| HKD      | HK             | 20260926 | Sat  | Day Following Mid-autumn Festival*   |
| HKD      | HK             | 20261001 | Thu  | Chinese National Day                 |
| HKD      | HK             | 20261019 | Mon  | Chung Yeung Day*                     |
| HKD      | HK             | 20261225 | Fri  | Christmas Day                        |
| HKD      | HK             | 20261226 | Sat  | Christmas Holiday                    |
> If you're using a third-party payment provider, log in to their platform to check your payment status.

## Payment cutoff time

There are specific times during a business day, called cut-off times, when Genstore Payments stops processing payouts for settlement within the settlement delay. Payouts initiated before the cut-off time are typically processed within the specified settlement delay, while those initiated after the cut-off time will be processed the next day within the specified settlement delay.

Different countries/regions and currencies may have different cutoff times. Here are a few examples:

| Country/region | Currency | Priority | Cut-off time | Local timezone | Settlement delay |
| :------------- | :------- | :------- | :----------- | :------------- | :--------------- |
| United States  | USD      | Regular  | 01:45        | ET             | Same day         |
| Hong Kong SAR  | HKD      | Regular  | 15:45        | HKT            | Same day         |

For example, if your account is in the U.S. and payments are successfully settled before 01:45 ET, the payment will be processed the same day, and you’ll likely receive the funds on the next business day.

## Update your bank account

If you need to change or add a bank account, you can update your details in Genstore admin.

Here’s how:

1. In Genstore admin, and under **Settings**, find the **Payments** menu.
2. Under **Genstore Payments**, click **Bank**.
3. You can add a new bank account or click the **Edit** icon to manage multiple accounts.
4. Depending on your location, you may need to provide the following bank account details:
   - **US**: Local bank account information.
   - **HK**: Bank account number, clearing code, and a bank statement.
5. If you have multiple bank accounts, set one as your default payment account for the **Balance account**. The system will use the first verified account as the default payment account.
6. To change the default payment account, go to the **Payouts** section under **Banks**, and the new default account will take effect in the next payment batch.
