# Delete customer

When managing customer data, there may be times when you need to delete customer information that is no longer active or necessary to keep. However, due to data protection regulations and the need to maintain transaction history integrity, there are several factors to consider before deleting customer data.

:::warning

Customer deletion is irreversible. Once executed, it cannot be undone. Please confirm carefully before proceeding.

:::

## Customer deletion restrictions

Customer data cannot be deleted if any of the following conditions apply:

- **Order history exists**: If the customer account has order history (including both completed and draft orders), the data cannot be deleted in order to maintain transaction record integrity.
- **Customer is being merged**: Customer data involved in an ongoing merge process cannot be deleted, as it would affect the accuracy of the merge.
- **Active gift cards exist**: If the customer account has **active and unexpired** gift cards, the customer data cannot be deleted in order to protect consumer rights.

## Delete customer

**Delete a single customer**

1. Log in to the **Genstore admin**.
2. Navigate to the **Store -> Customers** section, open the target customer’s details page.
3. Select **More actions** -> **Delete customer**.
4. In the deletion confirmation pop-up, click the **Delete** button to complete the process.

**Bulk delete customers**

1. Log in to the **Genstore admin**.
2. In the **Store -> Customers** page, select multiple customers you wish to delete.
3. Click **Delete customer**.
4. In the deletion confirmation pop-up, click the **Confirm** button.
5. If some customers do not meet the deletion conditions, the system will automatically skip those customers and only delete the ones that meet the conditions.
