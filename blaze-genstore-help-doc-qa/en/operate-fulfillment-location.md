# Manage locations

In the **Genstore** admin, **locations** refer to physical addresses used for **sales, shipping, or inventory storage**. By adding locations, you can flexibly manage multiple warehouses, distribution centers, or stores, ensuring precise inventory and logistics control.

In **Settings** -> **Locations**, you can **add, deactivate, activate**, and **delete** locations.

## Add a location

You can easily add new locations, which are **enabled by default**, and can be used for configuring [shipping profiles](./operate-fulfillment-shipping-profile.md).

### Steps:

1. Log in to the **Genstore admin**, and go to **Settings** -> **Locations**.
2. Click **Add location**, and enter the location name and detailed address.
3. Click **Save**.

The newly added location will automatically appear in the location list. From there, you can manage the location’s **status**, **edit details**, or **delete the location**.

## Change the default location

When no other location is specified, the default location will be used for inventory and shipping when adding products. You can easily update your default location.
### Steps

1. Log in to your Genstore admin and go to **Settings** -> **Locations**.
2. In the **Default location** section, click **Change default location**.
3. Select an available location.
4. Click **Save**.

::: tip

- A default location is automatically created when you open your store. To avoid disruptions to your business, it is recommended to review and update this location.
- Only active locations can be set as the default. Disabled locations cannot be used as the default.  
:::

## Deactivate a location

If you no longer want to use a location for **sales, shipping, or inventory storage**, you can deactivate it.

::: tip

- **At least one location must remain active**.
- The **default location** cannot be deactivated. To deactivate it, you must first change your store’s default location.
- Before deactivating a location, ensure:
  - **Inventory transfer**: All inventory at this location has been cleared or transferred.
  - **Order fulfillment**: All orders assigned to this location have been shipped.
  :::

### Steps:

1. Log in to the **Genstore admin**, and go to **Settings** -> **Locations**.
2. Find the location you want to deactivate and **turn off** the switch under the **Status** column.

## Reactivate a location

You can reactivate previously deactivated locations and resume using them for order fulfillment.

### Steps:

1. Log in to the **Genstore admin**, and go to **Settings** -> **Locations**.
2. Find the location you want to reactivate and **turn on** the switch under the **Status** column.

## Delete a location

If a location is no longer used for **sales, shipping, or inventory storage**, you can delete it permanently.

::: tip

 You must **deactivate** a location before deleting it.

 :::

### Steps:

1. Log in to the **Genstore admin**, and go to **Settings** -> **Locations**.
2. Find the location you want to delete and click the **Delete** icon.
