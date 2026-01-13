from scripts.fetch_nifty import fetch_nifty
from scripts.fetch_sectors import fetch_sectors
from analytics.market_metrics import calculate_market_metrics
from analytics.sector_metrics import calculate_sector_metrics

def run():
    fetch_nifty()
    fetch_sectors()
    calculate_market_metrics()
    calculate_sector_metrics()
    print("Pipeline + analytics run completed")

if __name__ == "__main__":
    run()
