# Connect a third-party domain to Genstore

If you already have a domain from a third-party provider (such as GoDaddy, IONOS, Namecheap, Cloudflare, etc.), you can connect it to your online store. When a third-party domain is successfully connected to Genstore, the system will automatically create a TLS certificate for you for free.

#### Steps:

1. In the Genstore admin, go to **Settings** -> **Domains**.
2. Click **Connect existing domain**.
3. In the **Domain** field, enter your domain name, for example `example.com`, then click **Next**.
4. Click **Connect automatically**, or expand **Manual setup** to complete the DNS record updates according to the instructions.

Domain verification may take up to 48 hours to complete. Once verified, your domain will be listed in the **Domains** section on the **Domains** page with a status of **Connected**.

## Connect automatically

Genstore partners with Entri Connect to provide you with an automatic domain connection service. You don't need to configure manually - simply authorize by logging in to automatically point your domain's DNS to Genstore.

Using the auto-connect feature will consume `10` points/domain. We will pre-deduct points before the auto-connect process begins and formally deduct them upon successful connection. If you cancel during the process or the auto-connect fails, the pre-deducted points will be returned to your store.

## Manual setup

If using manual setup, you need to log in to your domain provider account (such as GoDaddy, IONOS, Google Domains, etc.) and update the DNS records.

After updating the DNS records, you need to wait for the changes to take effect. This usually happens within two hours, but may take up to two days.

Correct DNS record values:

| Type  | Name | Correct record value                           |
| ----- | ---- | ---------------------------------------------- |
| A     | @    | `172.66.1.107` or `162.159.141.111`           |
| AAAA  | @    | `2a06:98c1:58::16a` or `2606:4700:7::16a`     |
| CNAME | www  | `shops.genmystore.com`                         |

::: tip

- Please delete any other incorrect A/AAAA/CNAME record values on your domain (if any such records exist).
- If you're connecting a subdomain, you only need to configure the corresponding CNAME record to point to `shops.genmystore.com`, without configuring A/AAAA records. For example: to connect **aaa.example.com**, you only need to point the **CNAME** record with the name **aaa** to `shops.genmystore.com`
- You don't need to change the **TTL** number in the DNS settings. Please use the default value.

:::