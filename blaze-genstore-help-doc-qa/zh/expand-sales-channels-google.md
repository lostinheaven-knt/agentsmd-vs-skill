# Google & YouTube 销售渠道

Genstore 支持通过 Google & YouTube 销售渠道帮助您推广和销售产品，实现产品信息同步至 Google Merchant Center。借助 AI 驱动的智能广告投放，您可以在 Google Search、YouTube、Google Maps、Google Shopping 等多个平台上高效触达目标受众，优化转化率，并提升品牌影响力。

:::tip
**Google & YouTube 渠道为系统内置应用**，在完成建店的初始设置后即自动安装，无需手动添加。您可在商户后台的 **销售渠道** 页面中查看该渠道。
:::

## 核心优势

- **无缝集成**：商店直接关联 Google Merchant Center，确保产品能在 Google 各大平台展示。
- **提升转化**：利用 Google AI 和媒体资源优化广告投放，提升销售转化。
- **数据驱动**：集成 Google Analytics（GA），助您深入分析电商数据，优化运营策略。

## 前置准备

### Genstore 在线商店要求

在使用 Google & YouTube 销售渠道前，您的在线商店需符合 Google Merchant Center 的要求：

- 您的 Genstore 商店需公开访问，[不能设置密码保护](./operate-store-design-preference#关闭密码保护)。
- 在 Genstore 后台中添加有效的 [支付服务提供商](./operate-payments.md)。
- 商店需提供 [退款政策和服务条款](./settings-policy.md)，并确保这些政策位于页脚菜单。
- 在线商店需包含 [联系信息](./start-genstore-account-create-manage#管理店铺名称和联系信息)，并至少提供一种联系方式（如邮箱、电话、邮寄地址或联系表）。
- 商店需支持向受支持的 [国家/地区发货](./operate-fulfillment.md)，并以符合该国家/地区的货币进行销售。
- 需根据销售地区 [设置运费](./operate-fulfillment-shipping-profile-shipping-rate.md)，确保符合 Google Merchant Center 的要求。

在设置过程中，Genstore 将提供任务清单，帮助您完成所有前置要求。

### **Google 账号要求**

使用 Google & YouTube 销售渠道，您需拥有一个 Google 账户，并创建 Google Merchant Center 账户。Google Merchant Center 主要用于存储商店和产品数据，并支持 Google 广告及其他服务。

如果您没有 Google 账户，可在设置 Google & YouTube 销售渠道时创建。

## Google Merchant Center 账户同步注意事项

成功连接 Google Merchant Center 后，以下信息将从 Genstore 同步至 Google：

- 已配置 Google & YouTube 销售渠道的店铺产品。有关如何为产品配置销售渠道，请参考 [为产品配置销售渠道](./operate-product-create#销售渠道)。

如果您的 Merchant Center 账户已设有产品信息流，系统会覆盖该数据，以保持与 Genstore 商店的一致性。

## 连接到 Google Merchant Center 

在使用 Google & YouTube 销售渠道前，您需要绑定 Google 账号与 Google Merchant Center，以便您可以与 Google 同步产品。

1. 登录 Genstore 商户后台。
2. 点击 **销售渠道** -> **Google & YouTube**，进入 Google & YouTube 销售渠道授权页面。
3. 点击 **连接 Google 账号**，完成 Google 账户授权。
4. 在 **关联您的 Google Merchant Center 账号** 下拉框中选择或创建账户：
   - 选择现有 Merchant Center 账户并点击 **关联**。注意：您绑定的 Google 账户应该是待关联 Google Merchant Center 账号的管理员账户。
   - 若无 Merchant Center 账户，可点击 **新建账号** 进行创建。
5. 选择产品投放的国家/地区和语言。
6. 确认所有信息后，点击 **完成创建**。

## 产品同步设置
### 设置产品上传 Google 规则
1. 点击 **产品管理**，进入到上传产品管理页面。
2. 点击 **产品上传规则**，进入到规则管理页面，对 **基础规则** 和 **产品规则** 进行确认和调整，用以确定店铺上传至 GMC 的产品范围和产品同步至 GMC 的规则，确定后点击 **保存规则**。
3. 规则保存后，系统将按照您设定的规则从店铺获取数据至应用中，此处理过程需要等待一段时间（时间的长度取决于获取数据的数量）。
2. 数据获取完成后，系统会 Tips 提示您获取完成，您可在**产品管理** 页面的产品列表中看到产品数据，并可点击进入详情，查看产品信息。

### 开启产品上传
1. 产品上传规则设置完成且数据获取完成后，可在 **产品管理** 页面的产品列表中看到产品数据。
2. 确认产品数据无误后，点击 **开启自动上传**，系统将列表中的数据向 GMC 开始上传，此上传过程需要等待一段时间（时间的长度取决于获取数据的数量）。
3. 上传至 GMC 已批准/未获批准/待审核 产品都会将对应的状态展示在产品管理列表中，未获批准的产品将会给到具体的异常原因提示；
4. 数据上传获得结果后，系统会 Tips 提示您上传结果，您可在**产品管理** 的列表中看到产品的上传状态。

注明：上传数据并非实时立刻执行，对于有修改和更新的产品系统会进行定时同步，执行时间为每 1 小时执行一次。

## 关闭产品上传
1. 点击 **产品管理**，进入到上传产品管理页面。
2. 若您目前正处在产品上传开启状态，需要关闭上传产品，点击**关闭自动上传**，系统将停止将您产品管理列表中的产品同步至 GMC.

## 产品 Feed 链接获取
1. 点击 **产品管理**，进入到上传产品管理页面。
2. 产品获取完成后，系统会生成 Feed XML 文件。
3. 点击**复制 Feed 链接**，Feed XML 文件生成后，您可复制 Feed XML 文件的 URL 到 Google GMC 中通过 XML的方式导入产品信息至 GMC。


## 设置 Google 数据追踪

1. 登录 Genstore 商户后台。
2. 在左侧导航栏，点击 **销售渠道** -> **Google & YouTube**，进入 Google & YouTube 销售渠道 **设置页**。
3. 在 **数据追踪** 部分，您可点击 **添加数据跟踪**，您可选择：
   - Google Ads：追踪添加购物车、访问线上商城主页、提交结算、提交订单等行为，并设置 **转化 ID** 及 **转化标签**。
   - Google Analytics：创建衡量 ID，跟踪用户行为。
   - Google Tag Manager：创建 **容器 ID** 以管理营销标签。

## 解绑 Google 账号

如不再需要 Google & YouTube 销售渠道，可解绑 Google 账号：

1. 登录 Genstore 商户后台。
2. 在左侧导航栏，点击 **销售渠道** -> **Google & YouTube**，进入 Google & YouTube 销售渠道 **概览页**。
3. 点击页面右上角的 **设置**。
4. 点击 Google 账号后的 **解绑** 按钮。
5. 系统将弹出确认窗口，确认断开操作后，将断开 Google 账号连接。

解绑后，将同步解除 Google Merchant Center、Google Ads 及数据追踪关联。


