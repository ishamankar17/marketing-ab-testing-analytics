# Marketing A/B Testing & Conversion Analytics

A/B testing (also called split testing) is a controlled experiment where two versions of a campaign, page, or product feature are shown to different groups of users at the same time — a **Control** (the existing/baseline version) and a **Test** (the new variant). By comparing how each group performs on key metrics, and checking whether the difference is statistically significant, marketers can determine whether a change actually improves results or if the observed difference is just random variation.

## Overview

This project analyzes a real marketing A/B test comparing a **Control** campaign against a **Test** campaign over a ~30-day period. It takes the analysis from raw daily ad-platform exports all the way to a statistically validated business recommendation, answering the core question: *the Test campaign is getting more clicks — but is it actually working better, or is that difference just noise?*

The workflow covers data cleaning, KPI calculation (CTR, CPA, conversion rates), hypothesis testing (Welch's t-test), full-funnel analysis, and an interactive 4-page Power BI dashboard.

## Tools & Tech

- **Python** — pandas, NumPy for data cleaning and KPI calculations
- **Matplotlib, seaborn** — exploratory visualizations
- **SciPy** — statistical significance testing
- **Jupyter Notebook** — exploratory and statistical analysis
- **Power BI** — interactive dashboard and business reporting

## Dataset

Two daily-level CSV exports, one per campaign:

- **Control group** — daily spend, impressions, reach, website clicks, and purchases for the baseline campaign
- **Test group** — the same daily metrics for the new campaign variant

The raw files were cleaned (missing rows dropped, dates parsed, campaign labels added) and merged into a single combined dataset, from which CTR, CPA, cost-per-add-to-cart, cost-per-purchase, and stage-wise funnel conversion rates were derived for both groups.

## Analysis Performed

1. **Data cleaning & merging** — standardized both raw exports into one analysis-ready dataset.
2. **KPI engineering** — calculated CTR, CPA, CPC, CPM, and conversion rates at each funnel stage for both campaigns.
3. **Exploratory analysis** — compared clicks, purchases, CTR, and CPA between groups, and plotted daily trends.
4. **Statistical testing** — ran a statistical significance test on CTR, CPA, and purchase conversion rate to check whether the Control vs. Test differences are statistically significant, not just visually different.
5. **Funnel analysis** — traced the full drop-off from Impressions → Website Clicks → View Content → Add to Cart → Purchase for each campaign.
6. **Dashboarding** — rebuilt all key metrics and the funnel in Power BI for a stakeholder-friendly, interactive view.

## Screenshots

### Campaign Performance

<img width="1313" height="737" alt="image" src="https://github.com/user-attachments/assets/bd65ae75-58cd-413b-9a3d-6f131245f3c5" />

Compares spend, clicks, purchases, CTR, and CPA side by side for Control vs. Test. The Test group shows higher spend and clicks, a noticeably higher CTR (4.92 vs 0.05 on this view) and a daily CTR trend line tracking performance across the month.

### Funnel Analysis

<img width="1312" height="740" alt="image" src="https://github.com/user-attachments/assets/cfcf7e02-f07a-40e1-bbea-83473e237452" />

Shows the full conversion funnel — Impressions to Website Clicks to View Content to Add to Cart to Purchase — for each campaign. Test converts a smaller pool of impressions more efficiently, ending with a higher overall CVR (0.70% vs 0.57%).

### Campaign Metrics

<img width="1311" height="738" alt="image" src="https://github.com/user-attachments/assets/5d7f3480-db2d-454d-85a5-cc8aa587d84f" />

Breaks down cost efficiency (CPC, CPM, cost per add-to-cart, cost per purchase) and stage-by-stage conversion rates for both campaigns, alongside daily spend trends. Test has a higher CTR and cart-to-purchase rate, but a lower content-view and add-to-cart rate than Control.

### Insights

<img width="1312" height="735" alt="image" src="https://github.com/user-attachments/assets/b39b5706-1419-495d-b57d-bd91f860022d" />

Summarizes the business verdict: CTR uplift, purchase growth, CPA change, and p-values from the significance tests, plus key findings and the recommended next experiment. This is the page decision-makers would read first.

## Business Insights

- **CTR improved significantly.** Click-through rate rose from 4.86% (Control) to 8.09% (Test), a **+66.5% uplift** that is statistically significant (Welch's t-test, *p* = 0.0003).
- **Purchases grew only modestly.** Website clicks jumped ~17%, but purchases grew just **+3.1%** — most of the extra traffic didn't convert.
- **The post-click funnel weakened.** View-to-cart conversion fell from 66.9% to 47.5% in the Test group, pointing to a landing-page or offer issue rather than a traffic issue.
- **Cart completion improved.** Once a user added to cart, they were more likely to complete the purchase (40.2% → 59.1% cart-to-purchase rate).
- **CPA rose, but not significantly.** Cost per acquisition increased from $4.41 to $4.92 (+11.6%), but this was **not statistically significant** (*p* = 0.1946); the change in purchase conversion also wasn't significant (*p* = 0.1428).

**Verdict: Test wins on engagement, not yet on efficiency.** The recommendation is to optimize the post-click experience (landing page, offer, CTA) before scaling the Test campaign's budget.

## Author

**Isha Mankar**
[GitHub](https://github.com/ishamankar17)
