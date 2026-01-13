from scripts.fetch_nifty import fetch_nifty
from scripts.fetch_sectors import fetch_sectors
from analytics.market_metrics import calculate_market_metrics
from analytics.sector_metrics import calculate_sector_metrics
from analytics.signal_engine import generate_market_signals

def run():
    fetch_nifty()
    fetch_sectors()
    calculate_market_metrics()
    calculate_sector_metrics()
    generate_market_signals()
    print("Pipeline + analytics + signals completed")

if __name__ == "__main__":
    run()
