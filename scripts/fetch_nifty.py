import yfinance as yf
import pandas as pd
from datetime import date
import os

# Create data directory if not exists
os.makedirs("data/indices", exist_ok=True)

def fetch_nifty():
    ticker = "^NSEI"   # NIFTY 50
    df = yf.download(ticker, period="10d", interval="1d")

    if df.empty:
        print("No data fetched")
        return

    df.reset_index(inplace=True)
    df["Index"] = "NIFTY 50"

    file_path = "data/indices/nifty_daily.csv"

    if os.path.exists(file_path):
        existing = pd.read_csv(file_path)
        df = pd.concat([existing, df]).drop_duplicates(subset=["Date"])

    df.to_csv(file_path, index=False)
    print("NIFTY data updated successfully")

if __name__ == "__main__":
    fetch_nifty()
