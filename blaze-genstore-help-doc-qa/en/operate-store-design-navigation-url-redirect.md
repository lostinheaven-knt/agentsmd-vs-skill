# URL redirection

You can configure URL redirections in the Genstore admin to automatically redirect traffic from old URLs to new ones. This helps you avoid 404 errors, preserve SEO rankings, and improve the user experience.

Genstore supports the following two types of redirection:

|Type|Description|
|---|---|
|**Single redirection**|- Redirects a specific old URL to a new URL <br/>- Ideal for page updates or merges|
|**Pattern redirection**|- Redirects multiple URLs that share a common path prefix to a new structure <br/>- Useful for collection restructuring or category replacements|

---

## Configure a URL redirect

1. Log in to your Genstore admin, and go to **Store** -> **Online Store** -> **Menus** from the left-hand menu. 
2. Click **URL redirect** in the top-right corner.
3. Click **URL redirect** again and choose the redirect type:
    - **Single redirect**: Redirect one specific old path to a new path
    - **Pattern redirect**: Redirect multiple paths that share a prefix to a new path structure
4. Fill in the redirect information:
    - **Redirect traffic from**: Relative path only (exclude domain), e.g. `/products/old-product-name`
    - **Redirect traffic to**: Relative path only (exclude domain), e.g. `/products/new-product-name`
5. Click **Save**. The system will automatically validate the redirect path.

## Import URL redirect configuration

1. Log in to your Genstore admin, and go to **Store** -> **Online Store** -> **Menus**.
2. Click **URL redirect** in the top-right corner.
3. Click **Import**, and download the CSV template.
4. Fill in the template with old and new paths, and save the file as a CSV.
5. Upload the CSV file and confirm the import.
6. The system will automatically validate each redirect entry based on the following rules:
    - Must start with `/` (i.e., a relative path); do not include full URLs like `https://...`
    - Cannot contain query parameters (`?`)
    - Cannot contain anchors (`#`)
    - Cannot include spaces or invalid characters (e.g. `< >`, `{ }`, `|`, `^`, `[ ]`)

## Export URL redirect configuration

1. Log in to your Genstore admin, and go to **Store** -> **Online Store** -> **Menus**.
2. Click **URL redirect** in the top-right corner.
3. Click **Export**, and choose from the following options:
    - Export all redirect records
    - Export selected records
    - Export based on filters or search results
4. After selecting your export scope, click **Export redirect**. The system will generate a CSV file for download.