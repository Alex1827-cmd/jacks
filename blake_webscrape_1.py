# Import modules
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

# Grab data from website
base_url = r"https://www.basketball-reference.com/teams/{}/stats_basic_totals.html"
team = 'ATL'

# Fetch and parse the HTML
url = base_url.format(team)
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# Find the table with stats
game_table = doc.find(id="stats")

# Remove all header rows with class 'thead'
header_rows = game_table.find_all('tr', class_='thead')
for row in header_rows:
    row.decompose()  # Ensure parentheses are added

# Convert the cleaned HTML table to a DataFrame
# Wrap the HTML string in StringIO
html_str = str(game_table)
html_file_like = StringIO(html_str)

# Read the HTML content using pd.read_html
games = pd.read_html(html_file_like)[0]

# Save the DataFrame to a CSV file
games.to_csv("games_test.csv", index=False)