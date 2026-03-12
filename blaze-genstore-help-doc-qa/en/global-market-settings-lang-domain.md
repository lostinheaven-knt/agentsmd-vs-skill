# Language and domains

In Genstore, you can configure the language and domain for each market to provide a localized browsing experience for customers in different countries or regions.

There are three types of domain configurations for markets:

- **Use primary market settings**
  - Markets that use the primary market’s configuration will share the same language and domain settings.
  - By default, new markets inherit the language and domain settings of the primary market.
- **Use subfolder domains**
  - You can assign subfolder-based URLs to each market. The URL structure follows the format:
	 `[primary domain]/[country/region code]/[language code]`.
  - You can activate multiple languages for each market, with each language assigned its own subfolder.
  - For example:
	- If your primary market (U.S.) uses the domain `example.com`, the Canadian market could use `example.com/ca`.
	- If you enable French for Canada, the URL would be `example.com/ca/fr`.
- **Use custom domain or subdomain**
  - You can assign a custom domain (e.g., `example.ca`) or subdomain (e.g., `ca.example.com`) to each market.
  - Before assigning, go to **Settings** -> **Domains** to connect the desired domain or subdomain.
  - Once connected, you can assign the domain to a market and configure the associated languages.

> If a domain or subdomain is removed, customers visiting that market’s URL will see a 404 error page.

::: tip

The primary market always uses the primary domain and cannot be changed.
 To change the primary market domain, go to **Settings** -> **Domains** and set a new domain as the primary domain.

:::

### Steps to assign domain and language

1. From your Genstore admin, go to **Settings** -> **Markets**.
2. Click into the market you want to configure.
3. Under **Market settings**, click **Languages and domains**.
4. Click **Manage domains**, then choose your desired domain setup: subfolder, custom domain or subdomain, or use the primary market’s configuration.

## Configure languages

You can assign one or more languages to the selected market.

### Steps

1. Next to the domain, click **Add language** -> **Add more languages**.
2. On the **Languages** page, click **Add language**.
3. Select the language you want to add and click **Next**.
	Genstore will prompt you to install the Translate app to help localize your store.
4. Choose the market to assign the language to and click **Finish**.
5. Once added, the new language will appear under **Languages** -> **Unpublished**. To publish it, click **...** -> **Publish**.
	**Note:** You can also edit which markets the language is assigned to from this page.
6. Return to the market and open the **Language and domains** section. You’ll see the new language has been added.
7. To make additional changes, click **...** next to the language to delete it or set it as the store’s default language.

::: tip
If a market uses the Primary Market domain configuration, its language settings will also follow the Primary Market and cannot be configured independently. To manage a specific market's language separately, please set its domain to use a subfolder or subdomain.
:::