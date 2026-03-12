# Customer account

Customer accounts store personal details provided by customers through registration, order placement, and other interactions with the store. Key details include customer ID, name, email, phone number, address, login credentials, password, customer tags, tax exemption settings, and notes.

:::tip

Genstore treats email addresses and phone numbers as unique identifiers, so duplicates are not allowed within the same store.

:::

## Sources of customer accounts

- **Customer registration info**: Accounts are created automatically when a customer registers and logs into the store.
- **Customer placing an order**: When a guest places an order, the system creates an account using the provided email or phone number, with an initial status of **pending activation**.
- **Customer subscribing to email marketing**: Accounts are automatically created when a customer successfully subscribes to email marketing, with an initial status of **pending activation**.
- **Other methods of data submission**: If a customer submits their information through pop-ups, inbox, forms, etc., an account is created with an initial status of **pending activation**.

## Invite customer to activate their account

Account activation verifies the customer's email or phone number and unlocks the full features of the account.

Except for customer-initiated registrations, all accounts created through other methods will initially have a **pending activation** status. You can invite customers to activate their accounts by following these steps:

1. In Genstore admin, go to **Store** -> **Customers**.
2. Click on the **Customer details page** and click **Send invitation**.
3. Review the invitation email. You can either use the preset template or customize the subject and body of the email.
4. After the customer receives the activation email, they can click the **Activate account** button, set their password, and complete activation.
:::tip
   - If the customer declines activation on the activation page, their status will be shown as **Customer declined activation** on the details page.
   - If an invitation has been sent before, the system will display the number of past invitations and the most recent invitation time.
:::

## Managing customer accounts

### Account registration

Customers can create an account by clicking **Register** on the store. The options include:

- **Email + password registration**: Enter an email address and a password of at least 6 characters.
- **Third-party account registration**: Customers can register quickly using their Google or Facebook accounts by clicking **Register with Google/Facebook** on the registration page.

### Account login

Genstore currently supports the following login methods:

- **Username and password login**: Log in using the registered email and password.
- **Third-party account login**: After registering with a third-party account, customers can log in easily by clicking the corresponding account. If the account hasn’t been registered yet, the system will automatically register and log in the user.
- **Verification code login**: Customers who registered via email + password can select the verification code login option on the login page. Enter the email, receive the verification code, and log in.

### Change or reset password

#### Customer actions (Storefront)

- **Change password**: After logging in, go to **My profile** -> **Edit profile** -> **Change password**, and follow the prompts to update your password.
- **Forgot password**: On the login page, click **Forgot password** and follow the instructions to reset it.

#### Merchant actions (Merchant admin)

- **Reset customer password**: In the Genstore admin, go to the customer detail page, click **More actions** -> **Reset account password**. The system will send a password reset email to the customer. After clicking the link in the email, the customer can set a new password on the reset page.


::: faq

## FAQs

### Q1. Didn’t receive the verification code in my email?
> A: Please check the following:
> 	1. Make sure the email address you entered is correct, or try requesting the code again after 60 seconds. 
> 	2. Verify that the sender email address has been properly configured and verified in [Store notifications](./settings-notifications.md).
> 	3. If the issue persists, please contact Genstore support.

### Q2. Verification code login failed?
> A: Check whether the verification code is still within the 15-minute validity period. If it’s expired, we recommend requesting a new one. If you continue to experience issues, please reach out to Genstore support.

:::