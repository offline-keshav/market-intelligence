from scripts.fetch_nifty import fetch_nifty
from scripts.fetch_sectors import fetch_sectors

def run():
    fetch_nifty()
    fetch_sectors()
    print("Pipeline run completed")

if __name__ == "__main__":
    run()
