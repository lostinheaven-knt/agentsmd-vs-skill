# Manage markets

Genstore allows you to create multiple markets to assign different settings for different countries and regions, helping you manage your brand experience. A market can include a single country/region or a group of countries/regions. For example, you can create a “North America” market for both Canada and the United States using shared settings. If you want to apply a different setup for Japan, you can create a separate market specifically for that country.

## Add a market

If you want to customize the online store experience for a specific region, you can add a new market on the **Markets** page. For example, you might want to create a market for a group of countries (e.g. North America), or a standalone market for a single country (e.g. Canada).

::: warning

If the new market you create includes countries/regions already assigned to another market:

- Those countries/regions will be automatically removed from the original market and added to the new one.
- If the original market no longer contains any countries/regions, it will be automatically deleted. Any international pricing, domains, subfolders, or custom settings associated with it will also be removed.

:::

### Steps

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. Click **Add market**.
3. Enter a **market name**. This name is for internal reference only and is not visible to customers.
4. Under **Country/Region**, search for and select the countries or regions you want to include. You can add multiple countries/regions to a market.
5. Click **Add market** to confirm.

## Preview a market

You can preview the customer experience for any market—whether active or inactive—using the languages assigned to that market.

### Steps

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. Click into the market you want to preview.
3. Click **Preview**.

## Change primary market

When you first set up your store, Genstore automatically creates a primary market for you. You can change the primary market to a different country or region based on your sales strategy.

Once changed, the new primary market becomes the default market for your store, affecting the default settings for language, currency, shipping, and taxes.
**Note:** The market must be in an active state before it can be set as the primary market.

### Steps

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the **Overview** section, click the active market you want to set as the primary market.
	If the country/region is not yet part of a market, create and activate a new market first. See [Add a market](#add-a-market).
3. Click **More actions**.
4. Select **Make primary market**.
5. Click **Save** to confirm.

After changing the primary market, the original primary market will not be deleted and will remain active.

::: tip Restrictions

- Only markets using a [primary market domain](./global-domains.md) can be set as the primary market.
- Markets using subfolder-based domains cannot be set as the primary market to avoid 404 errors.
- Only active markets can be set as the primary market. Inactive markets cannot be set as the primary market.

:::

## Deactivate a market

By default, newly added markets are active (activated by default). If you do not plan to sell in a specific market yet, you can set it to inactive. This will not delete the market configuration (such as shipping zones) or affect existing orders, and you can reactivate the market at any time.

- Deactivated markets will no longer allow customers to check out.
- If the market uses a top-level domain or subdomain, that domain will redirect to the primary market domain.
- If the market uses a subfolder, its URL will become inaccessible.

### Steps

1. From your Genstore admin, go to **Settings** -> **Market**.
2. In the **Active** section, click the market you want to deactivate.
3. In the status dropdown, select **Inactive**.
4. Click **Save** to confirm.

## Delete a market

You can delete markets that are no longer needed. Deleting a market will prevent customers in that market from placing orders and will invalidate its folder URL, but it will not affect existing orders. Once deleted, the market is permanently removed. **Note:** The target market must be set to _inactive_ before it can be deleted.
### Steps

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the **Inactive** section, click the market you want to delete.
3. Click **More actions**.
4. Click **Remove market**.
5. Click **Confirm** to complete the action.

## Edit countries and regions in a market

You can update a market by adding or removing countries/regions based on your evolving sales strategy.

### Add countries or regions

You can expand an existing market by adding more countries or regions. For example, if your market includes France and Germany and you plan to sell in Italy, you can add Italy to the same market.

#### Steps

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. Click the market you want to edit.
3. In the **Market details** section, click the pencil icon on the right.
4. In the **Edit market** pop-up, search for the country/region you want to add, then select the checkbox next to its name.
5. Click **More actions** -> **Edit market**.
6. Search for the countries/regions you want to add, then check the box next to their names.
7. Click **Save** to confirm.

### Remove countries or regions

You can remove one or more countries or regions from a market. Common use cases include:

1. **Manually remove a country or region**
   - For example, if your “North America” market includes the U.S., Canada, and Mexico, but you want to focus only on the U.S. and Mexico, you can remove Canada.
2. **Automatically remove a country or region when creating a new market**
   - If you create a new market for a country that already exists in another market, Genstore will automatically remove it from the original market.
     - For example, if Germany was part of a broader EU market but now requires a more targeted strategy, you can create a new market for Germany. The system will move Germany into the new market and leave the rest of the countries unchanged.

#### Steps

1. From your Genstore admin, go to **Settings** -> **Market**.
2. Click the market from which you want to remove countries/regions.
3. In the **Market details** section, click the pencil icon on the right.
4. In the **Edit market** pop-up, search for the country/region you no longer want to sell to in this market, then clear the checkbox next to its name.
5. Click **Save** to confirm.
