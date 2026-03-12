# Find and submit your sitemap

Every Genstore site automatically generates a `sitemap.xml` file that includes links to all your products, pages, blog posts, and more. These links help search engines crawl and index your website, making your content more discoverable in search results.

To speed up indexing, we recommend submitting your sitemap to Google Search Console. This allows search engines to discover your new pages more quickly and improves the overall visibility of your website.

Crawling and indexing times may vary depending on your site’s structure and content update frequency. Google does not guarantee how long the process will take. You can check the submission status and learn more in the [Google Search Console Help Center](https://support.google.com/webmasters/answer/7474347?hl=en).

## Before you begin

- You need a **Google Search Console account**

## Locate your sitemap file

Genstore automatically generates a `sitemap.xml` file at the root of your domain. For example: `example.com/sitemap.xml`.

This file updates automatically and includes child sitemaps for all products, pages, blogs, and more—no manual updates required. If you’ve enabled multiple languages or configured multiple domains for international targeting, each domain will generate its own sitemap.

If you have multiple domains but are not using internationalization, we recommend redirecting all secondary domains to your primary domain to avoid duplicate indexing or confusion about page ownership.

## Verify site ownership (Google Search Console)

Before submitting your sitemap, you need to verify that you own your website through [Google Search Console](https://search.google.com/search-console/welcome?utm_source=about-page&pli=1).

::: tip

Make sure your website is publicly accessible before verification. If your store is password-protected, [temporarily disable the password](./operate-store-design-preference#turn-off-password-protection) first.

:::

### Verification steps

1. Go to [Google Search Console](https://search.google.com/search-console/welcome), click the **≡** icon, and select **Add property** from the dropdown menu.
2. In the **Select property type** dialog, select **URL prefix** and enter your full domain, including `https://`.
3. Click **Continue**.
4. In the **Verify ownership** window, choose **HTML tag** or another method you’re comfortable with.
5. Under **HTML tag**, click **Copy** to copy the full meta tag to your clipboard. Be sure to include the entire tag, including `<` and `>`. For example:
	```text
	<meta name="google-site-verification" content="IV7BPLESttSpBdxSWN1s4zlr4HIcuHkGQYmE3wLG59w" />
	```
6. Log in to your Genstore admin and go to **Store -> Online Store -> Themes**.
7. Find the theme you want to edit, click the **...** button to open the actions menu, and then click **Edit code**.
8. In the **Layout** section, click `theme.liquid`.
9. Paste the meta tag you copied in step 5 directly below the opening `<head>` tag.
10. Click **Save**.
11. Return to Google Search Console and click **Verify**.

::: tip

If the verification fails the first time, wait about 15 minutes and try again.

:::

## Submit your sitemap

1. After verification, open your Google Search Console dashboard.
2. *(Optional)* If you have multiple root domains under your account, use the dropdown at the top to select the correct domain.
3. In the left-hand menu, go to **Index -> Sitemaps**.
4. In the **Add a new sitemap** section, enter `sitemap.xml`. The system will auto-complete your full URL (e.g., `https://example.com/sitemap.xml`).
5. Click **Submit**.
