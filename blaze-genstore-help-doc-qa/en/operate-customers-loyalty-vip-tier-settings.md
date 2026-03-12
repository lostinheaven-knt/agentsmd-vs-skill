# Set VIP tier

The VIP Program is a crucial component of Genstore Loyalty, designed to encourage customer engagement and spending by offering various VIP tiers. This guide provides detailed instructions on how to add and edit VIP tiers and benefits, as well as solutions to common issues.

## Add VIP tiers

:::tip

Ensure the VIP program is inactive before adding a new tier.

:::

### Basic settings

- **Tier name**: Input a unique name for the tier, such as Bronze, Silver, Gold (up to 24 characters).
- **Tier requirement**: Define the points required for customers to achieve this tier, e.g., 1000 points.  **Note**: The threshold values are unique across all tiers.

### Tier privileges

Offer distinct point rewards to VIP customers that foster loyalty and increase sales. **Note**: VIP point benefits are unrestricted by order amount or product range.

- **Point Benefits**: Customers at this tier can receive:
  - Points based on the order amount (recommended): e.g., 10 points for every $100 spent.
  - A fixed number of points per order: e.g., 20 points per order.

:::tip

Here’s the relationship between point rewards and user tiers, with specific logic outlined in the diagram below:

- VIP benefits take precedence over standard benefits. For example: Customer A is a **Silver VIP**, earning 100 points for every $100 spent. Although there is a store promotion awarding 50 points per $100 spent, Customer A will receive 100 points for an order of $100, benefiting from the higher reward rule.
- Users must meet the threshold of the corresponding tier to enjoy the benefits.
- The two types of benefits cannot be used simultaneously.

:::

### **Entry rewards**

Activate exclusive rewards when customers first reach this tier. We recommend implementing a tiered entry reward system across different VIP tiers to more effectively enhance customer loyalty. You can click **Create prize**, and then **Add** next to each listed reward.

- **Discount amount**: E.g., a $10 discount voucher. For setup, refer to the [Discount amount redemption](./operate-customers-loyalty-points-redemption-discount-amount.md) page.
- **Discount percentage**: E.g., a 5% discount. For setup, refer to the [Discount proportion redemption](./operate-customers-loyalty-points-redemption-discount-percentage.md) page.
- **Free shipping**: E.g., a free shipping coupon, with settings for the maximum applicable shipping fee available at the [Free shipping redemption](./operate-customers-loyalty-points-redemption-free-shipping.md) page.
- **Free gifts**: Items that customers can redeem for free or at a discount using points. For setup, refer to the [Free gift redemption](./operate-customers-loyalty-points-redemption-free-gifts.md) page.
- **Points**: Award a specified number of points, simply enter the reward amount on the points page.

## Preview and publish

Check your settings in the **Summary** section to the right. The system provides a real-time summary here. Once you confirm the details, click **Save** to activate the rule.

Once created, the tier automatically appears in the VIP tab where you can edit the tier privileges or delete the current tier.

To customize your tier card background, click **Custom** in **Tier card background**. For detailed instructions, see [Store branding](./operate-customers-loyalty-customize.md).

::: faq

## FAQs

### Q1. How many VIP tiers can I create? Are more tiers better?
> A: You can set up to 10 VIP tiers. It is recommended to provide at least 2 VIP tiers, but it is best to limit the total to 5 for easier communication and management.

### Q2. How do I delete a VIP tier?
> A: First, deactivate the VIP program by toggling it off, then you can delete a tier by clicking the **Delete** button on the tier card or in the edit menu. A confirmation prompt will appear before deletion.

### Q3. Will changing the rules of the VIP program affect current customer tiers?
> A: Yes, any changes to the settings of the VIP program, such as points calculation rules or tier requirements, will trigger a recalculation of customer tiers and they will be reassigned based on the new rules.

### Q4. Can I edit VIP tiers while the VIP program is active?
> A: Yes. Once the VIP program is active, you can edit certain settings of the tiers (except for the threshold) but you cannot delete tiers at that time.

### Q5. What are point privileges?
> A: Point privileges are specific rules for point acquisition provided to customers at certain VIP tiers. Customers at this tier can earn more points, such as extra points for every $100 spent.

### Q6. At what tier should I start offering entry rewards?
> A: It is recommended to offer entry rewards starting from tier 2 and above. This not only effectively encourages customers to actively upgrade but also significantly enhances user engagement and loyalty.

### Q7. Can I set multiple same-type entry rewards for the same tier?
> A: Yes, you can configure multiple same-type entry rewards for the same tier, such as several discount vouchers.

### Q8. Can I customize the background of the tier cards?
> A: Yes, you can choose the default tier card background from the system or customize the card design to match your brand style.

:::