# Genstore tax

Genstore tax is a fully automated tax engine designed to help merchants navigate the complexities of global tax compliance. The system automatically identifies regional tax laws to calculate sales tax, value added tax (VAT), and shipping tax in real-time. This automation reduces manual errors, ensures compliance, and allows you to focus on scaling your business.

## Service fees and billing rules
Please review the following fee structure before enabling Genstore tax:

| Subscription plan | Lite | Growth | Scale |
| :---------------- | :--- | :----- | :---- |
| Monthly Free Credits (Monthly Plan)  | 15   | 60     | 180   |
| Annual Credit Allowance (Yearly Plan)  | 180  | 720    | 2160  |
| Additional transaction fee | $0.30 | $0.30 | $0.30 |

* **Per-transaction fee**: $0.30 USD per calculation.
* **Transaction logic**: Each completed order counts as one transaction. If an order is returned or refunded, the system must recalculate the tax; this is treated as a **new transaction** and will incur an additional $0.30 fee.
* **Settlement**: Fees are non-refundable and are billed automatically to your Genstore account. Deductions occur on your billing date or upon reaching your account's billing threshold.
* **Billing transparency**: Track your expenses via **Settings** -> **Billing**. In **Past bills**, click to view the billing details, and you can find this information under **Genstore tax calculation fee**.
> **Example**: For stores on the Lite plan, your first 15 transactions each month are free. If you process 100 transactions, the tax service fee is calculated on the remaining 85 transactions at a rate of $0.30 each, totaling $25.50.

::: tip
* By enabling Genstore tax, you agree to the service fee terms.
* Genstore tax requires an active store subscription; it is disabled by default for unsubscribed stores.
* Development stores do not currently support Genstore tax services.
:::

## Configuration workflow

Genstore tax requires manual activation. To enable accurate tax calculations, please enter your company details during activation. You must also complete the configurations below to ensure regulatory compliance and risk coverage in your specific region:

### 1. Set a manual fallback tax rate
Genstore tax relies on real-time API calculations. To prevent checkout failures during rare network interruptions or service fluctuations, we strongly recommend setting a **manual fallback rate** for each tax region.

#### Setup steps:
1.  Navigate to **Settings** -> **Taxes and duties** in your Genstore admin.
2.  Select the target tax region to open the configuration page.
3.  Click the **switch icon** next to the current method and change it to **Manual tax**.
4.  Enter your fallback rates (e.g., product tax, custom taxes).
5.  *[Optional]* Click **More settings** to customize tax display names or add merchant notes.
6.  Click the **switch icon** again to return the method to **Genstore Tax**.
7.  Click **Save**.

### 2. Enable Genstore Tax for specific regions
To assign Genstore tax to a specific shipping zone:
1.  Go to **Settings** -> **Taxes and duties**.
2.  Select your target region.
3.  Ensure the calculation method is set to **Genstore Tax**.
4.  Click **Save**.

### 3. Secondary jurisdiction management (US and Canada)
For regions with complex local tax laws, you can manage tax collection at the state or provincial level.

::: tip
* This feature is currently exclusive to the **United States** and **Canada**.
* For all other countries, Genstore tax applies a uniform calculation across the entire national territory.
:::

#### Operational steps:
1.  Go to **Settings** -> **Taxes and duties** and select a region (e.g., United States).
2.  Under **Tax area**, manually toggle the switch for each state or province (e.g., enable for California, disable for New Hampshire).
3.  To manage all regions at once, use the **master switch** at the top right of the list.
4.  Click **Save**.

## Product tax code management
Accurate automation depends on correctly mapping your products to tax codes:

* **Category mapping**: Map tax codes directly to "product categories." Genstore will recommend the appropriate code based on the category, saving you from manual per-product assignments.
* **Default mapping**: Products without a specific code are assigned **P0000000** (Standard tangible personal property) by default. Review these regularly to ensure you aren't over-calculating tax on exempt items.
* **Non-standard items**: For specialized items like taxable shipping/freight, click **Non-standard product tax code** to configure.

**Note**: If the system detects unmapped categories, a warning banner will appear in your admin. Click **View** to resolve these mappings immediately. When in doubt, consult a tax professional.

## Storefront and customer experience
To ensure transparency and trust, estimated taxes are displayed during the checkout flow:

* **Tax-exclusive pricing**: Customers see the "Tax" line item with a "**?**" tooltip. Hovering over the icon displays your custom tax description. The final tax is finalized upon checkout completion.
* **Tax-inclusive pricing**: No additional tax is added at checkout. A notification appears below the total stating, "Tax is included in the product price."

## Appendix: Unsupported regions
Genstore tax is currently unavailable in the following 13 jurisdictions. If you have a tax nexus in these areas, you **must** configure manual tax rates to process transactions:

* **AQ**: Antarctica
* **AS**: American Samoa
* **BV**: Bouvet Island
* **EH**: Western Sahara
* **FM**: Micronesia
* **GU**: Guam
* **HM**: Heard Island and McDonald Islands
* **MH**: Marshall Islands
* **MP**: Northern Mariana Islands
* **PW**: Palau
* **PR**: Puerto Rico
* **UM**: U.S. Minor Outlying Islands
* **VI**: Virgin Islands (U.S.)