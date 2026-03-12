# Automatic redirection

Genstore allows you to enable automatic redirection so customers are directed to the appropriate market based on their location and browser language. This ensures a more personalized and localized shopping experience.

For example, if a customer is browsing from Canada with their browser language set to French, and the Canadian market has a published French version, the system will automatically redirect them to the Canadian market and display the store in French.

There are two types of redirection: **country/region redirection** and **language redirection**. You can enable them individually as needed.

## Country/Region redirection

When enabled, the system detects the customer’s IP address and redirects them to the corresponding market.

- If the customer’s IP location is not part of any configured market, the system will redirect them to the **primary market** by default.

### Steps

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. In the top-right corner, click **Preferences**.
3. In the **Automatic redirection** section, enable **Country/Region redirection**.

## Language redirection

When enabled, Genstore detects the customer’s browser language preferences and automatically switches to the matching language version—provided that the language is already enabled and published in the selected market (see [Configure languages for a market](./global-market-settings-lang-domain#configure-languages)).

- If the browser language is not enabled or published, the store will default to the market’s primary language.

### Steps

1. From your Genstore admin, go to **Settings** -> **Market**.
2. In the top-right corner, click **Preferences**.
3. In the **Automatic redirection** section, enable **Language redirection**.
