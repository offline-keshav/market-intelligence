import pandas as pd

def generate_market_signals():
    df = pd.read_csv("data/indices/nifty_analytics.csv")

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    latest = df.iloc[-1]

    # Direction signal
    if latest["7d_return_pct"] > 0 and latest["daily_return_pct"] > 0:
        direction = "Bullish"
    elif latest["7d_return_pct"] < 0 and latest["daily_return_pct"] < 0:
        direction = "Bearish"
    else:
        direction = "Neutral"

    # Risk signal
    if latest["7d_volatility"] > df["7d_volatility"].mean() and latest["daily_return_pct"] < 0:
        risk = "High Risk"
    elif latest["7d_volatility"] < df["7d_volatility"].mean():
        risk = "Low Risk"
    else:
        risk = "Normal"

    # Momentum signal
    if latest["7d_return_pct"] > latest["30d_return_pct"]:
        momentum = "Strong Momentum"
    elif latest["7d_return_pct"] < 0:
        momentum = "Weak Momentum"
    else:
        momentum = "Stable"

    signal_df = pd.DataFrame([{
        "Date": latest["Date"],
        "Market_Direction": direction,
        "Risk_Level": risk,
        "Momentum": momentum
    }])

    signal_df.to_csv("data/indices/market_signals.csv", index=False)
    print("Market signals generated successfully")
