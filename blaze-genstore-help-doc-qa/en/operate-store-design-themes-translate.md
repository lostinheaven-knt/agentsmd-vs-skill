# Theme template translation

In Genstore, building a multilingual online store involves more than translating products, pages, and system messages. You also need to configure translations for various texts embedded in your **theme templates**.

These texts span layout structure, dynamic content, fixed sections, and theme settings. Depending on the content type, the translation path differs in Genstore admin.

## Theme template components

| Type                        | Example texts                                              | Description                                                  |
| --------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Template content**        | Homepage banner titles, product descriptions, button texts | Dynamic content created via the theme content editor         |
| **Template (default text)** | “Add to cart”, “No products”, “Checkout”                   | Built-in texts inside theme files (e.g. `product.liquid`)    |
| **Section groups**          | Header announcements, footer column titles                 | Translatable labels in configurable blocks like header/footer |
| **Static sections**         | Top navigation, “Contact us”, “Follow us”, search messages | Fixed layout areas such as Header, Footer, and Cart          |
| **Theme settings**          | Brand info, color options, font labels, tooltips           | Custom fields in `settings_schema.json` and `settings_data.json` |

## Translate directly using the theme editor

If your store only uses one language, you can edit the default texts directly using the theme editor.

### Steps

1. Log in to your Genstore admin.
2. Go to **Store** -> **Online Store** -> **Themes**.
3. Find your current theme and click `...` -> **Edit default theme content**.
4. In the translation app, select the target category, for example, **Templates**. 
5. Click **View store** to check your edits, then click **Save**.

> ✅ All translations apply to the current language only. This method is recommended for single-language stores.

## Translate using a translation app

If your store supports multiple languages, you need to configure each language separately through the translation app.

### Steps

1. Log in to your Genstore admin and go to **Settings -> Languages**.
2. Find the language you want to edit, then click **Translate** to open the translation app (e.g., Genstore Translate).
3. Choose a category (e.g., **Template content**, **Templates**, **Static group**, etc.).
4. Enter translations manually or click **Auto-translate**.
5. Click **View store** to verify changes, and then click **Save**.
