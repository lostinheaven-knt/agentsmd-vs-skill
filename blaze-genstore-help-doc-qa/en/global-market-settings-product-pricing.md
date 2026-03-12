# Products and pricing

When selling across multiple markets, your customers will see product prices, pay at checkout, and receive refunds in their local currency.

## Key terms

| Term           | Description                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Store currency | This is the default currency used throughout your Genstore admin, independent of any market.<BR /> You can set or change it in **Settings -> General** -> **Display currency**.                                                                                                                                                                |
| Base currency  | The main currency used for pricing and conversion within each market. <BR />All price adjustments and currency conversions are based on the market’s base currency.<BR />If **Show prices to customers in local currency** is enabled, Genstore will use dynamic exchange rates to convert the base currency to the customer’s local currency. |

### Default currency rules for markets

- **Primary market**: Uses the currency set under **Settings -> General -> [Display currency](./start-genstore-account-create-manage#select-store-currency)** as the base currency.
- **Single-country market**: Defaults to the official currency of the country/region.
- **Multi-country market**: Defaults to the store currency as the base currency and enables local currency display by default.
   For example, if your market covers multiple countries in the Americas and Asia, your store’s base currency is USD, and local currency display is enabled, Japanese shoppers will see product prices in JPY.
   **Note:** You can also disable local currency display and show prices using the [market's base currency](#set-the-base-currency-for-a-market).
- **Exchange rates**: By default, dynamic exchange rates are used whenever the market's base currency differs from the store currency. You can also manually manage exchange rates through the **Manage exchange rates** setting. <!-- Documentation not yet available -->

## Set the base currency for a market

### Steps:

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the **Markets** overview page, click the market you want to configure.
3. Click **Products and pricing**.
4. Under **Pricing** -> **Base currency**, select a currency from the dropdown list.
5. Click **Save**.

## Enable or disable local currency display

By default, multi-country markets have local currency display enabled, which shows prices to customers in their local currency. You can disable this if you prefer to display a single currency across the market.

### Steps:

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the **Markets** overview section, click the market you want to adjust.
3. Click **Products and pricing**.
4. In the **Pricing** section, do one of the following:
   - To enable local currency display, check **Show prices to customers in local currency**.
   - To disable local currency display, uncheck this box. Prices will be shown using the market’s base currency.
5. Click **Save**.

::: tip

When local currency is enabled, all conversions use dynamic exchange rates. Manual exchange rates are not supported.

:::

## Set price adjustments

Price adjustments allow you to increase or decrease product prices in a market by a percentage. This is useful for addressing differences in costs, logistics, or market strategy.

For example:

- A **+100%** adjustment doubles the product price.
- A **–50%** adjustment cuts the product price in half.

### Steps:

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. Click the market you want to update.
3. Click **Products and pricing**.
4. Under **Price adjustment**, choose either **Price increase** or **Price drop** from the dropdown.
5. Enter the adjustment percentage.
6. Click **Save**.

## Set fixed prices (optional)

In some cases, you may want to set fixed prices for specific countries or regions. This allows you to maintain stable pricing for key products and avoid fluctuations caused by exchange rates or temporary strategies—for example:

- Long-term promotional pricing in the French market
- Ensuring high-margin items maintain consistent pricing across markets

To set fixed prices for specific countries or regions instead of using dynamic conversion and adjustments, go to [Set product prices by country](./global-set-product-prices-by-country.md).
