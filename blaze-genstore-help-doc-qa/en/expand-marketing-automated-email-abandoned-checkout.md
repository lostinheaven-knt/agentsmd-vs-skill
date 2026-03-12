# Recover abandoned checkout

Genstore automation offers a wide range of workflow templates to help automate tasks for specific scenarios.

In this document, we’ll use **abandoned checkout recovery** as an example to show how to use Genstore's automation tool to recover abandoned orders and help you get started quickly.

## About abandoned checkout

An **abandoned checkout** occurs when a customer enters the checkout page and provides contact information (such as an email or phone number), but doesn’t complete the payment and ultimately abandons the purchase. These customers usually show high purchase intent, making them prime candidates for recovery.

**The goal of abandoned checkout recovery** is to automatically send reminder emails or SMS messages to customers who abandoned their orders. This helps guide them to complete their purchases, improving conversion rates and sales revenue.

## Enabling the abandoned checkout recovery template

1. Log in to your Genstore admin.
2. Go to **Marketing -> Marketing automation**.
3. Click **Create marketing automation**, and select the **Recover abandoned checkout** template.
4. Click **Create** to enter the workflow canvas.
You can review the predefined workflow and adjust it as needed.

## Default workflow logic

The following is the standard structure of the abandoned order recovery workflow:

|Step|Type|Description|
|---|---|---|
|1|Trigger|Trigger the process when the customer abandons checkout.|
|2|Condition|Only execute if the abandoned order amount is greater than $0.|
|3|Delay|Wait for 10 hours before proceeding to the next step.|
|4|Condition|Check if the customer has not completed the purchase after abandoning the order.|
|5|Condition|Ensure the abandoned product is still in stock.|
|6|Action|Send an abandoned order reminder email to the customer.|

The workflow includes three layers of conditions to ensure that reminder emails are only sent for valid abandoned orders with inventory, preventing interference with non-target customers.

## Configure workflow parameters (optional)

You can adjust key parameters in the workflow to suit your business needs, or keep the default values:

- **Order amount**: The process only runs for orders greater than $0 by default.
- **Wait time**: It’s recommended to set this to 6-24 hours to avoid disturbing customers immediately, which can improve open rates.
- **Order completion check**: Checks if the customer has placed a new order after abandoning the previous one.
- **Inventory check**: If the abandoned product is out of stock, no reminder will be sent.

## Activate the email (required)

::: tip
We recommend using Genstore’s provided abandoned order email marketing templates. These templates allow you to easily customize each content section and quickly create personalized emails.
:::

Click the **Send marketing email** node in the workflow canvas to enter the email setup page:
1. Click **Select template**. The template list page will open in a new window, allowing you to select and edit a template for the current workflow. For specific steps, refer to [Create email marketing campaign](./expand-marketing-email-create-new.md).
2. After selecting a template, return to the workflow editor to preview the email subject and content. To make further adjustments, click **Edit**.

## Activate the workflow

Return to the workflow canvas and click **Activate** in the top right corner to start the workflow. The system will verify the workflow logic’s completeness before activation. If there are any configuration errors, it will prompt you to make corrections.

You can also find the workflow under **Marketing -> Marketing automation**, click the title to view the workflow details, and click **Activate** to enable it.

## Customer experience

After activation, the system will automatically send emails based on the customer’s abandoned order behavior. Here’s what the customer will experience:

- The email will show the abandoned items, including images, names, and prices, to help them quickly recall their shopping intent.
- The email contains a quick checkout button that allows the customer to proceed directly to the checkout page for easy payment.

## Common non-triggering scenarios

The system will not send an abandoned order reminder in the following situations:

- **All products are out of stock**: No products available for checkout.
- **Customer has completed the purchase**: The customer has placed a new order after abandoning the previous one.
- **Not subscribed to marketing emails**: The customer hasn’t agreed to receive marketing emails.
- **Delay time hasn’t passed**: The delay period for the most recent abandoned order hasn’t been reached.
- **Order amount is $0**: Orders with a total of $0 are not considered valid abandoned orders.

## Adjust the workflow

You can view the workflow status, make adjustments, and track the effectiveness of abandoned order recovery at any time.

**Steps**:

- Go to **Marketing -> Marketing automation**.
- Search for and click the workflow title you want to view.
- Check the current workflow status (active or draft).
- Click **Edit** to modify the draft version. Drafts only become active once they are activated.
- Once your adjustments are complete, click **Activate** to replace the currently active workflow.

## Data and performance feedback

- View abandoned order records on the **Store** -> **Orders -> Abandoned Orders** page. The system will keep this data for 3 months, and data older than that will be automatically deleted.
- In the **Marketing automation** tab on Email marketing page, check the open rate, click-through rate, and the sales and order counts from recovered abandoned orders. This helps you evaluate the marketing effectiveness and adjust your recovery strategy.   

We recommend regularly reviewing the data feedback from abandoned order recovery and adjusting conditions and email content based on customer behavior to continually improve order recovery performance.