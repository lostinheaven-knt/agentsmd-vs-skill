# Market types

In Genstore, you can create multiple markets for different countries or regions. According to system logic, there are two types of markets:

- [Primary market](#primary-market)
- [Non-primary market](#non-primary-market)

## Primary market

The primary market is the main country or region where your products are sold. It defines the default customer experience of your store.

- **Default behavior**: Your store’s default settings—such as language, currency, and tax rates—are based on the primary market.
- **Cannot be deleted**: The primary market cannot be deleted but can be replaced with another eligible market.

### Setup recommendation

The primary market defines your store’s default customer experience, and it can include one or more countries/regions.

If your business focus shifts, you can change the primary market to another country/region that better fits your sales strategy. **Note:** Only markets that are active and configured with the primary market domain can be set as the primary market. For detailed steps, see [Change primary market](./global-market-manage-market#change-primary-market).

::: tip Restrictions

- Only markets configured with a [primary market domain](./global-domains.md) can be set as the primary market.
- Markets using subfolder-based domains cannot be set as the primary market to avoid 404 errors.

:::

## Non-primary market

Non-primary markets are used to cover countries or regions outside the primary market. These can include one or more countries/regions and support independent settings for language, pricing, domains, shipping, and more.

- Designed to support international markets beyond the primary market
- Allows localized settings for pricing, language, domains, and logistics

## Markets vs. Countries/Regions

Based on how many countries/regions are included and your sales strategy, markets can be configured in two ways:

- [Single-country market](#single-country-market)
- [Multi-country market](#multi-country-market)

### Single-country market

Use this option when you want to create specific localization strategies for a single country or region. For example:

- Set local pricing, currency, and language for a specific country
- Customize shipping methods or tax rules
- Operate with a dedicated domain or subdomain

#### Example

If Canada is your primary market and U.S. sales are growing, you can create a dedicated market for the United States to improve the localized experience.

#### Currency display

When you create a new single-country market, the system sets the base currency to match that country or region. If that currency is not supported, the store’s display currency will default to the market’s base currency.

### Multi-country market

When multiple countries or regions share similar sales strategies, you can group them into a single market for easier management. For example:

- Use the same product pricing and domain
- Maintain consistency in language and branding

::: tip Best practices

- Avoid grouping countries/regions with very different shipping models or tax rates into a single market.
- For high-performing countries/regions, consider creating separate markets to enable more refined pricing, operations, and promotions.
- Use market data to adjust your market structure dynamically. For instance, you may want to split high-performing countries from a previously combined market.

:::

#### Example

If you’re selling to Germany, France, Belgium, and Italy and want to use a unified pricing and shipping strategy, you can group all four countries into one market for streamlined management.

#### Currency display

When you create a multi-country market, the system sets the base currency for that market and automatically enables local currency display for product prices.
