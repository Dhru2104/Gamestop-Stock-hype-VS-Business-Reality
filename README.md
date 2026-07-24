****📊 GameStop: Stock Hype vs. Business Reality (2018-2026)****

A data analysis project investigating whether GameStop's dramatic stock price movements reflect genuine business performance — or something else entirely.

****📌 Project Overview****:

GameStop (GME) became a household name in January 2021 when its stock price surged over 15x in weeks, driven by a coordinated retail investor movement on Reddit's r/WallStreetBets. This project asks a simple question: did GameStop's business actually improve to justify this, or was the stock price telling a completely different story from the company's real performance?

By combining stock price data, official financial filings, and social media sentiment analysis, this project separates market hype from business fundamentals — and finds a business that has continued to decline in its core operations, even while achieving recent profitability through cost-cutting rather than sales growth.

****🔍 Key Findings****:

Stock price surged from ~$5 to ~$81 in January 2021, and never fully reverted — settling into a $20-30 range through 2026

Revenue fell 57% from $8.55B (2017) to $3.63B (2025), driven by the ongoing shift from physical to digital game distribution

Net income improved (2023-2026) despite falling revenue — but this came primarily from cost-cutting and non-operating income (e.g., interest on cash reserves), not from actual sales growth
Reddit mentions of GME spiked to 6,486 posts/week in late January 2021, then collapsed to under 100/week within three months — timing that closely mirrors the stock's rise and fall

As of 2026, Wall Street analysts largely maintain cautious "Hold"/"Sell" ratings on GME despite record profitability, citing the same structural decline in physical retail identified in this analysis

 ****🛠️Data Sources****🛠️:

| Source | Data | Coverage |
|--------|------|----------|
| Yahoo Finance (yfinance) | Daily stock price (OHLCV), quarterly/annual financials | 2018-2026 |
| SEC EDGAR | Historical annual revenue & financials | 2017-2025 |
| Kaggle | r/WallStreetBets Reddit posts (~53,000) | Sept 2020 - Aug 2021 |

****🛠️ Tools & Methods****

****Python (pandas, yfinance, vaderSentiment)**** — data collection, cleaning, sentiment scoring

****VADER Sentiment Analysis**** — scored ~15,000 GME-related Reddit posts on a -1 (negative) to +1 (positive) scale

****Power BI**** — interactive dashboard

## Repository Structure

```
├── data/
│   ├── raw/                                    # Original pulled data
│   │   ├── gme_stock_price.csv          # Yahoo Finance daily OHLCV
│   │   ├── gme_financials.csv           # SEC EDGAR revenue/income
│   │   └── reddit_wsb.csv               # Kaggle r/WallStreetBets posts
│   └── clean/                                  # Cleaned, analysis-ready CSVs
│       └── gamestop_stock_price.csv
│       ├── gamestop_reddit_sentiment.csv 
│       └── gamestop_daily_sentiment_summary.csv
├── scripts/
│   ├── gamestop_clean_data.py                  # Cleans stock/financials/SEC data
│   ├── gamestop_sentiment_daily.py             # Reddit sentiment analysis
│   ├── gamestop_annual_financials.py           #Financials
│   └── gamestop_weekly_sentiment.py            # Aggregates sentiment to weekly
├── dashboard/
│   └── gamestop_dashboard.pbix                 # Power BI file
```


****💡 Insights & Recommendations****:

Why it happened: 
→ The stock's rise and fall tracked Reddit posting activity, not business performance — GME mentions surged to 6,486 posts/week in Jan 2021, then crashed to under 100/week within 3 months, mirroring the price almost exactly. 

→ Revenue during this period rose only modestly, nowhere near enough to justify the price surge. Later, net income improved despite falling revenue — but this came mainly from cost-cutting and interest income, not real sales growth.

****Recommendations****:
1. Leadership should set Operating Income growth targets (not just Net Income) through actual retail improvements. 
2. Pre-commit any future capital to specific uses (e-commerce/store modernization) BEFORE hype happens. 
3. Redirect 30% of store closure savings directly into online ordering, delivery, website improvements — not cash reserves.

****🚀 How to Reproduce****:
1. **Install dependencies**: pip install pandas yfinance and vaderSentiment
2. **Reddit WallStreetBets Dataset**: Download the dataset from Kaggle(https://www.kaggle.com/code/gpreda/wallstreetbets-reddit-posts-analysis)
3. Run scripts in scripts/ in order to regenerate clean datasets
4. Open dashboard/gamestop_dashboard.pbix in Power BI Desktop to explore the interactive dashboard
