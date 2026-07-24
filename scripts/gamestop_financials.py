import yfinance as yf

gme = yf.Ticker("GME")

# Annual financials (income statement) - revenue, net income, etc.
annual_financials = gme.financials
annual_financials.to_csv("gamestop_annual_financials.csv")

# Quarterly financials
quarterly_financials = gme.quarterly_financials
quarterly_financials.to_csv("gamestop_quarterly_financials.csv")

# Balance sheet (assets, liabilities - useful for financial health)
balance_sheet = gme.balance_sheet
balance_sheet.to_csv("gamestop_balance_sheet.csv")

print("Annual Financials:")
print(annual_financials)

print("\nQuarterly Financials:")
print(quarterly_financials)