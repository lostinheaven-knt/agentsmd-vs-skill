# Activate accelerated checkout button

The accelerated checkout (dynamic checkout) button allows customers to complete their purchase directly from the product page, cart drawer, or cart page using saved payment details from **Apple Pay**, **Google Pay**, or **PayPal**.

## Prerequisites

Before enabling the accelerated checkout button, make sure:

- **Apple Pay** or **Google Pay** is enabled in **Genstore Payments**, or your PayPal business account is authorized.
- The customer’s country/region, device, or browser supports accelerated checkout functionality.

## How the button appears

- **When a payment option is available**: The button displays the corresponding payment brand logo, such as **Apple Pay**, **Google Pay**, or **PayPal**.
- **When no payment options are available**: The button displays **Buy now**.
- **When the button is not enabled**: The button does not appear.

## Enable the button

1. Log in to your **Genstore admin account** and go to **Store** -> **Online Store -> Themes**.
2. Under the theme you want to edit, click **Customize**.
3. In the top navigation, select **Products**.
4. Choose the product template you want to edit.
5. In the product information section, click **Buy Button**.
6. In the settings panel on the right, turn on the **Show Dynamic Checkout Buttons** and select where to display the payment brand logos.

## Hide the button

If you want to customize certain product pages or the cart page, you can hide or enable the accelerated checkout button through theme settings.

- **Hide the button on product pages**: If you only want to show the accelerated checkout button on specific product pages, you can configure this in the theme settings. This allows you to selectively display or hide the button based on your product needs.
- **Hide the button in the cart**: If you prefer not to display the accelerated checkout button on the cart page, you can disable this option. The button will then only appear on other selected pages.

## Compatibility

### Theme compatibility

Genstore's official themes fully support the accelerated checkout button. If you are using a third-party theme, compatibility issues may occur. Contact the theme developer for support.

### Payment compatibility

- **Limitations on product variants**:
  Customers cannot use accelerated checkout for different variants of the same product in a single transaction. For example, they can purchase three mugs of the same color but cannot mix colors when using accelerated checkout. If your store has many product variants, consider how this may impact conversions.
- **Does not support certain cart attributes**: The accelerated checkout button does not support the following cart features:
  - Terms and conditions confirmation
  - Applying gift cards or discount codes
  - Selecting a delivery date
