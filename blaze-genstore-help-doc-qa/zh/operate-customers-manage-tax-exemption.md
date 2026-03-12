# 设置客户免税

为客户设置免税可以有效减免指定客户群体的税费，特别是对于符合特定条件的非营利机构或其他免税资格的组织。

## 操作步骤

在 Genstore 商家后台，前往 **商店** -> **客户**，点击目标客户以进入其详情页。
在 **免税** 区域，您可以为该客户配置免税设置：
- **不免税**（默认）：客户下单时始终收取相应税费。
- **免税**：启用后，该客户的所有订单将免收税费（已含税产品除外）。
- **有条件免税**：客户默认不免税，仅在满足特定条件时免税。可配置以下两种条件：
	- **按地域设置**：您可为客户指定免税地区，例如：加利福尼亚州、佐治亚州和得克萨斯州。当客户的收货地址位于这些地区时，将不收取税费。
	- **按 Avalara 实体使用码设置**：如商店启用了 Avalara 自动税务服务，您可为符合条件的客户绑定实体使用码（Entity Use Code）。Avalara 将根据该码判断是否对交易免税。**注意**：实体使用码仅在开启 Avalara 时有效，使用手动计税方式则无需配置。

:::tip

- **电子邮箱关联**：免税设置仅对使用注册邮箱地址下单的客户有效。
- **含税价格产品**：即便客户享受免税，标有含税价格的产品仍需支付全额。

:::

## Avalara 免税客户设置说明

当商店启用 **[Avalara 自动化税务计算](./taxes-setting#自动税务)** 后，您可以为符合条件的客户设置 **实体使用码（Entity Use Code）**，以支持免税处理。Avalara 系统将在计算税费时，依据客户绑定的实体使用码及适用地区税法，自动判断是否免税。

**设置前须知**

请务必注意以下几点，确保合规性：
1. **准确设置实体使用码**：实体使用码应根据客户的真实免税资质进行设置。错误设置可能导致税务风险。
2. **了解使用限制**：某些使用码仅适用于特定地区，例如 `A - Federal Government` 仅适用于美国。
3. **上传免税证书至 Avalara**：设置实体使用码后，仍需登录 [Avalara 官网](https://www.avalara.com/us/en/signin.html)，为客户上传对应的免税资质证明。否则，该免税设置可能在实际计算中失效。

如有疑问，建议您联系 Avalara 官方获取最新和准确的指导。


**常见实体使用码（仅供参考）**

| Entity use code | Exempt reason | Restrictions and considerations |
| ---- | ---- | ---- |
| A | Federal Government | US only |
| B | State Government | - |
| C | Tribal Government | - |
| D | Foreign Diplomat | - |
| E | Charitable/Exempt Organization | - |
| F | Religious Organization | Effective January 1, 2018, the Streamlined Sales Tax Project (SSTP) split educational and religious organizations into two separate categories. Previously, Entity/Use Code F represented both religious and educational organizations. This change was effective in Avalara products on April 1, 2018. |
| G | Resale | - |
| H | Agricultural | - |
| I | Industrial Prod/Manufacturers | Tax codes PM020704 and PM020700 must be used with this code to apply state - mandated reduced rates for manufacturers in Alabama, Louisiana, and Mississippi. This code may produce a fully taxable result in states where no such reason for exemption or reduced rate is available. |
| J | Direct Pay | - |
| K | Direct Mail | - |
| L | Other/custom | Other exempt reasons such as, <br> - Capital Improvement <br> - Common Carrier <br> - Enterprise Zone <br> - Exempt by Statute <br> - Exporters <br> - Material Purchase <br> - Medical <br> - Pollution Control <br> - Prime Contractor <br> - R&D |
| M | Educational Organization | Effective January 1, 2018, the Streamlined Sales Tax Project (SSTP) split educational and religious organizations into two separate categories. Previously, Entity/Use Code F represented both religious and educational organizations. This change was effective in Avalara products on April 1, 2018. |
| N | Local Government | US only |
| P | Commercial Aquaculture | Canada only |
| Q | Commercial Fishery | Canada only |
| R | Non - resident | Canada only <br> For use by Canadian registrants receiving a Drop - Shipment Certificate from a registered consignee pursuant to Subsection 179(2) of the Excise Tax Act. |

关于 Avalara 实体使用码使用，您可以参考 Avalara 官网：[实体使用码](https://knowledge.avalara.com/bundle/dqa1657870670369_dqa1657870670369/page/Exempt_reason_matrix_for_the_U.S._and_Canada_entity_use_code_list.html#pus1650667484575)。Genstore 也强烈建议您咨询 Avalara 官方以获得更准确合规的指导。
