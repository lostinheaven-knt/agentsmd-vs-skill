# Taxes

The **Tax report** displays the sales taxes applied to revenue within the selected time range.

Each row in this report shows a **tax type** (e.g., state or county tax), its corresponding rate, and the total tax amount paid during the selected period.

The report determines the country/region based on the **sale destination**. For origin-based tax jurisdictions (e.g., California), it currently displays the destination rather than the jurisdiction where the tax applies. If a shipping address is available, it is used. If not, the billing address is used. If neither is available, the POS location is used.

## Report data fields

| Term | Definition |
| ---- | ---------- |
| **Sales channel** | The marketplace or platform where the sale occurred (if applicable). |
| **Country/region** | The country/region associated with the tax rate. For origin-based jurisdictions (e.g., California), this reflects the destination, not the jurisdiction where the tax applies. |
| **Region** | The state or province associated with the tax rate. For origin-based jurisdictions, this reflects the destination, not the jurisdiction where the tax applies. |
| **Tax type** | The name of the tax (e.g., GST, VAT). |
| **Tax rate** | The tax rate percentage. |
| **Tax amount** | The total sales tax applied during the selected period. For example, if your revenue is $100 and a tax rate of 7% applies, this column will display $7.00. |
