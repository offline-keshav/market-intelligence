import pandas as pd

def generate_sector_signals():
    df = pd.read_csv("data/sectors/sector_analytics.csv")

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(["Sector", "Date"])

    # Take latest day per sector
    latest_df = df.groupby("Sector").tail(1)

    # Benchmark: average momentum across sectors
    avg_momentum = latest_df["momentum_score"].mean()

    signals = []

    for _, row in latest_df.iterrows():
        if row["momentum_score"] > avg_momentum and row["7d_return_pct"] > 0:
            signal = "Breakout"
        elif row["momentum_score"] < avg_momentum and row["7d_return_pct"] < 0:
            signal = "Weakening"
        else:
            signal = "Neutral"

        signals.append({
            "Date": row["Date"],
            "Sector": row["Sector"],
            "Momentum_Score": round(row["momentum_score"], 2),
            "7d_Return_Pct": round(row["7d_return_pct"], 2),
            "Sector_Signal": signal
        })

    signal_df = pd.DataFrame(signals)
    signal_df.to_csv("data/sectors/sector_signals.csv", index=False)

    print("Sector signals generated successfully")
