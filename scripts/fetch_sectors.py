import yfinance as yf
import pandas as pd
import os

os.makedirs("data/sectors", exist_ok=True)

SECTORS = {
    "IT": "^CNXIT",
    "BANK": "^NSEBANK",
    "FMCG": "^CNXFMCG",
    "AUTO": "^CNXAUTO",
    "PHARMA": "^CNXPHARMA"
}

def fetch_sectors():
    all_data = []

    for sector, ticker in SECTORS.items():
        df = yf.download(ticker, period="10d", interval="1d")
        if df.empty:
            continue

        df.reset_index(inplace=True)
        df["Sector"] = sector
        all_data.append(df)

    final_df = pd.concat(all_data)

    file_path = "data/sectors/sector_daily.csv"

    if os.path.exists(file_path):
        existing = pd.read_csv(file_path)
        final_df = pd.concat([existing, final_df]).drop_duplicates(
            subset=["Date", "Sector"]
        )

    final_df.to_csv(file_path, index=False)
    print("Sector data updated successfully")

if __name__ == "__main__":
    fetch_sectors()
