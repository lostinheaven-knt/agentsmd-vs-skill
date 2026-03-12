# DSers Dropshipping

[DSers](https://www.dsers.com) 是 AliExpress 官方推荐的订单处理平台，广泛用于全球 Dropshipping 商家管理产品导入、批量下单与物流同步。

为帮助商家更高效使用 DSers，Genstore 提供了官方集成应用 **DSers Dropshipping**。通过 DSers Dropshipping，您可以将 Genstore 店铺与 DSers 平台无缝连接，实现从选品上架、订单同步、批量下单到物流追踪的全链路自动化，助力业务快速扩张。

## 核心功能

- **快速选品，高效上架**：您可快速导入产品，绑定多个供应商，批量发布至店铺；
- **订单自动化**：通过自动化、批量处理和数据同步，降低人工操作成本，提升履约效率；
- **实时物流同步**：发货后自动回传物流追踪信息；
- **支持多平台拓展**：可连接 AliExpress、Temu 等第三方平台，扩展货源。

## 使用前准备

在安装并使用 Genstore DSers 应用前，请确保您已准备好以下账号及绑定操作：

- 已申请 DSers 账号
- DSers 账号已绑定 AliExpress 账号
	- 如未绑定 AliExpress 账号，将无法完成订单处理与履约。
	- 具体步骤，可参考：[如何绑定 AliExpress](https://help.dsers.com/edit-account-link-dsers-to-aliexpress/)
- 拓展其他供货平台：除了 AliExpress 外，DSers 还支持连接多个第三方供货平台，您可根据需要连接第三方供货平台。
	- 具体步骤，可参考 [连接多个平台](https://help.dsers.com/connect-multiple-platforms/)

## 安装应用

1. 在 Genstore 后台，导航至  **应用**，或访问 [Genstore 应用市场](https://apps.genstore.ai/) 搜索 DSers Dropshipping；
2. 在应用卡片页点击 **安装**，进入权限确认页面；
3. 查看应用访问权限内容（如产品、订单等），确认无误后点击 **安装**；
4. 安装完成后将自动跳转至 DSers 控制台，根据页面提示完成授权和账号绑定。

## 通过 DSers 导入产品

您可通过 DSers 将 AliExpress、Temu 等平台的产品导入至 Genstore 产品库，实现快速选品、产品编辑与多店铺发布。目前支持以下三种导入方式：

- 关键词搜索导入
- 产品链接导入
- 使用 DSers Chrome 插件导入

### 关键词搜索导入

1. 在 DSers 控制台进入 **Find Product（查找产品）** 页面；
2. 输入关键词查找产品；
3. 勾选目标产品，点击 **Add to Import List（加入导入列表）**；
    - 首次操作时，系统可能提示安装浏览器插件，请按提示操作；
4. 同步完成后点击 **Check（查看）**，跳转至 **Import List（导入列表）** 页面；
5. 在列表中点击铅笔图标 **Edit（编辑）** 产品信息（标题、描述、图片等）；更多信息，可参考 [编辑产品详情](https://help.dsers.com/edit-products-customize-product-details/)
6. 确认信息后点击 **Push to Store（推送至店铺）**，将产品同步至 Genstore。

> 参考文档：[关键词搜索导入](https://help.dsers.com/import-products-from-find-suppliers/)

### 通过产品链接导入（AliExpress / Temu）

适用于已有明确商品链接的场景：

1. 复制 AliExpress 或 Temu 产品链接；
2. 登录 DSers，进入 **Import List（导入列表）** 页面；
3. 点击 **Import of Search（搜索导入）** 图标；
4. 粘贴链接后点击确认；
5. 产品导入成功后在列表中显示；
6. 可编辑后点击 **Push to Store（推送至店铺）** 发布至 Genstore。

> 参考文档：[通过链接导入产品](https://help.dsers.com/import-products-from-aliexpress-temu/)

### 通过 DSers Chrome 插件导入

1. 在 Chrome 浏览器中安装 DSers 插件；
2. 登录 AliExpress 或 Temu，使用插件导入商品；
3. 后续在 **Import List（导入列表）** 中完成编辑和推送。

> 参考文档：[使用插件导入产品](https://help.dsers.com/import-products-from-aliexpress-temu/)

## 在 Genstore 查看 Dsers 产品

- 成功同步后，您可在 Genstore 后台，导航至 **商店** -> **产品** 页面查看已导入产品；
- 上架状态：产品默认状态为 **上架**，您可进入产品详情页进一步编辑；关于产品页的具体操作说明，可参考 [添加产品](./operate-product-create.md)
- 库存同步：系统将自动为商品绑定 **Dsers 应用地点**，并同步库存。


## 将 Genstore 产品同步到 DSers

除了从 DSers 导入商品到 Genstore，平台也支持将您在 Genstore 创建的产品同步至 DSers：

1. 登录 DSers，进入 **My Products（我的商品）** 页面；
2. 在页面顶部选择 Genstore 店铺；
3. 点击 **Import Products from DSers（从 DSers 导入商品）**；
4. 系统默认展示所有商品，可单选或每次批量导入最多 10 个； 
5. 点击 **Import（导入）** 进行确认；
6. 导入商品将显示在 **Unmapped（未映射）** 分页中；
7. 点击商品卡片的 **Mapping（映射）** 图标，手动或自动完成映射操作。  

> 参考文档：[将产品导入 DSers](https://help.dsers.com/import-products/)

## Genstore 与 DSers 产品状态同步说明

在 Genstore 与 DSers 之间同步产品时，产品状态将自动映射。为确保订单正常处理，请留意以下状态对应关系：

### Genstore -> DSers

| Genstore 状态 | 映射至 DSers |
| ----------- | --------- |
| 草稿          | 草稿        |
| 上架          | 上架        |
| 存档          | 草稿        |

注意：Genstore 中“草稿”与“存档”的产品将在 DSers 中显示为草稿，无法用于履约。

### DSers -> Genstore

|DSers 状态|映射至 Genstore|
|---|---|
|上架|上架|
|草稿|草稿|

::: tip

从 DSers 向 Genstore 推送产品时，请取消勾选 **Also publish to Online Store** （即保留默认未选中状态），以保持产品状态为 **草稿**。推送完成后，您可在 Genstore 后台检查并完善产品信息。确认无误后，再将产品状态改为 **上架**，即可正式开始售卖。

::: 

## 订单同步与自动履约

产品上架后，当客户在 Genstore 下单，系统将自动通过 DSers 进行订单同步与履约处理。

### 同步订单

1. 客户在 Genstore 成功下单；
2. DSers 应用自动获取订单信息并同步至 DSers 后台；
3. 您可在 DSers 后台查看同步订单。

::: tip

如您在 DSers 账户中绑定了多个 Genstore 店铺，每个订单将根据其来源店铺自动分配。

:::

### 发货流程

您可通过以下两种方式对订单进行发货：

#### 在 Genstore 发起发货请求

1. 商家在 Genstore 后台点击订单中的 **Dsers 代发货**；
2. 系统将发货请求同步至 DSers，DSers 将通知供应商发货；
3. 供应商发货后生成追踪号；
4. DSers 自动将物流信息同步至 Genstore，更新订单状态；
5. 若启用发货通知，客户将收到追踪信息邮件。

#### 在 DSers 后台手动下单

1. 登录 DSers，进入 **Open Orders（开放订单）** 页面；
2. 勾选订单并点击 **Place Order（提交订单）**，可批量下单至供应商处；
3. 后续发货与物流同步流程同上，DSers 会自动将追踪号同步回 Genstore。

::: faq

## 常见问题

### Q1：对于 DSers 产品，如何在 Genstore 中进行仓库地点管理？
> A：通过 DSers 导入至 Genstore 的商品，会自动绑定由 Dsers 应用创建的地点，并使用该地点进行库存管理、物流设置和订单履约。您可前往 **设置** -> **地点**，查看应用地点。

### Q2：对于 Dsers 产品，税务如何计算？

> A：若“Dsers 应用地点”未提供详细地址，系统将按以下优先顺序选择计税地址：
> 	- 店铺注册地址；
> 	- 默认发货地点（如注册地址为空）。

### Q3：对于 DSers 产品，如何在 Genstore 中进行物流设置？
> A：请在 Genstore 后台 **设置** -> **发货配送** -> **物流配送** 中配置运费模板，并将由 Dsers 应用创建的地点作为发货点。系统将在客户下单时，自动根据该发货点及所选运费模板，计算用户应支付的物流费用。

:::