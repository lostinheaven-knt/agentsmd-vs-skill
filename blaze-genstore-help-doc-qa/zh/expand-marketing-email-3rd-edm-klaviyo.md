# 集成 Klaviyo

除了 Genstore 内建的邮件营销功能外，对于熟悉 Klaviyo 平台的用户，Genstore 还推出了官方应用 **Genstore Klaviyo**，支持将店铺数据原生同步至 Klaviyo，继续使用您熟悉的工作流与模板，打造更高效的自动化营销体系。

## 前置准备

- 已拥有 **Klaviyo 账号**

## 安装 Klaviyo 应用

您可通过 Genstore 应用商店安装 Klaviyo。

1. 打开 **[Genstore 应用市场](https://apps.genstore.ai/zh-CN/)**，并登录您的 Genstore 账号。
2. 如果您管理多个 Genstore 商店，请先选择目标商店。
3. 搜索 Genstore Klaviyo。
4. 在应用页，点击 **安装** 按钮。
5. 您将被导向 Genstore 商户后台，进入应用设置流程。
6. [可选] 点击应用名称旁的图钉图标，可将 Klaviyo 固定至后台导航菜单，便于后续访问。

:::tip

在授权 Genstore Klaviyo 应用时，您可能会看到 Klaviyo 关于 “未审核应用” 的提示。

该应用由 Genstore 官方开发，数据仅用于您与 Klaviyo 之间的同步，无其他用途。您可以安心完成授权流程。

如有疑问，可随时联系 Genstore 客服支持。

:::

## 连接 Klaviyo 与 Genstore 店铺

通过账户授权，您可将 Genstore 店铺近三个月内的产品、客户和订单数据同步至 Klaviyo，用于后续营销自动化配置。

1. 登录 Genstore 商户后台，在 **应用** 部分找到 Klaviyo。
   - 若未固定至导航栏，可前往 **应用 -> 已安装**，点击 **Klaviyo** -> **打开应用**。
2. 在 **账号设置** 中点击 **绑定**。
3. 系统跳转至 Klaviyo，输入账号与密码登录。
4. 查看 Klaviyo 需要请求的店铺权限，确认无误后，点击 **Allow** 完成授权。

## 设置客户同步与数据同步

根据 Klaviyo 的规则，若需要同步 Genstore 店铺中客户的订阅状态至 Klaviyo，需要前置选择一个 Klaviyo List 进行同步。

:::tip

Klaviyo List 是您用来存储客户联系信息（如邮箱地址）的名单集合，也是发送营销邮件的目标群体。

:::

### 选择客户 List

**配置步骤**：

1. 在 Klaviyo 客户同步设置中，选择一个已有的 List，点击 **保存**。
2. 如需创建新 List，可点击 **创建新的 List**，系统将跳转至 Klaviyo 后台创建页面。

### 配置 opt-in 设置（Klaviyo 后台）

List 选择完成后，请根据需求配置其订阅方式：

- **Double opt-in**：客户会收到确认邮件，需点击确认后才会同步订阅状态。
- **Single opt-in**：无需客户确认，系统自动同步订阅状态。

**配置步骤**：

1. 点击 **订阅确认方式（opt-in 设置）** 下的 **去配置** 按钮，跳转至 Klaviyo 后台 List 设置页面。
2. 在 **Settings -> API keys** 中，根据需要选择 double opt-in 或 single opt-in 模式。

## 数据同步

完成以上设置后，点击 **数据同步** 下的 **同步** 按钮，即可将店铺数据一键同步至 Klaviyo。

**初次同步数据范围**：

| 数据类型 | 同步规则 |
| --- | --- |
| 产品数据 | 店铺中所有产品数据将同步至 Klaviyo |
| 客户数据 | 店铺中所有的客户数据将同步至 Klaviyo |
| 订单数据 | 近三个月 Genstore 店铺中的订单数据将会同步至 Klaviyo |

**后续新增数据同步规则**：

| 数据类型 | 同步规则 |
| --- | --- |
| 产品数据 | 授权后，产品的新增/更新/删除将同步至 Klaviyo |
| 客户数据 | 授权后，客户的新增/更新/删除将同步至 Klaviyo |
| 订单数据 | 授权后，Genstore 店铺所有新订单将会同步至 Klaviyo |

## 邮件营销场景

完成数据同步后，您可以在 Genstore 后台访问 Klaviyo 的常用邮件营销场景模板，并跳转至 Klaviyo 中创建对应的自动化流程（Flow）。

### 场景说明：

- **邮件营销**：配置定期促销、活动或新品推送邮件，使用 Klaviyo 提供的模板实现个性化展示与分组投放。
- **新客户欢迎**：当客户在店铺注册账号后，自动发送欢迎邮件，建立良好第一印象，并引导进行首次购买。
- **自动化营销邮件**：基于客户下单、支付、取消等行为，触发相应邮件（如弃单挽留、订单确认等），提高复购率。

您可点击对应场景下的 **去创建** 按钮，直接跳转至 Klaviyo 完成配置。

### 重要说明

在设置自动化邮件流程时，若选择“客户行为”作为触发条件，仅支持 Genstore 通过 API 接口同步至 Klaviyo 的事件。
请在 Klaviyo 中设置 Trigger（触发器）与 Metric（用户行为指标）时，确认所选事件已由 Genstore 成功同步，以确保流程正确运行。

**拓展阅读**

如需深入了解 Flow 的创建与事件触发机制，您可参考以下 Klaviyo 官方文档：

- [Understanding flow triggers and filters - Klaviyo Help Center](https://help.klaviyo.com/hc/en-us/articles/115002779051)
- [How to use event data to personalize email and SMS flows](https://help.klaviyo.com/hc/en-us/articles/115002779071)
