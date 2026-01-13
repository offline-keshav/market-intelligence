import pandas as pd

def calculate_market_metrics():
    df = pd.read_csv("data/indices/nifty_daily.csv")

    # Standardize column names (defensive)
    df.columns = df.columns.str.strip()

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert Close to numeric (CRITICAL FIX)
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Drop bad rows
    df = df.dropna(subset=["Date", "Close"])

    # Sort properly
    df = df.sort_values("Date")

    # Analytics
    df["daily_return_pct"] = df["Close"].pct_change() * 100
    df["7d_return_pct"] = df["Close"].pct_change(7) * 100
    df["30d_return_pct"] = df["Close"].pct_change(30) * 100
    df["7d_volatility"] = df["daily_return_pct"].rolling(7).std()

    df.to_csv("data/indices/nifty_analytics.csv", index=False)
    print("Market analytics updated successfully")
