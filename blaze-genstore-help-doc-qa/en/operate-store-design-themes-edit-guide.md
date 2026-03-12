# Customize with theme editor

Genstore provides a visual theme editor that allows merchants, operators, and designers to adjust the layout, content, and overall visual style of their store—without writing any code.

## How to access

1. Log in to your Genstore admin and go to **Store** -> **Online Store** -> **Themes**.
2. Click the **Customize** button next to your target theme.
3. Click the dropdown in the top page selector to choose a page type (e.g. Home, Product, Collection).
4. For some pages, you can further select a specific resource or create a new theme.
5. The preview will refresh automatically to display the selected theme for editing.

The theme editor includes two main areas:

- [Top toolbar](#top-toolbar): for page navigation, preview, saving changes, and exiting the editor
- [Main workspace](#main-workspace): for managing page structure, visual styles, and app components 
## Top toolbar

Located at the top of the editor, the toolbar lets you manage your theme, preview pages, and perform actions.

| Feature           | Description                                                                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Theme name        | Displays the name of the theme currently being edited                                                                                           |
| Theme status      | Shows the theme status <br />- 🟢 Live view, for published themes<br />- ⚪ Draft, for unpublished ones                                          |
| Version | Version information for the current theme, and access to the [Code editor](./operate-store-design-themes-code-editor.md) |
| Market switcher   | Select target market to customize (for [multi-market stores](./global-market-manage-market.md))                                                     |
| Template switcher | Select a page type to edit, such as home, product, collection, or custom. Some pages (like product pages) support choosing a specific template. |
| Undo / Redo                                                 | Undo or redo unsaved changes made during the current editing session.<BR />- Only applies to changes not yet saved in the current session.<BR />- When no action is available, the button will be grayed out and disabled. |
| Device preview                                              | Preview your page on desktop, mobile, or full-screen to ensure a seamless experience on any device. |
| Preview           | Opens a live preview of the current theme                                                                                                   |
| Save              | Save all modifications (recommended frequently)                                                                                                 |
| Publish           | For draft themes, you can publish them directly and set them as your store theme.                                                                                                           |
## Main workspace

The main editing area consists of three main parts:

| Section                 | Description                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Function navigation bar | Located on the far left, it provides access to page template management, design, style design, theme design, and app embeds. |
| Sidebar panel           | Displays page structure, content modules, or style settings based on the selected function.                                  |
| Live preview area       | Shows a real-time preview of the selected page on the right. Supports switching between languages, markets, and devices.     |
## Navigation bar

The function toolbar is located on the far left of the editor interface. It contains five vertically arranged icons, each representing a different editing module:

- **[Page management](./operate-store-design-themes-edit-guide-page-manage.md)**: Used to centrally manage the creation and assignment of various page templates. Supports fuzzy search for unassigned pages and quick switching between templates for products, pages, blogs, and more to improve configuration efficiency.
- **Page design**: Used to manage and edit the structure and content of specific pages such as the homepage, product pages, and collection pages. You can add, delete, or rearrange sections and blocks within the page.
- **Style design**: Controls global visual styles that affect all pages, including color schemes, typography, animations, and more.
- **Theme design**: Used to configure the overall appearance of your website, including logo, brand details, social links, cart behavior, and [custom CSS](./operate-store-design-themes-edit-guide-page-css.md) to create a consistent brand identity.
- **App management**: Allows you to integrate app components from Genstore or third parties into your pages, enabling advanced features like promotions, recommendations, and forms.

## Contextual sidebar

The side panel is located on the left side of the main editor area. It dynamically updates based on the module selected in the function navigation toolbar and displays the corresponding settings and content structure.

### Page management
When **Page Management** is selected, you can view all page types supported by the current theme in the side panel, as well as manage template configurations and assignments for each page.

The Page Management area in Genstore consists of the following components:
- **Page list**: Displays all page types that support templates in groups, such as Home, Products, Collections, Blogs, Search, 404, etc. Certain types (e.g., Products, Pages, Blog Posts) can be expanded to view assigned pages and template details.
- **Template creation & switching**: Supports creating multiple templates for a page type. Click **Create template** to add a new template and assign it to specific pages, enabling differentiated content displays.
- **Template assignment status**: View the number of pages assigned to each template. You can click to quickly jump to a preview or edit the template.
- **Search & filter**: Use the search bar at the top to search by template name, page name, or unassigned pages to improve management efficiency.

### Page templates

When **Page design** is selected, the sidebar panel shows a breakdown of the page structure.

Genstore pages have three default areas:

| Area name                                                    | Description                                                                             |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| [Header](./operate-store-design-themes-edit-guide-header.md) | Contains logo, nav bar, announcement, search, cart, etc. Supports apps or Liquid blocks |
| [Template](./operate-store-design-themes-edit-guide-page.md) | Main content area: products, text/images, blogs, etc.                                   |
| [Footer](./operate-store-design-themes-edit-guide-footer.md) | Contains copyright, payment methods, social links, and subscription forms               |

#### Sections and blocks

Each page is built from multiple **sections**, and each section can contain one or more **blocks**.

- **Sections** are large layout containers like banners or product carousels
- **Blocks** are smaller units like text, buttons, or media items that live inside a section

This modular structure allows flexible customization and brand consistency.

**Section features**

| Feature  |  Description |
|---|---|
|Section list|Shows all sections used on the current page|
|Add section|Insert new functional areas like banners or collections|
|Drag to sort|Rearrange section order by dragging|
|Hide / Show|Temporarily disable or enable a section|
|Delete section|Permanently remove a section (requires saving)|

**Block features**

Some sections support multiple blocks:

| Feature  |  Description |
|---|---|
|Add block|Add elements like text, buttons, or media within a section|
|Drag to sort|Rearrange block order|
|Delete block|Remove a block without deleting its parent section|

### Style design

When **Style design** is selected, you can define a unified visual style for your entire site, including color schemes, typography, button styles, and layout settings to ensure a consistent brand experience.

**Main configuration options include:**

- **Color schemes**: Supports switching between light and dark modes, and allows you to define primary, secondary, accent, neutral, and background colors individually.
- **Typography**: Adjust heading and body text sizes, weights, and spacing to ensure clear visual hierarchy and readability.
- **Component styles**: Configure the appearance of visual elements such as icons, buttons, input fields, and cards (e.g. product, collection, blog cards).
- **Page layout**: Set overall spacing and layout rules for consistent display across different screen sizes.
- **Animations and interactions**: Configure visual effects for scroll behaviors, button hover states, drawer popups, and other UI feedback.

All settings apply globally to your storefront theme and are reflected in real time in the preview panel, helping you quickly evaluate the visual impact.

### Theme design

When **Theme design** is selected, you can configure global visual and behavioral settings for your website, covering brand identity, shopping experience, and custom styles to create a consistent storefront appearance.

**Main configuration options include:**

- **Logo and favicon**: Upload your store’s logo and browser icon (favicon), with optional width adjustments for desktop layouts.
- **Brand information**: Enter your store name and description to be used in supported theme modules.
- **Social media**: Add links to your social platforms (e.g. Instagram, Facebook), which can be displayed in the footer or other designated areas.
- **Search behavior**: Configure how the search bar works, including autocomplete and content source settings.
- **Currency formatting**: Set default currency display rules, including symbol position and decimal precision, for consistent price presentation.
- **Cart settings**: Customize the cart icon, layout, and interaction behavior during the shopping process.
- **[Custom CSS](./operate-store-design-themes-edit-guide-page-css.md)**: Add global CSS styles to further personalize your storefront appearance and meet specific brand design requirements.

### App management

Click the bottom icon to open the app embedding interface. You can integrate Genstore apps or third-party widgets into specific page areas to enhance marketing, form capture, recommendations, and more.

## Live preview area

The right panel displays a real-time preview of your template across different devices and languages.

- **Market/currency switch:** If multiple markets are enabled, you can switch regions and currencies.
- **Language switch:** Use the language dropdown to preview how the page appears in different languages.
    - After switching languages, the preview will reflect localized product titles, tags, price formats, etc.
    - **System fields** (e.g., "Sold Out", "Add to Cart") use platform-provided default translations.
    - **Merchant content** (e.g., product titles and descriptions) must be manually translated in the [Translation Editor](./operate-store-design-themes-translate.md).
    - Fields without translations will display content in the default language.
- **Real-time updates:** Supports responsive layouts and auto-refresh for instant visual feedback.

