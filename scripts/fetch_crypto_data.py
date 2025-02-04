import requests
import pandas as pd

def fetch_crypto_data(symbol="BTCUSDT", interval="1d", limit=500):
    """
    Fetch historical cryptocurrency data from Binance API.
    :param symbol: Cryptocurrency pair (e.g., BTCUSDT, ETHUSDT)
    :param interval: Timeframe (e.g., 1d = daily, 1h = hourly)
    :param limit: Number of data points to fetch
    :return: Pandas DataFrame with OHLCV data
    """
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url).json()

    df = pd.DataFrame(response, columns=["timestamp", "open", "high", "low", "close", "volume",
                                         "close_time", "quote_asset_volume", "trades",
                                         "taker_base", "taker_quote", "ignore"])

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    # Select relevant columns and convert to float
    df = df[["open", "high", "low", "close", "volume"]].astype(float)

    return df

# Fetch and save data
if __name__ == "__main__":
    df = fetch_crypto_data()
    print(df.head())  # Display first 5 rows
    df.to_csv("./data/btc_data.csv")  # Save to a CSV file for further analysis
    print("Data saved to ./data/btc_data.csv")
