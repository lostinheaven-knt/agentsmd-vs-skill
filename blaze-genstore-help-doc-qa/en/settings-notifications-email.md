# Manage your store emails

Emails are essential for staying on top of important updates and communicating with your customers. This guide shows you how to set up and manage your **store email**, **sender email**, and **reply-to email**, so you can run your business smoothly and keep your customers informed.

In Genstore, you’ll use three types of email addresses:
- **Store email**: Where Genstore contacts you about system updates, billing, and other important info. By default, this is the email you used when signing up for Genstore.
- **Sender email**: The email your customers see when they receive order updates, marketing emails, or other store communications. To look professional, we recommend using a branded email address with your own domain and verifying it.
- **Reply-to email**: The email address where you’ll get responses from customers when they reply to your store emails. This helps you stay on top of customer questions and feedback.

## Update your store email

Your store email is the address Genstore uses to contact you. If you need to update it, follow these steps:

1. In your Genstore admin, go to **Settings** -> **General**.
2. In the **Store details** section, click the pencil icon next to your store name and email.
3. Enter your new email address under **Store email**.
4. Click **Save**.

Note: To update the email or password you use to log in to Genstore, see [Verify or change your login email](./start-genstore-account-manage#verify-or-change-your-login-email).

## Update your sender email

Your sender email shows up in the **From** field of order notifications and marketing emails sent to customers. By default, this will look like `store+123@genstoremail.ai`, where `123` is a unique ID for your store.

To use your own branded email as the sender, follow these steps:

1. In your Genstore admin, go to **Settings** -> **Notifications**.
2. Click **Manage senders**.
3. Enter your preferred email address in the **Sender email** field.
4. Click **Save**.

### Verify your email domain

If you’re using your own domain for your sender email, you need to verify it. Verifying your domain helps keep your emails out of spam folders and ensures they reach your customers.

To verify your domain, follow the prompts to add new DNS records in your domain provider’s admin panel.

**Steps:**

1. In your Genstore admin, go to **Settings** -> **Notifications**.
2. Click **Manage senders**.
3. Click **Authenticate your domain** under your sender email. 
4. A pop-up window will display detailed instructions and the DNS records you need to add.
5. In a new browser tab:
	- Log in to your domain provider’s admin panel.
	- Go to the DNS management area (usually called “Zone Editor” or “DNS Settings”) and add the DNS records provided by Genstore (keep the TTL settings as they are).
6. Once you’ve added the records, return to the Genstore admin tab and click **Verify domain** to complete the setup.

It can take up to 24 hours for the changes to take effect. If verification doesn’t work, double-check the DNS records you added match the information provided in your Genstore admin.

## Update your reply-to email

Your reply-to email is where you’ll receive messages from customers who reply to your store emails. Updating this ensures you never miss important questions or feedback.

**Steps:**

1. In your Genstore admin, go to **Settings** -> **Notifications**.
2. Click **Manage senders**.
3. Enter your new email address in the **Reply-to email** field.
4. Click **Send verification email**.
5. You’ll get a verification email at your new reply-to address. Open the email and click the **Verify email** button to finish.