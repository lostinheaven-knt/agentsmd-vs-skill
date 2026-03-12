# Launch an SMS campaign

Before sending any text messages, you need to launch an SMS campaign and ensure you have a valid sending number for the target region, including:

- Toll-free numbers for the U.S. and Canada
- Branded sender IDs for Europe and Asia-Pacific

## Create an SMS campaign

You can create a campaign in two ways:

**Option 1:**

1. Log in to your Genstore admin and go to **Marketing**
2. Click **Start new campaign** in the top right
3. Select **SMS marketing**

**Option 2:**

1. Go to **Marketing -> SMS marketing**
2. Click **Create SMS campaign**

Once created, you’ll be taken to the SMS editor to configure content and recipients.

## Set up your message

### Sender ID

- The system will use your verified sender number by default
- Changing the sender ID may affect compliance status in certain countries and require re-approval
- To maximize deliverability and brand consistency, it’s best to keep the default

### Recipients

- You can select from your existing [customer segments](./operate-customers-segments.md), or create a new segment
- SMS can only be sent to users who have opted in; unsubscribed users will be excluded automatically
- Make sure your contact list is legally obtained and marketing compliant

### Message content

SMS messages are plain text only. No images or GIFs, but emojis and special characters are supported. Message length affects billing:

- **GSM-7 (standard text)**: up to 160 characters per message, then split into 153-char segments
- **UCS-2 (with emojis or non-Latin characters)**: up to 70 characters, then split into 67-char segments

#### Character count rules:

- Message length = signature (e.g. [YourStore]) + body content)
- Max length: 500 characters
- Special characters like `|`, `{}`, `[]` count as 2 characters

| Type                 | Encoding | Count rules                                     | Billing rules                                 |
| -------------------- | -------- | ----------------------------------------------- | --------------------------------------------- |
| English (GSM-7)      | GSM-7    | 1 char for standard, 2 chars for extended chars | ≤160 chars = 1 msg; <br />>160: 153/msg split |
| Multilingual (UCS-2) | UCS-2    | 1 char per symbol                               | ≤70 chars = 1 msg; <br />>70: 67/msg split    |

#### Examples:

- 350-character English SMS → 3 messages (153 + 153 + 44)
- 150-character Chinese SMS → 3 messages (67 + 67 + 16)

### Add links and personalization

- **Short links**: Automatically convert store links into short URLs to save space and track clicks
- **Variables**: Insert dynamic fields like name or phone number for personalized messages

> Messages without a link cannot be tracked for click activity.

## Preview and testing

Before sending, we recommend testing your message:

- **Live preview**: See how the SMS will appear for recipients in selected countries
- **Test message**:
	1. Click **Send test** in the top right
	2. Choose a country code and enter your mobile number
	3. Only one test message can be sent at a time
- **Preview summary**: Review sender ID, recipient count, message body, and estimated cost
