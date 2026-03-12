# Genstore Inbox

Genstore Inbox 是一款专为电商打造的实时客服工具，覆盖售前咨询至售后服务的完整对话流程。客户可直接在店铺页面发起对话，您可手动回复，或启用 [AI Agent](./expand-inbox-ai-intro.md) 实现自动应答。

除了基础对话功能，Inbox 还整合了常见问题配置、话术库、在线值班机制和智能应答模块（AI Agent），帮助商家提升客服响应效率、降低人工负担。

## 功能概览

| 模块名称 | 功能说明 | 是否关联 AI Agent | 
| :--- | :--- | :--- | 
| [基础装修](./expand-inbox-setup-appearance.md) | 用于设置 Inbox 窗口首页的欢迎语与会话入口文案 | 否 | 
| [多语言适配](./expand-inbox-setup-localization.md) | 针对不同国家/地区展示本地化内容，包括欢迎语、FAQ 等 | 否 | 
| [开启客服聊天入口](#启用-inbox) | 商店右下角展示聊天入口，客户可主动发起对话 | 否 |
| [素材准备 - FAQs](./expand-inbox-setup-faqs.md) | 设置常见问题并在聊天框首页展示，作为 AI 回答的依据 | **AI 可引用** | 
| [素材准备 - 话术库](./expand-inbox-setup-template.md) | 配置标准回复模板，人工客服可快速插入 | 否 | 
| [客服时段安排](./expand-inbox-setup-schedule.md) | 设置人工客服在线时间，控制是否由 AI 在非工作时间接管 | **与 AI 联动** | 
| [AI Agent](./expand-inbox-ai-intro.md) | 自动回复客户提问，支持个性化训练和多数据来源 | **主力 AI 模块** | 
| [会话处理/分组](./expand-inbox-setup-group.md) | 配置会话路由规则并进行后台回复管理 | 否 | 

## 权限准备
确保客服团队顺利使用 Inbox，您需为员工分配对应权限。

**路径**：Genstore 后台 -> **设置** -> **账号权限** -> **管理角色**

创建角色后，在权限配置中勾选 **Inbox**，可进一步细化为：

| 权限项     | 说明                   | 建议应用场景 |
| ---------- | ---------------------- | ------------ |
| 会话处理   | 可查看并回复客户消息   | 日常客服     |
| Inbox 管理 | 拥有所有配置与查看权限 | 店主、主管等 |

## 启用 Inbox

1. 登录 Genstore 后台。
2. 进入 **销售渠道** -> **Inbox** 页面。
3. 打开 **在线聊天** 开关，即可启用。

## 快速开始

完成 Inbox 启用后，建议您按照以下三个阶段完善功能配置，以达到最佳的客户接待效果：

### 第一阶段：店铺形象装修

* **[外观设置](./expand-inbox-setup-appearance.md)**：自定义聊天窗口的品牌色、欢迎语及入口文案，确保客服窗口与您的品牌视觉风格保持一致。
* **[多语言](./expand-inbox-setup-localization.md)**：为不同国家/地区的客户提供本地化语言界面，消除沟通隔阂。
* **[会话入口](./expand-inbox-setup-appearance.md#2-会话入口)**：确认商店前台的聊天图标已正常显示，并处于最适合客户点击的位置。

### 第二阶段：内容与服务准备

* **[FAQs（常见问题）](./expand-inbox-setup-faqs.md)**：录入物流、退换货等高频咨询。这些内容不仅直接展示给客户，也是 AI Agent 的核心知识库。
* **[话术库](./expand-inbox-setup-template.md)**：为人工客服准备标准化的快捷回复模板，提升响应速度并保持品牌回复口径的一致性。
* **[在线值班表](./expand-inbox-setup-schedule.md)**：设定客服团队的工作时间，明确人工在线与 AI 接管的切换逻辑。

### 第三阶段：智能化运营进阶

* **[AI Agent](./expand-inbox-ai-intro.md)**：Inbox 的核心智能模块。启用后，AI 将根据您准备的 FAQs 和店铺信息自动回答客户，极大降低人工负担。
* **[会话路由与分组](./expand-inbox-setup-group.md)**：当咨询量较大时，您可以设置路由规则，将特定的会话（如“订单问题”）自动分配给指定的人员分组处理。

## 管理客户会话

完成上述配置后，客户的所有咨询将实时汇总在 [Genstore 后台 Inbox 模块](https://help.genstoredev.com/zh/docs/expand-inbox?id=64)中。

具有权限的员工可以：
- 在 **客服工作台** 实时接收并回复消息。
- 开启邮件提醒（可在 [消息通知](./settings-notifications.md) 中设置），确保不遗漏任何潜在订单。
- 针对 AI 无法处理的复杂问题，人工随时接管对话。