# Manual tariff settings

Enable tariff settings in your store to manually configure how tariffs and import taxes are calculated. This ensures that international customers prepay these fees at checkout, preventing unexpected charges upon delivery.

## Important reminders

- **Tariff rates are not tax advice** – tariff calculations are for reference only. Tax regulations vary by country/region, so consult local tax experts or customs authorities to ensure compliance.
- **Verify compliance** – Some countries/regions offer tariff exemptions or have minimum taxable thresholds. Check local regulations to ensure your settings meet requirements.
- **Keep rates up to date** – Tax policies can change. Review and update your settings regularly to maintain accuracy.

## Enable prepaid tariff

Before manually configuring tariffs, enable **prepaid tariffs** to ensure customers pay these fees at checkout. When enabled, tariffs and import taxes are included in the order total and handled by the carrier.

:::tip

Before configuring tariff, confirm that your carrier supports **DDP (Delivered tariff Paid)** to ensure smooth collection and payment of tariff. Also, verify that your tariff rates align with the carrier’s process.

:::

### How to enable

1. Log in to the **Genstore admin** and go to **Settings** -> **Taxes and duties**.
2. Switch to **Manual tax** collection method.
3. Toggle on the **Duties and import taxes** section.
4. Check **My carrier supports prepaid tariffs** so tariffs are calculated at checkout.
5. Click **Turn on tariff settings**, then select shipping countries/regions in the new window. Each location has different tariff calculation rules, so configure rates accordingly.

## Edit tariff settings

Click **Edit** next to the desired country/region to modify tariff calculation methods and rates.

### Choose a tariff calculation method

Select a method based on your product type and target market:

#### Calculate based on CIF (Cost, Insurance, and Freight)

Use this method when tariffs are calculated on **product cost, shipping, and insurance**.

**Formula:**

```text
Tariff rate × (Product cost + Shipping)
```

**Steps:**

1. Select **CIF** as the tariff calculation method.
2. Enter tariff rates and additional costs (e.g., shipping, insurance) for each location.
3. Save your settings.

#### Calculate based on FOB (Free on Board)

Use this method when tariffs are based only on the **product’s sale price**, excluding shipping and insurance.

**Formula:**

```text
Tariff rate × Product cost
```

**Steps:**

1. Select **FOB** as the tariff calculation method.
2. Enter the product’s sale price and set the tariff rate for each location.
3. Save your settings.

#### Calculate based on weight

Use this method when tariffs are charged **per unit weight or volume** rather than price.

**Formula:**

```text
tariff rate × Product weight
```

**Steps:**

1. Select **weight-based** as the tariff calculation method.
2. Enter the tariff rate per weight unit and ensure product weight details are accurate.
3. Save your settings.

## Set default and custom tariff groups

### Set a default tax group

Apply a single tariff rate to all **unspecified** products.

**Steps:**

1. In the tariff settings, select **Default tax group**.
2. Enter the tariff rate and calculation method.
3. Save your settings. The default rate applies to all products without specific configurations.

### Create custom tax groups

Use custom tax groups for products that require different tariff rates (e.g., exemptions or unique tariffs).

**Steps:**

1. In **Custom tax groups**, click **Add tax group**.
2. Name the tariff group for easy reference.
3. Select a tariff calculation method (CIF, FOB, or weight-based) and set tariff rates.
4. Save your settings. The selected products will follow this tariff group’s rates.

### Customize tax display

You can rename tariff fees and add notes for better management.
