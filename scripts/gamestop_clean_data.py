import pandas as pd
# 1. CLEAN STOCK PRICE DATA
# Raw problem: dates have timezone info (e.g. "2018-07-18 00:00:00-04:00") and prices have long messy decimals.
# Fix: strip timezone, keep only Date (no time), round prices to 2 decimals.
stock = pd.read_csv("gamestop_stock.csv")
stock['Date'] = pd.to_datetime(stock['Date'], utc=True).dt.date
stock=stock[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

#round prices to 2 decimals
for col in ['Open', 'High', 'Low', 'Close']:
    stock[col] = stock[col].round(2)

stock.to_csv("gamestop_stock_clean.csv", index=False)
print("Stock data cleaned ->",stock.shape[0], "rows")

# 2 & 3. CLEAN ANNUAL + QUARTERLY FINANCIALS
# Raw problem: yfinance saves data "transposed" - each COLUMN is a date,
# each ROW is a financial metric (Revenue, Net Income, etc).
# This is hard to plot. Fix: flip it (.T) so each ROW is a date/period,
# and each COLUMN is a metric. Also keep only the metrics we care about,
# instead of the 40+ obscure accounting line items yfinance includes.
key_metrics = [
    "Total Revenue", 
    "Net Income", 
    "Operating Income", 
    "Gross Profit", 
    "Total Assets", 
    "Diluted EPS",
    "Total Liabilities"]

def clean_financials(filepath,period_label,output_name):
    """Reusable function: works for both annual and quarterly financials
    since they have the exact same structure."""
    df = pd.read_csv(filepath, index_col=0)
    df_clean=df.loc[df.index.intersection(key_metrics)].T
    df_clean.index.name = period_label
    df_clean=df_clean.reset_index()
    df_clean.to_csv(output_name, index=False)
    print(f"{output_name} -> {df_clean.shape[0]} rows")
    return df_clean

annual_clean=clean_financials(
    "gamestop_annual_financials.csv",
    "FiscalYearEnd",
    "gamestop_annual_financials_clean.csv"
)

quarterly_clean=clean_financials(
    "gamestop_quarterly_financials.csv",
    "FiscalQuarterEnd",
    "gamestop_quarterly_financials_clean.csv"
)

# 4. CLEAN BALANCE SHEET
key_bs_metrics = [
    "Total Debt",
    "Tangible Book Value",
    "Cash and Cash Equivalents",
    "Total Assets",
    "Total Liabilities Net Minority Interest",
    "Stockholders Equity",
]

bs = pd.read_csv("gamestop_balance_sheet.csv", index_col=0)
bs_clean=bs.loc[bs.index.intersection(key_bs_metrics)].T
bs_clean.index.name = "FiscalQuarterEnd"
bs_clean=bs_clean.reset_index()
bs_clean.to_csv("gamestop_balance_sheet_clean.csv", index=False)
print("gamestop_balance_sheet_clean.csv ->", bs_clean.shape[0], "rows")

#clean SEC revenue history
#raw problem: SEC data mixes FULLL YEA(10-K) and QUARTERLY (10-Q) rows
#together in 1 file, plus has duplicate/amended filings
# Fix: keep only rows that (a) span close to a full year (~350-380 days)
# AND (b) come from a 10-K (annual report) form, then remove duplicates.
sec=pd.read_csv("gamestop_sec_revenue_history.csv")
sec['start'] = pd.to_datetime(sec['start'])
sec['end'] = pd.to_datetime(sec['end'])
#calculate how many days each reporting period covers
sec['days'] = (sec['end'] - sec['start']).dt.days
#filter: only full-year periods reported in a 10-K annual filing
sec_annual=sec[(sec['days']>=300) & (sec['form']=='10-K')].copy()
#some years got refiled/amended-keep only the latest filing for each year
sec_annual=sec_annual.drop_duplicates(subset=['end'],keep='last')
#keep only useful columns, rename for clarity
sec_annual=sec_annual[['start','end','val']].rename(
    columns={'val':'AnnualRevenue'}
)
#add a billions column since raw revenue numbers are hard to read
sec_annual['AnnualRevenue_Billions']=(sec_annual['AnnualRevenue']/1e9).round(2)
sec_annual.to_csv("gamestop_sec_revenue_annual_clean.csv", index=False)

print("\nAll files cleaned successfully:")
