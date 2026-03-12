# Set pricing preferences

In a multi-market environment, currency conversion may result in inconsistent pricing display. Genstore provides two settings—**local currency** and **price rounding**—to help you present prices more professionally and consistently across markets.

## Enable local currency display

By default:

- **Single-country markets**: The base currency is set to the country’s official currency. If that currency is not supported, the system will fall back to your store’s [base currency](./global-market-settings-product-pricing#set-the-base-currency-for-a-market).
- **Multi-country markets**: The base currency defaults to your store currency, and local currency display is enabled by default.
  - You can [configure local currency individually](./global-market-settings-product-pricing.md) for each market.
  - Or enable local currency in bulk through **Market preferences**.
  - If you prefer to show prices in a single currency or want to configure manual exchange rates, you can disable the **local currency** setting. This ensures a consistent currency is used for all countries in that market.
  - Manual exchange rates are only available when local currency is disabled.

### Steps:

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the top-right corner, click **Preferences**.
3. In the **Local currencies** section, select the market where you want to enable or disable the setting.
4. Click **Save**.

::: tip

If manual exchange rates are already enabled for a market, the local currency setting will be automatically disabled.
 Local currency display is not available for single-country markets.

:::

## Enable price rounding

When selling in multiple currencies, exchange rate conversions may result in uneven price endings for products and shipping fees. Enabling price rounding ensures that prices and fees are rounded up using a predefined rule, resulting in cleaner and more consistent pricing.

### Steps:

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the top-right corner, click **Preferences**.
3. Toggle on **Price rounding**.

Once enabled, prices and shipping fees will be rounded up based on your configured rules. You can define custom rounding rules for each supported currency.
