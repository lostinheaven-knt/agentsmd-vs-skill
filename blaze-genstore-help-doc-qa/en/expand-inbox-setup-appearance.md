# Appearance settings

This page is used to configure the **visual style and entry text** of your website's customer service chat window (the entry point for both the AI Agent and human support). A well-designed appearance can significantly improve the rate at which customers initiate inquiries.

## How to access
1. Log in to the Genstore admin, and click **Sales Channels** -> **Inbox**.
2. Click **Enter** besides the **Help desk**.
3. In the left sidebar menu, click **Appearance** under **Settings**. From here, you can:
  - Modify the [Welcome message](#welcome-message)
  - Edit the [Chat entry text](#chat-entry)
  - Adjust the [Inbox widget position and size](#widget-style)

## Welcome message
This is the introductory text customers see immediately after opening the chat window.
* **Purpose**: To break the silence and guide customers to start a conversation.
* **Setup tips**:
    * Keep it brief (1–2 lines) and use a friendly tone.
    * Include brand personality, e.g., "Hi there! 👋 How can I help you today?"
    * Use emojis to make the interface feel more approachable.

## Chat entry
Configure the text displayed on the chat card when the bubble is not yet expanded.

* **Title**: We recommend using the variable <span v-pre> `{{ AI Agent name }}` </span>. The system will automatically pull the name you defined in the AI settings to create a more personalized identity, e.g., "Ask `Olivia` for help."
* **Subtitle**: A short sentence explaining your service capabilities, e.g., "Our AI agent and team are here to help."

## Widget style
You can adjust the physical attributes of the Inbox button to match your website’s design and avoid blocking core page content (such as checkout buttons).

| Setting | Options | Recommended scenario |
| :--- | :--- | :--- |
| **Inbox bubble size** | Small / Medium / Large | Default is **Large**; adjust based on your page layout. |
| **Horizontal position** | Left / Right | **Right** is recommended for most sites to suit right-handed navigation. |
| **Vertical position** | Low / Medium / High | Set to **High** if you have cookie banners or other floating elements at the bottom. |

## Real-time preview
The store preview area in the center of the page updates instantly. You can also click the **Mobile** icon in the bottom floating toolbar to switch between desktop and mobile previews. Once you are satisfied with the size and positioning, click **Publish** to apply the changes.

::: tip
If you want to display a "Quick Questions List" in the preview, you can configure this in the [FAQs section](./expand-inbox-setup-faqs.md).
:::