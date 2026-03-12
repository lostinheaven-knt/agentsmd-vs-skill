# Returns

The **Returns report** provides a comprehensive analysis of customer return behavior, including return dates, returned products, associated order IDs, and refund details.

## Report data fields

| Term | Definition |
| ---- | ---------- |
| **Return date** | The date and time when the return was processed. |
| **Product name** | The name of the returned product. |
| **Order ID** | The unique identifier of the order associated with the return. |
| **Net refund** | The refund amount for the product(s), excluding shipping and tax refunds. |
| **Shipping refund** | The refunded amount for shipping fees related to the order. |
| **Tax refund** | The refunded tax amount for the order. |
| **Total refund** | The total refund amount, calculated as `Net refund + Shipping refund + Tax refund`. |

:::tip

**Note**: The formula for **Total refund amount** may vary based on your business logic. Ensure alignment with your refund policy and accounting practices.

:::
