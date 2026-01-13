import pandas as pd

def calculate_sector_metrics():
    df = pd.read_csv("data/sectors/sector_daily.csv")

    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    df = df.dropna(subset=["Date", "Close"])
    df = df.sort_values(["Sector", "Date"])

    df["daily_return_pct"] = df.groupby("Sector")["Close"].pct_change() * 100
    df["7d_return_pct"] = df.groupby("Sector")["Close"].pct_change(7) * 100
    df["14d_return_pct"] = df.groupby("Sector")["Close"].pct_change(14) * 100

    df["momentum_score"] = (
        0.5 * df["daily_return_pct"] +
        0.3 * df["7d_return_pct"] +
        0.2 * df["14d_return_pct"]
    )

    df.to_csv("data/sectors/sector_analytics.csv", index=False)
    print("Sector analytics updated successfully")
