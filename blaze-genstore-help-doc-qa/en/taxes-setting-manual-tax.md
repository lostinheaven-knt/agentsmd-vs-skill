# Manual tax

Manual tax is generally suitable for scenarios where the tax rates in the target market countries are relatively simple and stable. You need to configure tax rates that comply with local tax laws for the countries or regions where you need to collect taxes, and manually update the configured tax rates in a timely manner when tax rates change.

## Configure manual tax for target regions

Tax collection regions are deeply linked to your logistics configuration. By default, the system synchronizes countries or regions from your [Shipping and delivery](./operate-fulfillment-shipping-profile-configuration.md) profiles.

1. Log in to the **Genstore** merchant admin, go to **Settings** -> **Taxes and duties**.
2. Find the country or region for which you want to configure taxes, and click to enter the tax rate configuration page.
3. Click the switch icon next to the current tax calculation method to switch to **Manual tax**.

## Set country and regional tax rates

In manual tax mode, you can flexibly configure tax rates based on the administrative hierarchy of the target market. The system uses a "priority override" principle to ensure accurate tax calculation.

### Country tax rate
You can set a country tax rate to establish a unified base product tax rate for the country or region.
- **Application logic**: The set country tax rate will be automatically applied to all secondary administrative regions (such as provinces, states) that do not have individual tax rates set.
- **Applicable scenarios**: Suitable for situations where the entire country/region implements a unified product tax rate.

### Regional tax rate
If product tax rates differ among different administrative regions under a country (such as states in the United States, provinces in Canada), you can set special tax rates for the corresponding regions.
- **Priority principle**: The system will first identify and use the **regional tax rate** when calculating; if no tax rate is set for that region, it will uniformly use the **country tax rate** for calculation.

::: tip

- **Set 0% tax rate**: When a country tax rate is set, if a region is tax-exempt by law or does not collect tax, you must explicitly set a 0% tax rate for that region; otherwise, the system will apply the country tax rate by default.
- **Search function**: If there are many secondary administrative regions, you can use the search box above the list to quickly locate and edit tax rates by entering the region name.

:::

## Set custom tax

If you need to set tax rules that differ from the default tax rate for specific products or shipping fees, you can use the **Tax overrides** feature. For example, alcoholic products may require a separate tax rate, or shipping fees may need to be taxed in specific regions.

### Custom product tax

Suitable for situations where specific products require independent tax rate configurations.

**Operation steps:**

1. Click **Add tax override**.
2. Check **Product**, click **Select products**, and choose the products that need specific tax rates in the pop-up product selection box.
   - **Note:** Products that have already been added cannot be selected again. To re-add them, please first remove them from the existing custom tax.
3. [Optional] If you need to configure tax rates for all regions, check **Add all regions with one click**.
4. Click **Confirm**.
5. The system will return to the current country's tax settings page. For products where you didn’t check **Add all regions with one click**, you can continue adding applicable regions under each product.
6. Click **Save** again to complete the setup.

### Custom shipping tax

Suitable for scenarios where you want to set tax rates for shipping fees.

**Operation steps:**

1. Click **Add tax override**.
2. Check **Shipping**.
3. [Optional] If you want to set shipping tax rates for all regions, check **Add all regions with one click**, and the system will automatically add all configurable regions.
4. Click **Confirm**.
5. The system will return to the current country's tax settings page. If you didn’t check **Add all regions with one click**, you can continue to manually configure the regions applicable to the current shipping rules.
6. After completing the setup, click **Save** in the upper right corner of the page.

## More settings

**Tax display name setting**

You can customize the tax name, which will be displayed on the user checkout page. The default display is **Tax**. You can also enter a **tax description** to help customers understand the tax when placing an order.