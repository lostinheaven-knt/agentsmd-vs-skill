# Birthday reward points

Offering birthday points is an effective way to enhance customer engagement by providing rewards on their special day. This guide details the setup process, including scenarios and essential considerations.

## Set point rules

**Navigation**: 

1. Log in to Genstore admin and go to **Store** -> **Customers** -> **Loyalty**. 
2. Under the **Points** tab, find the **Earn points** section.
### Setup steps

Click **Add** -> **Birthday reward** -> **Add**:

- **Rule name**: Provide a name for this reward rule to facilitate easy management.
- **Earning points**: Specify the number of points awarded for birthdays. **Adjust this number to align with your overall points system.**
- **Reward rules**:
  - **Auto**: Points are automatically added to customer accounts on their birthday, accompanied by an email notification.
  - **Manual**: Customers receive an email prompt to log in and claim their points. You can set specific timeframes for claiming these rewards:
	- Points can be claimed only on the actual birthday.
	- Points can be claimed on any day within the birthday month.
	- Set a range of days before and after the birthday for reward claims (e.g., 7 days before to 7 days after).

## Preview and publish

Check your settings in the **Summary** section to the right. The system provides a real-time summary here. Once you confirm the details, click **Save** to activate the rule.

You can manage this rule—view, edit, enable, or disable it—via the **Earn points** list.

:::tip

Use the status switch to easily toggle this rule on or off.

:::

::: faq

## FAQs

### Q1. What if a customer hasn't registered their birthday in advance?
> A: Customers need to register their birthday at least 30 days beforehand to qualify for the reward. We recommend that birthdays be registered at sign-up.
> 	:::tip
> 	In this case, you can always assign the birthday reward points manually. For instructions, see [Manage customers](./operate-customers-loyalty-customer-manage.md).
> 	:::

### Q2. Can we set different reward rules for customers of different levels?
> A: The system currently supports only a uniform rule for all customers, allowing only one birthday reward claim per year.

### Q3. What if a customer misses the claim period?
> A: Customers cannot claim their points after the claim period has ended. To prevent this, enable (default setting) email reminders for birthdays.
> 	::: tip
> 	In this case, you can always assign the birthday reward points manually. For instructions, see [Manage customers](./operate-customers-loyalty-customer-manage.md).
> 	:::

### Q4. Will customers receive email notifications for birthday point rewards?
> A: Email notifications vary based on your **Rule Settings**:
> 	1. For Automatic Distribution: System sends a points credit notification on the customer's birthday
> 	2. For Manual Redemption: System sends reminder emails based on your redemption period settings, as shown below:

| **Redemption period** | **Reminder email send time**            |
| --------------------- | --------------------------------------- |
| Birthday only         | On the actual birthday                  |
| Birthday month        | On the actual birthday and month end    |
| Custom period         | On the actual birthday and N days after |

:::