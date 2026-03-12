# Set tax exemption for customers

Setting tax exemption for customers can effectively reduce taxes for specific customer groups, especially for non-profit organizations or other entities that qualify for tax-exempt status.

## Operation steps

In Genstore admin, go to **Store** -> **Customers**, click on the target customer, and enter their detail page.
Under the **Tax exemption** section, you can configure the customer’s exemption status:
- **No tax exempt** (default): Taxes will always be applied to the customer's orders.
- **Tax exempt**: All orders placed by the customer will be exempt from tax (excluding tax-included products).
- **Conditional tax exempt**: The customer is not exempt by default, but will be tax-exempt under specific conditions. Two types of conditions are supported:
    - **By region**: You can specify exempt regions for the customer. For example, if you set California, Georgia, and Texas as exempt regions, no tax will be charged when the customer’s shipping address is in one of these states.
    - **By Avalara Entity Use Code**: If your store uses Avalara for automated tax calculation, you can assign an Entity Use Code to eligible customers. Avalara will determine whether the transaction is exempt based on the assigned code.
        > **Note**: Entity Use Codes are only applicable when Avalara is enabled. If you're using manual tax configuration, this setting is not required.

:::tip

- **Email matching required**: Tax exemption settings only apply if the customer places orders using their registered email address.
- **Tax-included products**: Even if the customer is exempt, tax-included products will still be charged at full price.

:::

## Avalara tax-exempt customer setup

When **[Avalara automated tax calculation](./taxes-setting#automated-tax-settings)** is enabled, you can assign **Entity Use Codes** to qualified customers to support tax exemption. Avalara will automatically determine whether a transaction is exempt based on the assigned code and applicable tax laws.

### Important considerations before setup

To ensure compliance, please note:

1. **Assign the correct Entity Use Code**: The code must reflect the customer's actual tax-exempt status. Incorrect assignment may lead to tax compliance issues.
2. **Understand code restrictions**: Some codes are limited to specific regions. For example, `A - Federal Government` is valid only in the United States.
3. **Upload exemption certificates to Avalara**: After assigning an Entity Use Code, you must log in to [Avalara’s website](https://www.avalara.com/us/en/signin.html) to upload the customer’s exemption certificate. Failure to do so may result in the exemption being invalid during calculation.

For detailed guidance, we recommend contacting Avalara directly.

### Common Avalara Entity Use Codes (for reference only)

|Entity Use Code|Exempt Reason|Restrictions and Notes|
|---|---|---|
|A|Federal Government|US only|
|B|State Government|–|
|C|Tribal Government|–|
|D|Foreign Diplomat|–|
|E|Charitable/Exempt Organization|–|
|F|Religious Organization|As of Jan 1, 2018, SSTP split religious and educational organizations into separate categories. This change took effect in Avalara on Apr 1, 2018.|
|G|Resale|–|
|H|Agricultural|–|
|I|Industrial Prod/Manufacturers|Must be used with tax codes PM020704 and PM020700 for reduced rates in AL, LA, MS. May result in full tax in other states.|
|J|Direct Pay|–|
|K|Direct Mail|–|
|L|Other/Custom|Includes:  <br>- Capital Improvement  <br>- Common Carrier  <br>- Enterprise Zone  <br>- Exempt by Statute  <br>- Exporters  <br>- Material Purchase  <br>- Medical  <br>- Pollution Control  <br>- Prime Contractor  <br>- R&D|
|M|Educational Organization|Split from code F as of Jan 1, 2018. Change effective in Avalara from Apr 1, 2018.|
|N|Local Government|US only|
|P|Commercial Aquaculture|Canada only|
|Q|Commercial Fishery|Canada only|
|R|Non-resident|Canada only. For use by Canadian registrants receiving a Drop-Shipment Certificate from a registered consignee per Subsection 179(2) of the Excise Tax Act.|

For more information on Avalara Entity Use Codes, refer to Avalara’s official documentation: [Entity Use Code List](https://knowledge.avalara.com/bundle/dqa1657870670369_dqa1657870670369/page/Exempt_reason_matrix_for_the_U.S._and_Canada_entity_use_code_list.html#pus1650667484575). We also strongly recommend consulting Avalara support to ensure proper tax compliance.