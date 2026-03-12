# Merge customers

The customer merge feature allows you to consolidate duplicate or related customer profiles, simplifying management and unifying customer information. By merging, you can eliminate redundant data, maintain accurate and complete customer records, and centralize customer resources and history in a single account.

## Things to know before merging customers

1. **Irreversible**: Once a merge is completed, the action cannot be undone. Please review the data carefully before merging.
2. **Merge limit**: You can merge a maximum of two customer accounts at a time. If you need to merge more than two accounts, do so step by step.
3. **Permission restrictions**: Customer merge permissions are only available to merchants. Customers cannot merge accounts on their own.

## Mergeable items

The merge operation will consolidate the following data:

- **Basic information**: Name, email address, and phone number. If there are multiple names, emails, or phone numbers, only one will be retained after the merge. You can decide which item to keep before merging.
- **Orders and addresses**: All orders (including draft orders, but excluding abandoned orders) and shipping addresses.
- **Marketing subscriptions**: Email and SMS marketing subscription statuses will be inherited from the subscribed account.
- **Notes and tags**: Notes and customer tags will be merged.
- **Meta fields**: All meta fields will be merged. Empty fields will inherit data from the merged account.
- **Login password**: The password of the retained account will be kept.
- **Gift cards**: Any active and unexpired gift cards in the merged accounts will be retained.
- **Discount vouchers**: Unused and unexpired discount vouchers in the merged accounts will be retained.

## Steps to merge customers

### Prepare to merge

1. **Navigate to customer merge**: Log in to the Genstore admin, go to the **Store** -> **Customers**, click to enter the target customer’s detail page, and select **More actions** -> **Merge customer**.
2. The default displayed customer is the primary customer (the one that will be retained). To change it, go back to the customer list and use the search function to find the account you want to keep.
3. Use the search box to find and select the customer to be merged by their name, email, or phone number.

### Review and adjust

1. In the **Merge preview** section, you can review the merged customer’s information, such as name, email, phone number, default address, and tax-exempt status. Other data will be merged automatically, and once the merge is completed, it cannot be edited or restored.
   - If a piece of information is only available in one of the accounts being merged, such as the default address, the editing option for that field will not be displayed. Be sure to review all data carefully before merging to ensure that the information you want to keep is correctly set.
   - Changing the retained email will also update the customer ID, meaning the customer will need to log in with the new email after the merge.
2. The **Merge content** section will display the customer’s asset overview after the merge, such as tags, notes, marketing subscription status, discounts, tax-exempt status, addresses, orders, draft orders, gift cards, and meta fields.

### Complete the merge

- **Perform the merge**: After reviewing all information, click the **Merge** button to finalize the process.

## Handling exceptions

Some exceptions may arise during the merge process, and here are the solutions:

- **Notes exceed the limit**: If the merged notes exceed 1,000 characters, click **Resolve conflict** and adjust them to meet the limit.
- **Too many tags**: If the merged tags exceed 120 in total, click **Resolve conflict** and adjust them accordingly.
- **Data already deleted or in another merge task**: Customers in this state cannot be merged.
