# Avalara Tax

For countries with complex tax regulations, you can use Genstore's automated tax solution based on the third-party tax platform Avalara. You only need to connect your Avalara account, and then all transaction tax calculations on the platform will be handled by Avalara. You don't need to worry about when, where, or how much tax to collect from customers.

::: tip
Using Avalara Tax requires you to open and configure an Avalara account. We recommend you use Genstore Tax service, which doesn't require account opening and configuration, and is more convenient and faster.
:::

## Open and configure an Avalara account

Before using automated tax, you need to open an Avalara account. You can register an account on the [Avalara official website](https://www.avalara.com/us/en/index.html).

If you already have an Avalara account, log in to the Avalara platform and verify that the following configurations are completed:

### Set up your company and tax collection locations in Avalara

1. Log in to Avalara and navigate to **Settings** -> **Manage companies**.
2. Add your company details.
3. Go to **Settings** -> **Where you collect tax**.
4. Click **Add countries where you report tax** to configure tax collection locations.

### Obtain your API access credentials

1. Log in to Avalara and navigate to **Settings** -> **License and API keys**.
2. Click **Generate new key** to generate your license key.

::: tip

If you have any questions regarding your Avalara account setup, please contact Avalara customer support.

:::

## Connect and configure in Genstore

After obtaining your Avalara account and generated license key, follow these steps to complete the authorization:

1. Log in to Genstore merchant admin, go to **Settings** -> **Tax and duties**.
2. In the **Tax service** module, find **Avalara Tax**.
3. Click **Manage authorization**.
4. Enter your Avalara account credentials and the generated license key.
5. Select the account environment (if you are unsure which environment to use, please consult Avalara support):
   - Select **Production environment** if your account is in the production environment.
   - Select **Sandbox environment** if your account is in the sandbox environment.
6. Click **Test connection**. Only after successful verification can you continue.
7. Select the company entity you configured in the Avalara platform.
8. Select the tax calculation type:
   - **Tax calculation only**: Provides only tax calculation without syncing transaction records to the tax account.
   - **Tax calculation and transaction reporting**: Calculates taxes and syncs transaction information to the tax account, suitable for scenarios requiring tracking of complete transaction tax records for tax reporting or auditing.
9. After completing the settings, click **CLick to authorize**.

## Associate tax codes

The accuracy of automatic tax calculation depends on the correct mapping between products and Avalara tax codes. Genstore supports batch association by category:
1. Log in to Genstore Merchant admin, go to **Settings** -> **Tax and duties**.
2. In the **Tax service** module, find **Avalara Tax**.
3. Click **Manage tax codes**.
4. Verify the tax code association status of products on this page.
5. For non-standard products, such as freight tax codes, you can click **Non-standard product tax code** to configure.

## Enable Avalara Tax for target regions

After completing the global configuration, you need to enable the service for specific shipping regions:
1. Log in to Genstore merchant admin, go to **Settings** -> **Tax and duties**.
2. Select the target tax collection region and enter the tax configuration page.
3. Click the switch icon next to the current tax calculation method, switch to **Avalara Tax**.
4. [Optional] Click **More settings** to customize parameters such as tax display name and remarks.
5. Click **Save**.

## Disconnect

To disconnect Genstore from Avalara:

1. Go to **Settings** -> **Tax and duties**, find **Tax service**.
2. Click **Manage authorization** after the **Avalara Tax** module.
3. Click **Remove Authorization**.

::: warning
After removing the authorization, you will no longer be able to use Avalara automatic tax calculation services. If you need to reconnect to your Avalara account, please follow the above steps to reauthorize.
:::