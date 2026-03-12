# Set up Genstore Payments

**Genstore Payments** connects your store to local and international payment channels, reducing payment redirection issues and improving order conversion rates. This guide will walk you through how to apply for and set up **Genstore Payments**.

## Qualification requirements

**Genstore Payments** is an integrated payment gateway provided by Genstore, enabling eligible merchants to accept payments. You must meet the following requirements to use **Genstore Payments**:

- You must be registered in one of the supported countries or regions:
	- [United States](./operate-genstore-payments-usa.md)
	- [Hong Kong SAR](./operate-genstore-payments-hk.md)
- Your business and products must comply with regulations.
- You must adhere to the laws and regulations of your country/region, as well as the terms and conditions of **Genstore Payments**.

If you are unable to meet these conditions, we recommend using a [third-party payment service provider](./operate-payments-third-party.md).

## Set up your Genstore Payments

Setting up **Genstore Payments** is easy. Once your application is approved, you will receive a notification. After approval, you can use your **Genstore Payments** account to collect and make payments.

### Steps to set up

1. In Genstore admin, find the **Payments** menu under **Settings**.
2. Click **Activate Genstore Payments**, then follow the guided steps to fill in the required information and upload your documents. Your account will then be submitted for review, which may take several business days.
3. During the review process, we may ask you to provide additional or updated information. Please follow the instructions in your admin to complete the steps.
4. Once the review is complete, you will need to sign the agreement and finish configuring your **Payment method**, **Balance account**, and **Bank** information.
	> Please note that you can only start receiving payments after configuring your payment methods and balance account.
5. Then click **Activate** at the top to let your customers pay with Genstore Payments in your store.

### Configure payment methods
You need to select the payment methods you wish to accept and enable them on the **Payment methods** page.
* **Card**: All credit and debit card payment methods, including Visa, Mastercard, American Express, JCB, Discover, Diners Club, and Union Pay.
* **Wallet**: Digital wallet payment methods, including Google Pay and Apple Pay.
* **Buy Now, Pay Later**: Currently, only U.S. merchants can accept Klarna payments from local U.S. consumers.

Please note that some payment methods may not be available in certain markets or regions where your customers are located.

* United States merchant
    *   **American Express**: Supported only in USD 
    *   **JCB**: Supported in select major currencies only
    *   **Klarna**: Only supports USD payments within the U.S.

* Hong Kong merchant
    *   **American Express**: Supported in select major currencies only
    *   **Klarna**: Not supported 

For a detailed list of supported payment methods, please refer to [Accepted payment methods](./operate-genstore-payments-pay-options.md)

### Manage your payment account

Once your application is successful, you’ll need to set up basic attributes of your **Payment account**, including the time zone and settlement currency.

#### Payment account time zone

The settlement and payments of your **Payment account** will be processed according to the time zone you set. For example, if your **Payment account** is set to Eastern Time (ET), all incoming and outgoing payments will occur during that time zone.

#### Settlement currency

The settlement currency for your **Payment account** will match the currency of your business’s registered country/region. Supported settlement currencies are:

| Country/Region | Settlement currency |
| -------------- | ------------------- |
| United States  | USD                 |
| Hong Kong      | HKD                 |

> - The settlement currency cannot be changed.
> - The bank account linked to your **Payment account** must support the same settlement currency.

### Account closing time

You can configure your sales day to end later if your user's business closes after midnight. For example, a restaurant owner that operates from noon to 3:00 AM can set the sales day closing to 3:00 AM. This means that the sales day of that business starts at 3:01 AM and ends at 3:00 AM on the next day. You can delay closing times until 6:00 AM.

#### Settlement delay

After a transaction is processed, Genstore Payments applies a regionally specific waiting period for any adjustments before settlement. You can increase or decrease this period on a specific balance account by configuring a settlement delay.

The settlement delay specifies after how many business days the funds in a settlement batch are made available. For example, with a settlement delay of five business days, sales that happened on a Monday are made available the following Monday.

By default, the settlement delay is 5 days. We will dynamically adjust payout delays based on your risk indicators, such as transaction status, dispute status, and fulfillment duration.

**The following table shows examples of how settlement delay works.**

**Regular (No fixed holidays) example (EDT)**

|Day and time of capture| Sales day closing time| Settlement delay | Day and time of settlement|
|-----| -----| -----| -----|
|Monday at 14:00 EDT| 00:00 EDT| 	5 business days | Next Monday at 00:00 EDT|
|Tuesday at 02:00 EDT| 05:00 EDT| 	5 business days | Next Monday at 05:00 EDT|
|Thursday at 05:00 EDT| 00:00 EDT| 	5 business days | Next Thursday at 00:00 EDT|
|Friday, Saturday, or Sunday| 00:00 EDT| 	5 business days | Next Friday at 00:00 EDT|
|Monday at 17:00 EDT| 00:00 EDT| 	5 business days | Next Monday at 00:00 EDT|

**Example including public holidays (EDT)**
> Public holidays also impact when your funds are settled. The settlement delay increases when a sales day falls on a bank holiday.

|Day and time of capture| Sales day closing time| Settlement delay |Bank holiday| Day and time of settlement|
|-----| -----| ----- |-----| -----|
|Monday at 14:00 EDT| 00:00 EDT| 5 business days |Tuesday and Wednesday|Next Wednesday at 00:00 EDT |
|Thursday at 05:00 EDT | 00:00 EDT| 5 business days |Monday|Next Friday at 00:00 EDT |
|Friday, Saturday, or Sunday | 00:00 EDT| 	5 business days |Monday|Next Monday at 00:00 EDT | 

## Set up bank reconciliation

### Change payment description name

The **payment description name** (also called the **payment statement descriptor**) is the text that appears on your bank statement to help you identify payments made via **Genstore Payments**. By default, **Genstore Payments** uses `GP` + store name for identification, such as `GP0293845`. **Note**: If the payment description name exceeds the allowed character limit or if the store name is incompatible with the system, we will use your store ID instead of the store name.

If you require a customized payment description name, you can modify it in Genstore admin.

#### Steps to modify payment description name

1. In Genstore admin, find the **Payments** menu under **Settings**.
2. Under Genstore Payments, click **Bank** to view your **Payouts statement descriptor** and update it as needed.
3. For U.S. payment description names: Supports uppercase [A-Z], lowercase [a-z], numbers [0-9], and the following symbols: `/` `-` `?` `:` `( )` `.` `,` `'` and space, with a limit of 10 characters.

### Edit customer statement description

When shoppers check their bank statements, they need to be able to easily identify the charges they see. The text that describes charges is known as a transaction  description, statement descriptor, shopper statement, or billing descriptor. If shoppers do not recognize a transaction by its description:

* There is a higher chance your shopper issues a chargeback.<!-- Link to chargeback -->
* You can get a fine from the relevant card scheme related to your chargeback rate.

To prevent these issues, ensure that your transaction description contains your brand or the (chain) merchant name that is most recognizable to the cardholder (as required by the card schemes), and optionally customize your transaction description.

The transaction description supports up to 22 characters (including spaces). You can enter your store name, business name, or another identifier that helps customers quickly recognize you.

Allowed characters:

* Lowercase and uppercase characters: [a-z] [A-Z]
* Numbers: [0-9]
* Special characters: `.`, `,`, `'`, `_`, `-`, `?`, `+`, `*`, and space.

#### Operation steps:

1. In Genstore admin, find the **Payments** menu under **Settings**.
2. Click to activate **Genstore Payments**, then click **Balance account** tab, find the **Customer billing statement** section, and update your statement descriptor.
3. Click **Save**.
