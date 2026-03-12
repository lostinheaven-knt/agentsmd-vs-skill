# Shipping profiles

A shipping profile is the foundation for calculating shipping rates, logistics delivery, and order warehouse routing. Understanding the profile setup helps you configure delivery options that align with your expectations.
## Components of a logistic profile

You need to focus on the following elements when setting up a logistic profile:

- **Shipping location**
	- Shipping location refers to the warehouses or stores where your products are shipped from. This setting affects the shipping fee calculation and product inventory. For more details, refer to [configuring shipping location](operate-fulfillment-shipping-profile-configuration#configure-shipping-location).
- **Applicable products**
	- The products in a shipping profile will determine which profile is used to calculate shipping rates and warehouse routing. Note: A product can only match one shipping profile. For more details, refer to [Create custom shipping profile](./operate-fulfillment-shipping-profile-configuration#create-custom-shipping-profile).
- **Shipping zones**
	- Shipping zones define the areas to which your products can be delivered. If a customer's shipping address is outside the defined zones, the order may not be placed successfully. Be mindful of shipping costs when setting these zones. For more details, refer to [configure shipping zones and rates.](./operate-fulfillment-shipping-profile-configuration#configure-shipping-regions-and-rates)
- **Shipping rates**
	- Shipping rates must be configured for each shipping zone within the profile. These rates directly impact the cost of delivering products to that zone. For more details, refer to [configure shipping regions and rates.](./operate-fulfillment-shipping-profile-configuration#configure-shipping-regions-and-rates)

## Shipping profile types

There are two types of logistic profiles in Genstore: **General shipping profile** and **Custom shipping profile**. Both can be used for shipping fee calculations, delivery, and warehouse routing. Here are the differences:

| Items               | General shipping profile                                                                                       | Custom shipping profile                                                                                                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use case            | General shipping profile that apply to most products                                                           | For products that require special shipping locations, zones, or rates. <br />Example: For fragile or oversized items like glass or ceramics, a custom profile is recommended.                                          |
| Number of profiles  | Only one profile is allowed                                                                                    | Multiple profiles can be created (currently no limit)                                                                                                                                                                  |
| Creation method     | **The system will automatically generate a default shipping profile, which merchants need to manually update** | Merchants can create as needed                                                                                                                                                                                         |
| Applicable products | Applies to all physical products in the store, including new items                                             | User-defined product range                                                                                                                                                                                             |
| Profile management  | Profile deletion is restricted                                                                                 | No restrictions on deletion                                                                                                                                                                                            |
| Profile priority    | Custom profiles have higher priority                                                                           | Custom shipping settings have higher priority than general shipping settings.  <br>Since a product cannot be assigned to multiple custom shipping settings at the same time, there is no priority conflict among custom shipping profiles. |
