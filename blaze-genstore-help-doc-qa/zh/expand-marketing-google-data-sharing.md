# 设置 Google 数据共享

通过将 Genstore 店铺的数据同步至 Google，您可以使用 Google Analytics、Google Ads 和 Google Tag Manager 等工具，分析店铺流量、广告成效和用户行为，并通过动态广告优化营销效果。

::: tip
本功能为**可选设置**。启用数据共享后，建议更新您的 [隐私政策](./settings-privacy.md)，说明数据类型和用途，以符合相关法律法规。
:::

您可以选择以下任一方式完成 Google 数据共享：

- **通过 Google & YouTube 销售渠道应用自动同步数据**（推荐）
- 手动嵌入 Google 提供的代码，实现自定义追踪

## 通过 Google & YouTube 销售渠道共享数据（推荐）

::: tip
**Google & YouTube 渠道为系统内置应用**，在完成建店初始设置后即自动安装，无需手动添加。您可在商户后台的 **商店 -> 销售渠道** 页面中查看该渠道。
:::

### 设置步骤

1. 登录 Genstore 商户后台。
2. 点击 **销售渠道** -> **Google & YouTube**，进入 Google & YouTube 销售渠道授权页面。
3. 点击 **连接 Google 账号**，完成 Google 账户授权。
4. 点击 **关联您的 Google Merchant Center 账号** 下拉框，选择或创建账户：
   - 选择现有 Merchant Center 账户并点击 关联。注意：您绑定的 Google 账户应该是待关联 Google Merchant Center 账号的管理员账户。
   - 若无 Merchant Center 账户，可点击 **新建账号** 进行创建。
5. 选择产品投放的国家/地区和语言。
6. 确认所有信息后，点击 **完成创建**。

更多关于 Google 账号的说明以及具体操作可参考 [Google & YouTube 销售渠道](./expand-sales-channels-google.md)。

设置完成后，Genstore 将自动向 Google 工具同步店铺数据。您可根据自己的业务需求，选择启用其中一项或多项功能。

## 通过代码编辑器嵌入 Google 追踪代码

如需更灵活地控制数据追踪内容，可手动嵌入 Google 提供的脚本代码。

### 设置步骤

1. 登录 Genstore 商户后台。
2. 点击 **商店** -> **在线商店** -> **模板**，选择当前使用的模板，点击右侧 **... -> 编辑代码**。
3. 打开需要追踪的模板文件，插入您的 Google 脚本。
4. 点击右上角 **保存**，完成修改。

::: tip
您可以嵌入的代码包括：
- Google Ads 转化追踪代码
- Google Analytics 衡量代码（GA4）
- Google Tag Manager 容器代码
:::

### 参考资料

[Google 网站设置转化跟踪](https://support.google.com/google-ads/answer/12216424)

## 在 Google 工具中查看共享数据

完成设置后，您可前往以下工具查看数据同步情况：

|工具|用途|访问链接|
|---|---|---|
|**Google Analytics**|查看网站访问量、页面浏览、用户行为、广告转化等|[访问 Google Analytics](https://analytics.google.com)|
|**Google Ads**|查看广告投放数据（展示量、点击率、转化等）|[访问 Google Ads](https://ads.google.com)|
|**Google Tag Manager (GTM)**|管理并监测网站的标签及数据追踪脚本|[访问 GTM](https://tagmanager.google.com)|
