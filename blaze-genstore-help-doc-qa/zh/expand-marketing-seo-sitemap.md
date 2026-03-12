# 生成并提交您的站点地图

每个 Genstore 网站都会自动生成一个 `sitemap.xml` 文件，包含所有产品、页面、博客文章等链接。这些链接可供搜索引擎抓取和索引，帮助您的网站内容更容易出现在搜索结果中。

为了加快页面的收录速度，建议您将站点地图提交到 Google Search Console。这有助于搜索引擎尽早发现您的新页面，提升网站整体的可见性。

Google 的抓取与索引时间因网站结构和内容更新频率而异，无法保证具体完成时间。您可以在 [Google Search Console 帮助中心](https://support.google.com/webmasters/answer/7474347?hl=en&visit_id=638827123947167441-3869662&rd=1) 查看提交状态并了解更多信息。

## 前置准备

- 拥有 **Google Search Console 账号**

## 查找站点地图文件

Genstore 会自动在您站点的根目录下生成 `sitemap.xml` 文件。例如 `example.com/sitemap.xml`。

该文件会自动更新，并包含所有产品、页面、博客等子站点地图，无需手动维护。此外，如果您启用了多语言或使用多个域名进行国际站配置，每个域名都会自动生成独立的站点地图文件。

若您拥有多个域名但未启用国际化功能，建议将这些域名统一重定向到主域名，以避免搜索引擎重复抓取或混淆页面归属。


## 验证网站所有权（Google Search Console）

在提交站点地图之前，您需要先通过 **[Google Search Console](https://search.google.com/search-console/welcome?utm_source=about-page&pli=1)** 验证网站归属。

::: tip

验证前，请保证网站需处于公开状态。如启用了密码保护，[请先关闭](./operate-store-design-preference#关闭密码保护)）。

:::

### 验证步骤
1. 访问 [Google Search Console](https://search.google.com/search-console/welcome)，点击 **≡**，从下拉菜单中选择 **添加属性**。
2. 在 **选择属性类型** 对话框中，选择 **URL 前缀**，填写完整域名（包含 `https://`）。
3. 点击 **继续**。
4. 在 **验证所有权** 窗口，选择 **HTML 标记** 或其他您熟悉的验证方法。
5. 在 **HTML 标记** 部分，点击 **复制** 以将完整的元标记复制到剪贴板。请务必复制所有内容，包括 `<` 和 `>`。例如：

  ```text
  <meta name="google-site-verification" content="IV7BPLESttSpBdxSWN1s4zlr4HIcuHkGQYmE3wLG59w" />
  ```

6. 登录 Genstore 商户后台，转至 **商店** -> **在线商店** -> **模板**。
7. 找到要编辑的模板，点击 **...** 按钮打开操作菜单，然后点击 **编辑代码**。
8. 在 **layout** 部分，点击 `theme.liquid`。
9. 将您在步骤 5 中复制的元标记直接粘贴到 `<head>` 开始标记下的空白行中。
10. 点击**保存**。
11. 返回 Google Search Console，点击 **验证**。

::: tip

如首次验证失败，请等待 15 分钟后重试。

:::

## 提交站点地图

1. 验证完成后，进入 Google Search Console 控制台。
2. （可选）如果您的账户下有多个根域名，请在页面顶部的下拉菜单中选择正确的域名。
3. 左侧菜单选择 **索引 -> 站点地图**。
4. 在 **添加新的站点地图** 输入框中填写：`sitemap.xml` ，系统会自动补全您的网站域名，例如 `https://example.com/sitemap.xml`。
5. 点击**提交**。

