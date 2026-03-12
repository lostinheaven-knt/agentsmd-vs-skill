# Custom apps

A custom app is an app exclusively developed for your Genstore store, distinct from public apps that serve multiple stores. It allows you to access store data through the Genstore API and extend platform functionality.

## Permission preparation

You can invite collaborators or staff to create, edit, or delete custom apps and grant development permissions as well as related API scope settings.

### Create app develop role

1. Log in to the Genstore admin.
2. Navigate to **Settings** -> **Users and permissions**.
3. Click **Manage roles**.
4. In the new window, click **Create role**.
5. Fill in the role **Title** and **Description**, such as `Custom App Development`.
6. In the **Store permissions** section, check **App development**.
7. Click **Save**.

### Assign app develop role

After creating the role with full permissions, you can assign it to collaborators or your staff.

1. Log in to the **Genstore admin**, navigate to **Settings** -> **Users and permissions**.
2. In the **staff** list, select the user, click **...** -> **Edit**.
3. In the staff details section, **select** the roles to assign.
4. Click **Save**.

## Create custom app

Once the role is created and assigned, you can begin the development of the app. **Note:** Only the store owner or staff with `App development` permission can develop custom apps.

1. In the Genstore admin, click **Apps** -> **Develop apps**.
2. In the new window, click **Build app**, and fill in the following information:
	- **App name**: Custom app name
	- **App developer**: Choose the store owner or an authorized staff account
3. Click **Build app**.

## Configure custom app

### Configure API access scope

Before installing the app, you need to set the API access scope.

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. In the **Overview** tab, click **Configure API access scope**. In the subsequent **App configuration** page, click **Edit**.
4. Check the required permission scopes (such as order reading, product management, etc.).
5. Click **Save**.

## Install app

Before installing the app, you need to obtain the API credentials.

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. Click the **Install app** button to confirm the installation.
4. The system will generate an **API Access token**. **Important:** The `Access Token` is only visible the first time, so make sure to save it.

## Credentials management

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. Click the **Manage API credentials** button or the **API credentials** tab to view:
	- `API Key`
	- `API Secret`
	- `API Access Token` (only visible the first time, recommended to view and save)

## App maintenance

### Update API scope

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. You can view the current API access scope in the **App configuration** tab.
4. Click **Edit** to modify the permission scope. **Note:** When updating the API scope, at least one permission must be retained for already installed apps.
5. Click **Save**.

### Modify basic information

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. You can modify the following in the **App settings** tab:
	- App name/description
	- Primary developer (if the staff account is deleted, ownership automatically reverts to the store owner)
	- Development update notification email (optional)

Click **Save** once modifications are complete.

## Uninstall and delete app

### Uninstall app

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. Click **Uninstall app**.
4. The system will automatically revoke the API Token and delete Webhooks.

### Permanently delete

Before deletion, ensure that the app has been uninstalled.

1. In the Genstore admin, click **Apps** -> **Build apps**.
2. In the app list, click on the target app to enter the app detail page.
3. Go to **App settings -> Delete app**.
4. Confirm the deletion, and all related data will be permanently deleted. **Note:** Deletion is irreversible, please proceed with caution.
