# 集成 Mailchimp

**Mailchimp** 是一款强大的 EDM（电子邮件营销）与 SMS（短信营销）工具，支持与 Genstore 店铺的实时数据同步，帮助您轻松构建高效的个性化营销体系。借助 Mailchimp，您可以基于产品、客户和订单数据创建自动化邮件场景，例如欢迎邮件、购物车提醒等，实现精准触达。

## 前置准备

- 已拥有 **Mailchimp 账号**

## 安装 Mailchimp 应用

您可通过 Genstore 应用商店安装 Mailchimp。

1. 打开 **[Genstore 应用市场](https://apps.genstore.ai/zh-CN/)**，并登录您的 Genstore 账号。
2. 如果您管理多个 Genstore 商店，请先选择目标商店。
3. 搜索 Genstore Mailchimp。
4. 在应用页，点击 **安装** 按钮。
5. 您将被导向 Genstore 商户后台，进入应用设置流程。
6. [可选] 点击应用名称旁的图钉图标，可将 Mailchimp 固定至后台导航菜单，便于后续访问。

## 连接 Mailchimp 与 Genstore 店铺

通过账户授权，您可将 Genstore 店铺近三个月内的产品、客户和订单数据同步至 Mailchimp，用于后续营销自动化配置。

1. 登录 Genstore 商户后台，在 **应用** 部分找到 Mailchimp。
   - 若未固定至导航栏，可前往 **应用 -> 已安装**，点击 **Mailchimp** -> **打开应用**。
2. 在 **账号设置** 中点击 **绑定**。
3. 系统跳转至 Mailchimp，输入账号与密码登录。
4. 查看 Mailchimp 需要请求的店铺权限，确认无误后，点击 **Allow** 完成授权。

## 设置客户同步与数据同步

根据 Mailchimp 的规则，若需要同步 Genstore 店铺中客户的订阅状态至 Mailchimp ，需要前置选择一个 Mailchimp Audience List 进行同步。

:::tip

Mailchimp Audience List 是您客户资料的总数据库，后续发邮件、设置自动化流程、做数据分析，均基于 Audience List 操作。

:::

### 选择客户 Audience List

**配置步骤**：

1. 在 Mailchimp 客户同步设置中，选择一个已有的 List，点击 **保存**。
2. 如需创建新 List，可点击 **创建新的 List**，系统将跳转至 Mailchimp 后台创建页面。

## 数据同步

完成以上设置后，点击 **数据同步** 下的 **同步** 按钮，即可将店铺数据一键同步至 Mailchimp。

**初次同步数据范围**：

| 数据类型 | 同步规则 |
| --- | --- |
| 产品数据 | 店铺中所有产品数据将同步至 Mailchimp |
| 客户数据 | 店铺中所有的客户数据将同步至 Mailchimp |
| 订单数据 | 近三个月 Genstore 店铺中的订单数据将会同步至 Mailchimp |

**后续新增数据同步规则**：

| 数据类型 | 同步规则 |
| --- | --- |
| 产品数据 | 授权后，产品的新增/更新/删除将同步至 Mailchimp |
| 客户数据 | 授权后，客户的新增/更新/删除将同步至 Mailchimp |
| 订单数据 | 授权后，Genstore 店铺所有新订单将会同步至 Mailchimp |

# 邮件营销场景

完成数据同步后，您可以在 Genstore 后台访问 Mailchimp 的常用邮件营销场景模板，并跳转至 Mailchimp 中创建对应的自动化流程（Automation）。

### 场景说明：

- **邮件营销**：配置定期促销、活动或新品推送邮件，使用 Mailchimp 提供的模板实现个性化展示与分组投放。
- **新客户欢迎**：当客户在店铺注册账号后，自动发送欢迎邮件，建立良好第一印象，并引导进行首次购买。
- **订单通知邮件**：当客户下单或订单取消后，通过 MailChimp 自动化发送订单确认、发货通知、订单取消等通知。

您可点击对应场景下的 **去创建** 按钮，直接跳转至 Mailchimp 完成配置。


