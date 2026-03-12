# Genstore copyright notice

In your store theme footer (usually at the bottom-left corner), the system will display content similar to the following by default:

```
© 2025, {your-store-name} Made with Genstore AI
```

This copyright notice identifies your store’s copyright information and indicates that it is powered by Genstore.

## Why it matters

- **Copyright statement**: Displays ownership information to your customers.
- **Platform attribution**: Shows that your store is powered by Genstore.
- **Customization**: By editing the theme code, you can remove or modify the default text so the footer better fits your brand.

## How to remove the copyright notice

::: warning

This action involves editing code. Be sure to back up your theme before making changes.

:::

1. In your Genstore admin, go to **Store -> Online Store -> Themes**.
2. Click the **...** icon next to the theme you want to edit, then select **Edit code** from the dropdown menu.
3. In the file list on the left, expand the **sections** folder and locate the `footer.liquid` file.
4. Use the search function to find the code block  `footer__copyright`.
5. Delete or comment out that code block:
    - **Delete**: Remove the code directly.
    - **Comment out**: Wrap the code with `{% comment %}` and `{% endcomment %}` to hide it.
6. Save the file, then refresh your storefront to confirm that the copyright notice has been removed.

::: tip

- Removing the copyright notice does not affect store functionality—it only changes the storefront display.
- To replace it with custom text, insert your own copyright information after removing the default one.
- Editing code comes with risks. We recommend testing changes on a duplicate theme before applying them to your live theme.

:::