pip install pandas requests beautifulsoup4 lxml
python scrape.py

import pandas as pd
import requests

TEAMS = {
    "Georgia": "https://college-football-results.com/f/georgia.htm",
    "Maryland": "https://college-football-results.com/f/maryland.htm",
    "Missouri": "https://college-football-results.com/f/missouri.htm",
    "Virginia Tech": "https://college-football-results.com/f/virgtech.htm",
    "Wisconsin": "https://college-football-results.com/f/wisconsi.htm",
}


def inspect_team(team, url):
    print(f"\n{'='*80}")
    print(team)
    print(f"{'='*80}")

    try:
        tables = pd.read_html(url)

        print(f"Found {len(tables)} tables")

        for i, table in enumerate(tables):
            print(f"\nTABLE {i}")
            print("Shape:", table.shape)
            print(table.head())

    except Exception as e:
        print(f"Error: {e}")


for team, url in TEAMS.items():
    inspect_team(team, url)
