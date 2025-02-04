# Enables interactive mode

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved data
df = pd.read_csv("../data/btc_data.csv", index_col="timestamp", parse_dates=True)

# Plot Bitcoin Closing Price Over Time
plt.figure(figsize=(12,6))
sns.lineplot(x=df.index, y=df["close"], label="Closing Price", color="blue")
plt.title("Bitcoin Price Trend 📈", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Compute Moving Averages
df["50_MA"] = df["close"].rolling(window=50).mean()  # 50-day Moving Average
df["200_MA"] = df["close"].rolling(window=200).mean()  # 200-day Moving Average

# Plot Closing Price + Moving Averages
plt.figure(figsize=(12,6))
plt.plot(df.index, df["close"], label="Closing Price", color="blue", alpha=0.5)
plt.plot(df.index, df["50_MA"], label="50-Day Moving Average", color="red")
plt.plot(df.index, df["200_MA"], label="200-Day Moving Average", color="green")
plt.title("Bitcoin Price with Moving Averages 🚀")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.legend()
plt.grid(True)
plt.show()

df["daily_return"] = df["close"].pct_change()  # Percentage Change

# Plot Daily Returns
plt.figure(figsize=(12,6))
sns.histplot(df["daily_return"].dropna(), bins=50, kde=True, color="purple")
plt.title("Bitcoin Daily Return Distribution 📊", fontsize=14)
plt.xlabel("Daily % Change")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


import yfinance as yf

# Fetch Ethereum Data from Yahoo Finance
eth = yf.Ticker("ETH-USD")
eth_df = eth.history(period="1y")  # Last 1 year of data

# Plot BTC vs ETH Prices
plt.figure(figsize=(12,6))
plt.plot(df.index, df["close"], label="Bitcoin", color="blue")
plt.plot(eth_df.index, eth_df["Close"], label="Ethereum", color="orange")
plt.title("Bitcoin vs Ethereum Price Comparison 🔥")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.legend()
plt.grid(True)
plt.show()
