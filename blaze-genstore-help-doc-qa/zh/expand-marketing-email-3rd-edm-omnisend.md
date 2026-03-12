# Omnisend 邮件营销

**Omnisend** 是一款强大的 EDM（电子邮件营销）与 SMS（短信营销）工具，支持与 Genstore 店铺的实时数据同步，帮助您轻松构建高效的个性化营销体系。借助 Omnisend，您可以基于产品、客户和订单数据创建自动化邮件场景，例如欢迎邮件、购物车提醒等，实现精准触达。

## 前置准备

- 已拥有 **Omnisend 账号**
- 确保您即将授权的 Omnisend 店铺已与 Genstore 的站点网址相关联

### 如何将 Omnisend 店铺与 Genstore 店铺相关联？

1. 登陆 Omnisend，切换为您要绑定的 Omnisend 店铺。
2. 点击 **Store setting**，选择 Store information。
3. 将该店铺与 Genstore 店铺网址进行绑定，确认无误后，点击 **Update information**。

## 安装 Omnisend 应用

您可通过 Genstore 应用商店安装 Omnisend。

1. 打开 **[Genstore 应用市场](https://apps.genstore.ai/zh-CN/)**，并登录您的 Genstore 账号。
2. 如果您管理多个 Genstore 商店，请先选择目标商店。
3. 搜索 Genstore Omnisend。
4. 在应用页，点击 **安装** 按钮。
5. 您将被导向 Genstore 商户后台，进入应用设置流程。
6. [可选] 点击应用名称旁的图钉图标，可将 Omnisend 固定至后台导航菜单，便于后续访问。

## 连接 Omnisend 与 Genstore 店铺

通过账户授权，您可将 Genstore 店铺近三个月内的产品、客户和订单数据同步至 Omnisend，用于后续营销自动化配置。

1. 登录 Genstore 商户后台，在 **应用** 部分找到 Omnisend。
   - 若未固定至导航栏，可前往 **应用 -> 已安装**，点击 **Omnisend** -> **打开应用**。
1. 在 **账号设置** 中点击 **绑定**。
2. 请检查并确保您即将授权的 Omnisend 店铺已与 Genstore 的站点网址相关联。
3. 系统跳转至 Omnisend，输入账号与密码登录。
4. 选择您需要绑定的 Omnisend 店铺。
5. 查看 Omnisend 需要请求的店铺权限，确认无误后，点击 **Authorize access** 完成授权。

## 数据同步

完成以上设置后，点击 **数据同步** 下的 **同步** 按钮，即可将店铺数据一键同步至 Omnisend。

**初次同步数据范围**：

| 数据类型 | 同步规则 |
| --- | --- |
| 产品数据 | 店铺中所有产品数据将同步至 Omnisend |
| 客户数据 | 店铺中所有的客户数据将同步至 Omnisend |
| 订单数据 | 近三个月 Genstore 店铺中的订单数据将会同步至 Omnisend |

**后续新增数据同步规则**：

| 数据类型 | 同步规则 |
| --- | --- |
| 产品数据 | 授权后，产品的新增/更新/删除将同步至 Omnisend |
| 客户数据 | 授权后，客户的新增/更新/删除将同步至 Omnisend |
| 订单数据 | 授权后，Genstore 店铺所有新订单将会同步至 Omnisend |

**订单数据状态说明**：

| 订单状态 | 说明 |
| --- | --- |
| Paid for order | 订单已完成支付，包含全额支付或部分支付的订单 |
| Order fulfilled | 订单已进入履约流程，包含全部发货或部分发货的订单 |
| Order canceled | 订单已被取消 |
| Placed order | 已成功创建但尚未支付、发货或取消的订单 |

# 邮件营销场景

完成数据同步后，您可以在 Genstore 后台访问 Omnisend 的常用邮件营销场景模板，并跳转至 Omnisend 中创建对应的自动化流程（Automation）。

### 场景说明：

- **邮件营销**：配置定期促销、活动或新品推送邮件，使用 Omnisend 提供的模板实现个性化展示。
- **新客户欢迎**：当客户在店铺注册账号后，自动发送欢迎邮件，建立良好第一印象，并引导进行首次购买。
- **自动化营销邮件**：基于客户下单、支付、取消等行为，触发相应邮件（如感谢邮件、补货通知等），提高复购率。

您可点击对应场景下的 **去创建** 按钮，直接跳转至 Omnisend 完成配置。

### 重要说明

在设置自动化邮件流程时，仅支持 Genstore 通过 API 接口同步至 Omnisend 的事件。  
请在 Omnisend 中创建 Automation 时，确认所选 trigger 已由 Genstore 成功同步。

**拓展阅读**：

如需深入了解 Automation 的创建与事件触发机制，您可参考以下 Omnisend 官方文档：

- [Learn how to set up and customize your automation workflows, use audience filters and tags in automation](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings)

