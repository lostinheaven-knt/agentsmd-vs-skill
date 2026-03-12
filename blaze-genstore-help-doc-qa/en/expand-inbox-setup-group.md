# Conversation routing

The conversation routing feature allows you to **automatically assign new conversations to the most appropriate agent or team based on the customer's origin market.** By creating different groups, you can easily enable collaboration across global teams and provide localized support.

## Feature overview

With grouping functionality, you can:
- **Precise distribution**: Create independent support groups for different markets (e.g., US / EU / SA / MENA).
- **Expert matching**: Ensure agents familiar with specific languages or business areas handle the corresponding markets.
- **Priority management**: When a customer matches multiple rules, the system automatically assigns the conversation based on priority.

## How to access
1. Log in to the Genstore admin, and click **Sales Channels** -> **Inbox**.
2. Click **Enter** next to **Help desk** to enter the customer service workspace.
3. In the left sidebar menu, click **Groups** under **Settings**. On this page, you can:
   - [Add a new group](#create-a-group)
   - [Manage group configurations](#manage-groups)

## Create a group
Creating groups allows you to precisely assign conversations to specific agents. Click the **Create group** button in the top right corner and follow these steps:

1. **Set group name**: Give the group an identifiable name, such as `US Support`.
   > Tip: Names must be unique and should ideally include the market or team role. Length is limited to 30 characters.
2. **Configure service regions**: Click **Select markets** and check **one or more** markets, such as US, EU, SA, MENA, etc.
   > Coming soon: We will support more dimensions for customer segmentation, such as IP-based location and geographic coordinates.
3. **Assign staff**: Click **Select staff** and check **one or more** agents. Note:
   - Only selected agents will receive conversations from this group.
   - You can assign agents based on language proficiency, professional skills, or time zones.
4. **Set priority**: Enter an integer between 0–99. The higher the value, the higher the priority.
   - Note: Priority values must be unique across different groups.
   - Example: If a customer matches both `US Support` (Priority 50) and `Global Team` (Priority 10), the system will prioritize the `US Support` assignment.
5. **Routing strategy**: Receive customer messages from selected markets and automatically distribute conversations based on the defined priority.
6. Click **Save** to finish creating the group.

## Manage groups

Once created, groups are displayed as cards on the list page where you can view:
- **Group name**: Identified in the top left, e.g., `US Support` / `Arabic Team`.
- **Conversation source**: The type of source; currently, routing is supported by market only.
- **Staff list**: The list of agents belonging to that group.
- **Routing strategy**: Description of the current strategy, e.g., "Receive messages from selected markets."

**Operation tips**
- Click the **Edit** icon to modify rules. Changes only apply to new conversations; existing ones are not affected.
- Click the **Delete** icon to remove a group. Note: Ensure there are no active conversations linked to a group before deleting it.

## Conversation assignment logic

When a new customer conversation is created, the system follows a "funnel" logic based on these steps:
1. **Rule matching**: Real-time check to see if the customer’s origin market matches any custom groups.
2. **Priority determination**: If multiple groups are matched, the system assigns it to the group with the highest priority value.
3. **Agent assignment**: The conversation is pushed to the workspace of agents within the final matched group.
4. **Fallback logic**: If no group is matched, the conversation enters the "Default group" to ensure no message is missed.

::: tip
To prevent customers from being left unattended due to uncovered rules, the system includes a non-deletable default group:
- **How it works**: New conversations that don't match any custom group are automatically routed here.
- **Staff scope**: Includes all staff with Inbox permissions by default to ensure maximum visibility.
- **Configuration note**: The routing strategy for this group cannot be modified or deleted.
:::

## Example scenarios

To help you understand the logic when multiple rules exist:
- **Multiple matches**: A customer from the US enters. They match both `US Support` (90) and `Global Team` (10). Since 90 > 10, the conversation is routed to `US Support`.
- **No rule coverage**: A customer from France enters. If no specific rule for France exists, the conversation automatically enters the default group.

| Source | Matched groups | Priority | Final routing result |
| :--- | :--- | :--- | :--- |
| **United States (US)** | `US Support` | **90 (Highest)** | `US Support` |
| | `Global Team` | 10 | |
| **France (FR)** | (No match) | - | **Default group** |

## Recommended templates

### Template A: Basic distribution

| Group | Market | Staff | Priority |
| :--- | :--- | :--- | :--- |
| Default group | All | All | 0 |
| `US Support` | United States | Alice | 50 |

### Template B: Multi-country and multi-team

| Group | Markets | Staff | Priority |
| :--- | :--- | :--- | :--- |
| `Arabic Team` | SA, AE | Omar | 80 |
| `EU Team` | FR, DE, IT | Marie | 70 |
| `US Team` | US | Alice | 60 |
| `Global Team` | All | All | 10 |

::: faq
## FAQs

### Q1: Can I route based on IP or language?
> A: The current version supports routing based on market regions only. Future versions will support location, IP, tags, and intent-based rules.

### Q2: Can an agent belong to multiple groups?
> A: Yes. The system will determine the routing based on the matched group's priority.

### Q3: How do I optimize logic using priority?
> A: Priority is the core of the system's decision-making. 
> - **High priority (High value)**: Use for specific, high-value, or language-specific groups (e.g., VIP service, specialized language teams).
> - **Low priority (Low value)**: Use for broad, general area groups (e.g., Global Team).
> - **Tiered suggestion**: Use a tiered approach (e.g., 90 / 70 / 50 / 10) so you can insert new rules between levels later.

### Q4: Can I manually transfer a conversation?
> A: Yes. Even after automatic assignment, agents can manually transfer a conversation to a more suitable colleague or group within Inbox.
:::