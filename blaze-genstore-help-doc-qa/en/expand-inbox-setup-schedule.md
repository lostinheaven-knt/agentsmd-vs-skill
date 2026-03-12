# Set up service hours

To manage how customer messages are handled in Genstore Inbox, you can configure support hours for both live agents and the AI Agent.

- When the AI Agent is **disabled**, messages are handled by human agents during scheduled hours, and offline replies are sent during off-hours.
- When the AI Agent is **enabled**, you must first define its working mode: **24/7** or **specific hours**. Human support hours will then apply only to the remaining time outside the AI Agent’s availability.

## Set AI Agent service mode (if enabled)

If the AI Agent is turned on, start by defining its service mode:

- **24/7 AI support**: The AI handles all conversations at any time. Human support hours will be ignored.
- **AI On-Duty**: The AI only responds during defined hours. You will need to configure human support hours for the remaining time.

**Path**: Genstore Admin -> **Sales channels** -> **Inbox**.

Click **Enter** to access the Help desk workspace. Go to **Settings** -> **Service hours**

For instructions on enabling the AI Agent, see [Enable AI Agent](./expand-inbox-ai-intro#enable-ai-agent).

## Configure live agent hours

When the AI Agent is disabled, or set to scheduled mode, you can define the time periods when human agents are available.

**Path**: Genstore Admin, go to **Sales channels** -> **Inbox**.

Click **Enter** to access the Help desk workspace, go to **Settings** -> **Service hours**.

By default, service hours are set to **08:00–23:00, Monday to Sunday** (based on your store’s local time). You can fully customize this schedule.

**Instructions**:

- Adjust each day’s hours individually
- Use the `...` menu to **Clear today's schedule**
- Apply one day’s settings to all days using **Apply to all days**
- Click **Save** when done

### Bulk actions for agent schedule

To simplify setup, you can apply or clear working hours for the entire week using the bulk actions menu in the upper-right corner of the schedule section:

- **Set default hours (all days)**: Apply 08:00–23:00 to every day of the week
- **Clear all schedules**: Remove all time slots for the entire week

These shortcuts help reduce manual work if your team follows a standard schedule.

## Set automated first replies

You can configure separate auto-replies for online and offline periods:

- **Online**: Greet customers and ask for more context
- **Offline**: Let customers know support is currently unavailable and when to expect a response

The system provides default reply templates that you can customize.

**Setup instructions**:

1. In the **First auto reply** section, turn on the toggle switch
2. Edit messages for **Online** and **Offline** (max 2048 characters); a live preview will appear on the right
3. Click **Save** to apply changes
