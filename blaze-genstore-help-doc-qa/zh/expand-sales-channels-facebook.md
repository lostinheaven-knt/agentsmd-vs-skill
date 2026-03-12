# Facebook & Instagram 销售渠道

在 Genstore，您可通过 Facebook & Instagram 销售渠道推广和销售产品。绑定 Facebook 账号后，产品信息会自动同步至 Facebook 和 Instagram 商店。借助 AI 驱动的广告投放，您能够精准触达目标客户，提高转化率，扩大品牌影响力。

:::tip

**Facebook & Instagram 渠道为系统内置应用**，完成建店初始设置后将自动安装，无需手动添加。您可在商户后台的 **商店 -> 销售渠道** 页面中查看该渠道。

:::

## 核心优势

- 同步产品描述及图片至 Facebook 和 Instagram 商店。
- 利用 Facebook & Instagram 社交媒体提升广告效果，扩大品牌影响力。
- 通过 Facebook Pixel 分析电商数据，优化投放策略。
- 统一库存管理，实现多平台销售。

## Facebook 账号要求

Facebook & Instagram 销售渠道适用于所有 [Genstore 版本](./start-understand-pricing-plans.md)。在开始使用 Facebook & Instagram 之前，请确保您：

- 拥有 Facebook Business Manager 账号，并具备管理权权限。
- Facebook Business Manager 已连接到您的 Facebook 公共主页及广告账户。
- 如已有个人广告账户，需将其关联至 Business Manager。如无广告账户，可在 [Business Manager 中创建](https://www.facebook.com/business/help/910137316041095?id=420299598837059) 。
- 您的 Facebook 公共主页需已发布，且每个业务页面只能归属于一个 Business Manager。
- 需使用 Genstore 在线商店进行销售，且商店不能受密码保护。了解 [如何删除在线商店密码](./operate-store-design-preference#关闭密码保护)。

更多信息，可参考：

- [Business Manager 介绍](https://www.facebook.com/business/help/1710077379203657)
- [广告账户指南](https://www.facebook.com/business/help/195296697183682?id=829106167281625)

## 前置准备

在绑定 Pixel 时有两种数据上报路径，请先确认您的需求：

- **Pixel 上报（浏览器端追踪）**：只需绑定 Pixel 即可，不需要 Access Token。
- **Conversions API 上报（服务器端追踪）**：如果您希望通过服务器端回传事件，则需要额外配置 Access Token。

::: info  
Pixel 绑定为必选操作。Access Token 配置仅在使用 Conversions API 时需要，且可在绑定完成后随时在商户后台维护。  
:::

### 获取 Access Token （可选）

如果您希望通过 **Conversions API** 将事件从服务器端回传至 Facebook，则必须生成并配置 Access Token。若仅使用 Pixel 前端埋点（浏览器端追踪），一般无需填写 Access Token。

1. 进入 Facebook  Business 管理后台。
2. 选择 **数据源** -> **数据集和 Pixel 像素代码**，点击 **添加** 按钮新建 Pixel。
3. 前往 **事件管理工具**，点击 **连接数据**，选择需要连接的数据源。
4. 选择需要连结的 Pixel 数据。
5. 点击 **设置**，建议使用默认推荐设置。
6. 选中您已连结的 Pixel 名称，点击 **设置** 找到 **设置直接继承**。
7. 点击 **生成访问口令**，复制并妥善保存。

## 设置 Facebook & Instagram 销售渠道并完成产品同步

1. 登录 Genstore 商户后台。
2. 点击 **销售渠道** -> **Facebook & Instagram**，进入渠道授权页。
3. 点击 **连接 Facebook 账号**，同步账号信息。
4. 在 Facebook 授权页点击 **绑定**，完成账号授权。
5. 选择或者创建 Facebook **业务资产组** 进行绑定。
6. 选择或新建一个 Meta Pixel 进行数据追踪，提升广告投放效果。
7. 确认所有信息后，点击 **提交审核**。
8. 审核完成后，您店铺中已配置 **Facebook & Instagram** 销售渠道的产品将自动同步至 Facebook 产品目录。
   > 有关如何为产品配置销售渠道，请参考 [为产品配置销售渠道](./operate-product-create#销售渠道)。

## 开通 Instagram shop

::: tip

请提前了解 [Facebook & Instagram 电商准入要求](https://www.facebook.com/business/help/2347002662267537?helpref=faq_content)

:::

### Instagram shop 开通流程
1. 申请 [注册 Facebook 账号](https://www.facebook.com/r.php?entry_point=login)。
2. 开通 Facebook 账号对应的 Facebook 主页，确保您是页面管理者。
3. 注册 [Meta Business 账号](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fsettings%2Fpeople%2F61577096798237%3Fbusiness_id%3D750381927420085%26verification_email_status%3Dsuccess)，并获得管理员权限，用于管理 Meta 下的相关业务，例如广告、Meta Business Suite、商务管理平台、电商管理工具等。
4. 在 Genstore 中完成 Facebook & Instagram 销售渠道授权绑定，将商品同步至 Meta 产品目录。参考 [设置 Facebook & Instagram 销售渠道并完成产品同步](#设置-facebook-instagram-销售渠道并完成产品同步)
5. 注册 [Instagram 个人账号](https://www.instagram.com/)。
6. 使用 Instagram 移动端应用登录账号，并将其升级为 [Instagram 专业账户](https://www.facebook.com/business/help/502981923235522?helpref=faq_content)。**注意：此步骤需在移动端完成**。
7. 在 Meta Business 账号体系下创建 [电商管理工具](https://www.facebook.com/commerce_manager?business_id=1073642577586787)，用于管理电商相关内容。
8. 按照 [Meta 官方指南](https://help.instagram.com/1187859655048322) 在 Facebook 和 Instagram 上开设店铺，并授权 Instagram 专业账号使用店铺资源，如：产品类目等。
9. 在 Instagram 移动端申请开通 Shopping 功能，路径：**设置** -> **Shopping**。此申请需等待 Meta 审批（约 5-7 个工作日）。
10. 审批通过后，即可在 Instagram 添加和推荐商品，开展销售。参考 [管理 Instagram 店铺并添加商品](https://help.instagram.com/601476600985792/Manage%2Byour%2Bshop%2Bwith%2Brecommended%2Bproducts)。

## 解绑 Facebook 账号

如不再需要 Facebook & Instagram 销售渠道，可解绑 Facebook 账号：

1. 登录 Genstore 商户后台。
2. 在左侧导航栏，点击 **销售渠道** -> **Facebook & Instagram**，进入销售渠道概览页。
3. 点击页面右上角的 **设置**。
4. 点击 Facebook 账号后的 **解绑** 按钮。
5. 在弹窗中确认操作后，将断开 Facebook 账号连接。

