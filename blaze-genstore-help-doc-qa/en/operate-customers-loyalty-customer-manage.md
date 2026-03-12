# Manage customers

Beyond points and VIP membership levels, **Genstore Loyalty** also offers comprehensive customer management features.

Access these by entering your Genstore admin, then navigate to **Store** -> **Customers** -> **Loyalty**.  You can view the member details in the **Members** part of the **Dashboard** section.

## View member information

Click **Members** to enter the **Members** page. This section displays key customer data such as name, email, VIP level, point balance, referral status, and total spending. You can filter and manage customers in the following ways:

1. **Search**: Supports fuzzy searches by customer name or email.
2. **Filter**: Click the **Filter** icon to apply filters:
   - **Creation time**: Options include last week, month, three months, a year, or a custom range.
   - **Total spend**: Filter by amount or points with conditions like "Greater than or equal to", "Equal to", or "Less than or equal to".
   - **Status**: Filter by status as "Member", "Guest", or "Excluded".
   - **VIP tier**: Filter by configured VIP tiers, including an option for customers without a VIP tier.
1. **Batch freeze or unfreeze**: Select one or more customers by checking the checkbox to adjust customer information, and to batch freeze or unfreeze customer accounts.

## Modify member information

Access member details by clicking on their entry, where you can freeze or unfreeze accounts and edit phone numbers or points.

- **Basic info**: Includes avatar, name, email, address, membership start date, days as a member, phone number, and editable birthday.
- **VIP tier**: View the member's current level and progress.
- **Points**: View redeemed and expired points, adjust points, or assist in redeeming rewards.
- **Referrals**: See the status of member referrals, including active, pending, and invalid, along with exclusive referral links.
- **Activity**: Displays the customer's activity history related to points, rewards, VIP status, and referrals.

You can also click **View in Store** in the upper right corner to see the customer's complete order history, activity in the store, credit, set tags, or notes.

## Bulk adjust member information

In the upper right corner, click **Adjust member** to bulk modify member points or birthdays by uploading a CSV file.

- **Customer identifier**: Identify customers by their **Email** or **Mobile number**.
- **Fields to adjust**: Identify customers by their **Email** or **Birthday**.
  - **Points**
	- **Add points**: Add or deduct points from a customer's balance. Use positive numbers to add points, negative numbers to subtract. For example, if Customer A has 100 points and the file shows 300, their new balance will be 400 points.
	- **Reset points**: You can also reset the customer's points balance. For example, if Customer A has 100 points before adjustment, and the points column for Customer A in the imported file is 300, after the import adjustment, Customer A's points balance will be 300.
  - **Birthday**: Adjust the customer's birthday information.
- **Download CSV template**: The system provides a CSV template based on selected adjustment fields. Ensure at least one field is selected before downloading.
- **Add file**: The system checks the CSV file format and size. If the file meets the requirements, you can click **Import and adjust**. **Note**: Only CSV files up to 30MB are supported.

Clicking **Import and adjust** initiates the import process. If successful, the popup closes and the customer page refreshes. If the import fails, an error prompt appears detailing the failure reason.

:::tip

The system updates all records at once; if some fail, the import stops, and all changes are rolled back to ensure data consistency.

:::

::: faq

## FAQs

### Q1. How do I choose the customer identity field?
> A: By default, Email is used for customer identification. You can manually select "Phone Number" if preferred.

### Q2. Which fields can I adjust?
> A: The system allows adjustments for **Points** and **Birthdays**. Points are selected by default; you can uncheck this or add other fields.

### Q3. Is there a validation when downloading the CSV template?
> A: Yes, the system checks that at least one field has been selected before allowing the download. If no fields are selected, a prompt will appear: **"Please select at least one adjustment field."**

### Q4.  What are the requirements for importing a CSV file?
> A: The file must be in CSV format and not exceed 30MB. If the file does not meet these criteria, an error message will display.

### Q5. What happens when I click the cancel button?
> A: Clicking the **Cancel** button closes the popup and clears any uploaded files.

:::