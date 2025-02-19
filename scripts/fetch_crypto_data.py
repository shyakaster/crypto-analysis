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
    # Fetch Bitcoin data
    df_btc = fetch_crypto_data(symbol="BTCUSDT")
    print(df_btc.head())  # Display first 5 rows of Bitcoin data
    df_btc.to_csv("../data/btc_data.csv")  # Save Bitcoin data to a CSV file
    print("Bitcoin data saved to ../data/btc_data.csv")

    # Fetch Ethereum data
    df_eth = fetch_crypto_data(symbol="ETHUSDT")
    print(df_eth.head())  # Display first 5 rows of Ethereum data
    df_eth.to_csv("../data/eth_data.csv")  # Save Ethereum data to a CSV file
    print("Ethereum data saved to ../data/eth_data.csv")
