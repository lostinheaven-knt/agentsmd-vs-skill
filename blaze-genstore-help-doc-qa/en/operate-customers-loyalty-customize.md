# Store branding

The brand customization page allows you to personalize your store's visual experience by adjusting colors, text, and layouts to match your brand identity. Through this page, you can customize the member panel, launcher, and VIP level cards to provide your customers with a unique shopping experience.

## How to access

1. Log into your Genstore admin.
2. Navigate to: **Store** -> **Customers** -> **Loyalty** -> **Settings**. 
3. Find the **Branding** section.

## Member panel

In the member panel, you can customize your membership panel theme and content to better align with your brand style.

**Steps**:

- Click to enter the editing page
- In the **Theme** section, choose preset color themes or customize button and background colors. Supports solid colors or gradients
- Adjust the display order and visibility of different modules (invitation cards, points, referrals, etc.) through drag and drop

| **Module**      | **Display timing** | **Description**                                              |
| --------------- | ------------------ | ------------------------------------------------------------ |
| Invitation card | Pre-login          | Shows new users the benefits of joining the rewards program, encouraging registration and participation |
| Points          | Post-login         | Explains how to earn and redeem points, promoting user engagement |
| Referrals       | Post-login         | Displays referral rewards, encouraging users to invite new customers |
| VIP             | Post-login         | Shows VIP level benefits and achievement conditions.         |
| Your rewards    | Post-login         | Displays available rewards and details.                      |
| Your activities | Post-login         | Shows user activity history and point changes.               |

Use the preview function on the right to see real-time display effects of all activity widgets. Click **Save** to apply changes after ensuring all settings meet your brand requirements.

## Launcher

You can customize the launcher's style, appearance, and display position.

**Steps**:

- Click to enter the editing page
- Use the top toggle button to enable or disable the launcher
- Customize launcher appearance, including type, text, icon, size, and color
- Set launcher display position, choosing between all pages or specific pages

Use the preview function on the right to see real-time display effects. Click **Save** to apply changes after confirming all settings match your brand requirements.

## VIP tier cards

You can customize VIP tier cards. Click **Customize** under VIP level cards to enter the **VIP level cards** page:

**Customize**:

- Click to enter the editing page
- Click the **edit** icon to modify VIP tier card style and content
- Set card name, background color, font style, and progress bar font size

Use the preview function on the right to see real-time display effects. Click **Save** to apply changes after ensuring all settings align with your brand requirements.

## Multilingual support

Genstore Loyalty program supports multilingual display, helping you better serve customers from different language backgrounds and enhance their experience and engagement.

You can translate all merchant-customized content, including point earning methods, reward names, VIP tier names, and loyalty panel messages. Fixed system content will be automatically translated and adapted.

### Add languages and auto-translate

**Steps**

1. Log in to your Genstore admin.
2. Go to **Store** -> **Customers** -> **Loyalty**.
3. Click **Settings** and under the **Branding** section, click **Languages** to open the translation configuration page.
4. Click **Add language**, and select one or more languages from the list. Currently supported:
    - English (en-US)
    - Simplified Chinese (zh-CN)
    - Traditional Chinese (zh-TW)
    - Spanish (es-ES)
    - Malaysian (ms-MY)
5. Click **Save**. The system will automatically initialize default translations for the selected languages.

### Edit translation content

After adding a language, click the pencil icon in the language list to open the translation editor. You can review and adjust the displayed content for each module. For example:

1. Expand the **Welcome (Display only before sign in)** section.
2. Edit fonts, font size, and contents.
3. Preview the logged-in and logged-out display in real time.
4. Click **Save** in the top-right corner to apply your changes.

::: tip

Some fields contain dynamic parameters, such as `{Store name}`, which will be automatically replaced with your store name on the storefront.  Please do not remove or alter the parameter format, as this may affect proper display.

:::

### Additional content management

In addition to the **Settings -> Languages** module, some loyalty-related fields must be managed within their specific modules:

| Field type                     | Configuration path                                       |
| ------------------------------ | -------------------------------------------------------- |
| Loyalty panel content          | Settings -> Branding -> Panel                            |
| Point label                    | Settings -> More settings -> General -> Point label      |
| Earning/redeeming method names | Points tab -> Earn/redeem section                        |
| VIP tier names                 | VIP tab -> VIP tier management                           |
| Referral reward names          | Referrals tab -> Referrer/Friend's reward option section |

### Set default language

The default language is used when a customer's selected language is not available. We recommend setting this to match your store's primary language.

**Steps**

1. Navigate to **Store** -> **Customers** -> **Loyalty**, then click **Settings** -> **Branding** -> **Languages**.
2. In the language list, find the desired language and toggle the **Default** switch.

::: tip

The current default language is English (en-US), which cannot be deleted.  
To delete it, you must first set another language as the default.

:::

### Delete a language

To remove a previously added language:

- Click the trash icon next to the language in the list.
- Confirm the deletion when prompted.

**Note:**  
Be cautious when deleting a language that is already active. If customers switch to that language in your store, loyalty content may not display correctly.