# Customize with code

This section is intended for merchants or developers with front-end development experience. By editing the theme code, you can customize your store’s page structure, styles, and functional components—unlocking advanced branding and layout control.

## How to access the code editor

1. Log in to your Genstore admin.
2. Go to **Store** -> **Online Store** -> **Themes**.
3. Find the theme you want to edit, click the `...` button to open the menu, and select **Edit code**.
4. In the file tree on the left, choose the `.liquid` or `.json` file you want to modify.
5. Make the necessary changes in the code editor.
6. Click **Save** when you’re done.

### Theme file structure

The theme’s code is organized into several key directories based on their purpose and usage:

|Directory|Description|
|---|---|
|**`layout`**|- Contains layout files for global structure, only supports `.liquid` files  <br>- Typically includes files like `theme.liquid`|
|**`templates`**|- Holds template files for different page types (e.g., `product.json`, `collection.json`) <br>- Each page type has a corresponding `liquid` template to define its layout and content rendering logic|
|**`sections`**|- Reusable page sections, supports both `.json` and `.liquid` formats  <br>- Common examples include `header.liquid`, `footer.liquid`  <br>- JSON files support market-specific configuration via naming|
|**`blocks`**|- Allows merchants to dynamically add functional components (“blocks”) to pages  <br>- Provides higher flexibility and customizability|
|**`snippets`**|- Reusable code blocks, mainly `.liquid` files  <br>- Cannot contain `schema` blocks  <br>- Ideal for pure display components like product cards or labels|
|**`assets`**|- Static assets such as CSS, JavaScript, images, and fonts  <br>- Examples include `theme.css`, `custom.js`, `logo.png`, etc.|
|**`locales`**|- Contains language translation files in `.json` format  <br>- Used for multilingual store support with localized text for each language|

## Editor keyboard shortcuts

The following shortcuts are supported in the theme code editor to help you work more efficiently:

|Action|Windows / Linux|macOS|
|---|---|---|
|Save|Ctrl + S|Cmd + S|
|Find|Ctrl + F|Cmd + F|
|Replace|Ctrl + H|Cmd + H|
|Undo|Ctrl + Z|Cmd + Z|
|Select all|Ctrl + A|Cmd + A|
|Copy|Ctrl + C|Cmd + C|
|Cut|Ctrl + X|Cmd + X|
|Paste|Ctrl + V|Cmd + V|
|Format code|Ctrl + Shift + I|Cmd + Shift + I|
|Comment/Uncomment|Ctrl + /|Cmd + /|
|Go to line|Ctrl + G|Cmd + G|
