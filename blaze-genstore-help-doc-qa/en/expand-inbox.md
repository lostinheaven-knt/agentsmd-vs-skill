# Genstore Inbox

**Genstore Inbox** is a real-time customer service tool designed specifically for e-commerce merchants. It supports the full conversation flow from pre-sale inquiries to post-sale support. Customers can initiate conversations directly from your storefront, and you can either respond manually or enable the **[AI Agent](./expand-inbox-ai-intro.md)** for automated replies.

In addition to the basic chat feature, Inbox integrates with FAQs, response templates, duty schedules, and the AI Agent module to help merchants improve service efficiency and reduce manual workload.

## Feature overview

| Module name | Description | AI Agent integration |
| :--- | :--- | :--- | 
| [Appearance settings](./expand-inbox-setup-appearance.md) | Used to set up welcome message and conversation entry copy for the Inbox widget homepage | No | 
| [Localization](./expand-inbox-setup-localization.md) | Displays localized content for different countries/regions, including welcome messages, FAQs, etc. | No | 
| [Enable customer service chat entry](#enable-inbox) | Displays chat entry in the bottom right corner of the store, allowing customers to initiate conversations | No |
| [Content preparation - FAQs](./expand-inbox-setup-faqs.md) | Sets up common questions and displays them on the chat widget homepage as a basis for AI replies | **Can be referenced by AI** | 
| [Content preparation - Response templates](./expand-inbox-setup-template.md) | Configures standard reply templates that support staff can quickly insert | No | 
| [Service hours scheduling](./expand-inbox-setup-schedule.md) | Sets up staff online hours to control whether AI takes over during non-working hours | **Works with AI** | 
| [AI Agent](./expand-inbox-ai-intro.md) | Automatically replies to customer questions, supporting personalized training and multiple data sources | **Core AI module** | 
| [Conversation handling/grouping](./expand-inbox-setup-group.md) | Configures conversation routing rules and manages backend replies | No | 

## Permission preparation

To ensure your customer service team can use Inbox smoothly, you need to assign corresponding permissions to your employees.

**Path**: Genstore Admin -> **Settings** -> **User and permissions** -> **Manage roles**

After creating a role, check **Inbox** in the permission configuration to further refine:

| Permission item | Description | Suggested application scenario |
| ---------- | ---------------------- | ------------ |
| Conversation management | Can view and reply to customer messages | Daily customer service | 
| Inbox administrator | Has all configuration and viewing permissions | Store owner, supervisor | 

## Enable Inbox

1. Log in to your Genstore admin.
2. Go to **Sales channels** -> **Inbox**.
3. Toggle the **Live chat** switch to enable.

Once enabled, a live chat icon will appear on your storefront, allowing customers to start conversations.

## Quick start

Once you have enabled Inbox, we recommend following these three stages to optimize your setup and ensure the best customer service experience:

### Stage 1: Brand and interface customization

* **[Appearance settings](./expand-inbox-setup-appearance.md)**: Customize the brand colors, welcome messages, and entry text of your chat window to ensure the interface aligns with your brand identity.
* **[Multi-language support](./expand-inbox-setup-localization.md)**: Provide localized interfaces for customers from different countries and regions to eliminate communication barriers.
* **[Chat entry point](./expand-inbox-setup-appearance.md#2-Entry-Point)**: Confirm that the chat icon is correctly displayed on your storefront and positioned where it is most accessible to customers.

### Stage 2: Content and service readiness

* **[FAQs (Frequently asked questions)](./expand-inbox-setup-faqs.md)**: Input high-frequency inquiries regarding shipping, returns, and exchanges. This content is displayed directly to customers and serves as the core knowledge base for the **AI Agent**.
* **[Quick replies](./expand-inbox-setup-template.md)**: Prepare standardized quick-response templates for human agents to boost response speed and maintain a consistent brand voice.
* **[Service schedule](./expand-inbox-setup-schedule.md)**: Set your team's working hours and define the logic for switching between human support and AI-led automation.

### Stage 3: Advanced intelligent operations

* **[AI Agent](./expand-inbox-ai-intro.md)**: The core intelligent module of Inbox. Once enabled, the AI will automatically answer customer queries based on your FAQs and store information, significantly reducing manual workload.
* **[Conversation routing and groups](./expand-inbox-setup-group.md)**: For high-volume periods, you can set up routing rules to automatically assign specific inquiries (e.g., "Order issues") to designated staff groups.

## Managing customer conversations

Once configured, all customer inquiries will be aggregated in real-time within Genstore Inbox.

Authorized staff members can:
* Receive and reply to messages in real-time via the **Customer service workspace**.
* Enable **Email notifications** (configurable in [Message notifications](./settings-notifications.md)) to ensure no potential orders are missed.
* Take over conversations manually at any time for complex issues that the AI cannot resolve.