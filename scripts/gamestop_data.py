import yfinance as yf

# Get historical data
gme = yf.Ticker("GME")
data = gme.history(period="8y")  # last 8 years
data.to_csv("gamestop_stock.csv")

print(data.head())