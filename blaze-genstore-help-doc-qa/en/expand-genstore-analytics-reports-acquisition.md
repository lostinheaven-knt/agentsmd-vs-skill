# Acquisition reports

**Acquisition reports** provide comprehensive insights into how visitors discover and navigate your website. By analyzing these reports, you can answer critical questions like, *"How many users visited the website via marketing emails in the last 30 days?"* You can view overall traffic trends over time, drill into specific periods, and identify top sources, devices, and pages driving visits—all to optimize your website and marketing strategies.

:::tip
Unlike the [**Sales by traffic referrer**](./expand-genstore-analytics-reports-sales-referrer.md) report, **Acquisition reports** focus solely on visitor metrics (not sales or order values). These reports apply only to the Online Store sales channel.
:::

## Data refresh frequency

Reports update automatically every **4-5 seconds.** Refresh the page manually to ensure you’re viewing the latest data.

## Sessions & visitor tracking

Sessions and visitors are tracked using cookies. When a visitor accesses your store, two cookies are stored on their device:

1. **Visitor cookie**: Identifies unique devices. Each device (e.g., desktop, mobile) has a distinct visitor ID.
2. **Session cookie**: Tracks session duration and activity. A session ends if the visitor is inactive for a period.

**Session end criteria**:

- Sessions expire after 30 minutes of inactivity (no clicks, page views, etc.).
- All active sessions end at midnight UTC daily.

Since one visitor can trigger multiple sessions, **session counts typically exceed visitor counts**. Examples:

- A visitor browses for 20 minutes, leaves, and returns 2 hours later → **1 visitor, 2 sessions**.
- A visitor leaves after 5 minutes but returns 10 minutes later → **1 visitor, 1 session** (due to the 30-minute inactivity rule).

## How to access

1. Log in to your Genstore admin.
2. Navigate to **Analytics** -> **Reports** in the left menu.
3. Locate financial reports under the **Acquisition** section on the Reports Summary page.
4. Click any report title to view comprehensive metrics and granular data.

## Report categories

Genstore Analytics offers multiple **Acquisition reports** to analyze visits by time, location, referral sources, devices, visitor types, and markets. Common categories include:

- **[Sessions over time](./expand-genstore-analytics-reports-acquisition-time.md)**
- **[Sessions by location](./expand-genstore-analytics-reports-acquisition-location.md)**
- **[Sessions by referrer](./expand-genstore-analytics-reports-acquisition-referrer.md)**
- **[Sessions by device](./expand-genstore-analytics-reports-acquisition-device.md)**
- **[New vs returning visitors](./expand-genstore-analytics-reports-acquisition-visitor.md)**
- **[Sessions by market](./expand-genstore-analytics-reports-acquisition-market.md)**

## Common terms

| Term | Definition |
| ---- | ---------- |
| **Sessions** | Total sessions on your online store. |
| **visitors** | Number of distinct users (deduplicated by visitor ID) within the selected timeframe. |
| **Pageviews** | Total number of pages viewed. |
| **Average session duration** | `Total session duration / Total sessions`. |
| **Bounce rate** | `Sessions with only one page view / Total sessions`. |
| **Added to cart** | Sessions where products were added to the cart. |
| **Reached checkout** | Sessions where users entered the checkout process. |
| **Conversion rate** | `Sessions with purchases / Total sessions`. |
| **Completed chekout** | Total sessions resulting in a purchase. |

## Metrics glossary

Definitions of key dimensions and indicators used in traffic reports:

### Dimensions

#### Basic info

| Field | Definition |
| ---- | ---------- |
| **Occurrence time** | Timestamp of the visit. |
| **Campaign objective** | Goal of the marketing campaign. |
| **Campaign type** | Type of marketing campaign. |

#### Device info

| Field | Definition |
| ---- | ---------- |
| **Device browser version** | Version of the browser used. |
| **Device browser** | Name of the browser used. |
| **Device type** | Device category (e.g., mobile, tablet, desktop). |
| **Device operating system version** | Version of the operating system. |
| **Device operating system** | Name of the operating system. |

#### Page info

| Field | Definition |
| ---- | ---------- |
| **Landing page path** | Path of the first page viewed. |
| **Landing page resource** | Resource type (e.g., image, video) on the landing page. |
| **Landing page type** | Category of the landing page (e.g., homepage, product page). |
| **Landing page URL** | Full URL of the landing page. |

#### Geographic info

| Field | Definition |
| ---- | ---------- |
| **City** | Visitor’s city. |
| **Region** | Visitor’s state/province. |
| **Country/region** | Visitor’s country or region. |

#### Campaign info

| Field | Definition |
| ---- | ---------- |
| **UTM campaign content** | UTM parameter tracking specific content in campaigns. |
| **UTM campaign medium** | UTM parameter tracking the marketing medium (e.g., email, social). |
| **UTM campaign name** | UTM parameter tracking the campaign name. |
| **UTM campaign source** | UTM parameter tracking the traffic source (e.g., Google, Facebook). |
| **UTM campaign term** | UTM parameter tracking campaign keywords. |

#### Traffic source info

| Field | Definition |
| ---- | ---------- |
| **Referral name** | Website that referred the traffic. |
| **Referral source** | Name of the referral source. |
| **Referral path** | Path on the referral site leading to your store. |
| **Referral source** | Traffic source category (e.g., direct, search, email). |
| **Referral search term** | Keywords used to find your store via search. |
| **Referral URL** | Full URL of the referral page. |
| **Referral platform** | Platform of the referral source (e.g., desktop, mobile). |
| **Referral channel** | Method by which visitors arrived (e.g., organic, paid). |
| **Referral category** | Classification of the referral source. |

#### Market info

| Field | Definition |
| ---- | ---------- |
| **Market name** | Name of the visitor’s market. |

### Indicators

#### Visit metrics

| Field | Definition |
| ---- | ---------- |
| **visitors** | Deduplicated count of visitor IDs. |
| **Sessions** | Total sessions. |
| **Page views** | Total pages viewed. |
| **Average session duration** | Average time spent per session. |
| **Bounce rate** | Percentage of single-page sessions. |

#### Shopping behavior

| Field | Definition |
| ---- | ---------- |
| **Added to cart** | Sessions with cart additions. |
| **Reached checkout** | Sessions entering checkout. |
| **Completed chekout** | Sessions resulting in a purchase. |
