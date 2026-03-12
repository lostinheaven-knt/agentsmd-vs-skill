# 设置 Facebook 数据共享

通过将 Genstore 店铺的数据同步至 Facebook，您可以借助 Facebook 提供的广告和数据工具（如 Meta Pixel 和 Conversions API）更有效地追踪店铺流量、优化广告定位并提升转化效果。

::: tip
本功能为**可选设置**。启用数据共享后，建议更新您的 [隐私政策](./settings-privacy.md)，说明数据类型和用途，以保障客户知情权。
:::

您可以选择以下任一方式完成 Facebook & Instagram 数据共享：
- **通过 Facebook & Instagram 销售渠道自动同步数据**（推荐）
- 手动嵌入 Meta Pixel 像素代码，实现自定义追踪

## 通过 Facebook & Instagram 销售渠道共享数据（推荐）

:::tip
**Facebook & Instagram 渠道为系统内置应用**，在完成建店的初始设置后即自动安装，无需手动添加。您可在商户后台的 **商店 -> 销售渠道** 页面中查看该渠道。
:::

**设置步骤**：
1. 登录 Genstore 商户后台。
2. 点击 **销售渠道** -> **Facebook & Instagram**，进入渠道授权页。
3. 点击 **连接 Facebook 账号**，同步账号信息。
4. 在 Facebook 授权页点击 **绑定**，完成账号授权。
5. 选择或者创建 Facebook **业务资产组** 进行绑定。
6. 选择或新建一个 Meta Pixel 进行数据追踪，提升广告投放效果。
7. 确认所有信息后，点击 **提交审核**。
8. 审核完成后，您店铺中已配置 Facebook & Instagram 销售渠道的产品将自动同步至 Facebook 产品目录

更多关于 Facebook 账号的说明以及具体操作可参考 [Facebook & Instagram 销售渠道](./expand-sales-channels-facebook.md)

成以上设置后，Genstore 将自动向 Facebook 同步您的店铺访问和交易数据。

## 通过代码编辑器嵌入 Meta Pixel

如果您希望精确控制追踪内容和页面，可通过手动添加 Meta Pixel 实现自定义事件追踪。
1. 登录 Genstore 商户后台。
2. 点击 **商店** -> **在线商店** -> **模板**。
3. 找到当前使用的模板，点击右侧 **... -> 编辑代码**。
4. 打开您希望与 Facebook 共享数据的页面模板，贴入您的 Meta Pixel 代码。
5. 点击右上角 **保存**，发布更改。

### 参考资料

Facebook Meta 像素代码具体说明请查看官方说明：

- [Facebook转化追踪说明](https://developers.facebook.com/docs/meta-pixel/implementation/conversion-tracking#standard-events)
- [Facebook Meta Pixel 像素代码标准事件说明](https://developers.facebook.com/docs/meta-pixel/reference#standard-events)

## 在 Facebook 同步数据

完成设置后，您可以在以下工具中查看数据是否成功同步，并分析广告成效：

|工具|用途|访问链接|
|---|---|---|
|**Meta Ads Manager**|查看广告预算、投放成效、受众转化等|[点击进入](https://www.facebook.com/adsmanager)|
|**Events Manager**|查看像素事件、Conversions API 数据、用户行为路径|[点击进入](https://www.facebook.com/events_manager)|
