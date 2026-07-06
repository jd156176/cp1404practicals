"""
Wimbledon
Estimated Time: 45 minutes
Actual Time:
"""

FILENAME = "wimbledon.csv"
CHAMPION_COUNTRY_COLUMN = 1
CHAMPION_NAME_COLUMN = 2

def load_file(filename):
    """Load the data from the CSV file."""
    champions = []
    with open(filename, "r", encoding = "utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split("")

            champion_parts = [parts[CHAMPION_COUNTRY_COLUMN], parts[CHAMPION_NAME_COLUMN]]
            champions.append(champion_parts)

    return champions

def main():
    """Run the main Wimbledon program."""
    load_file(FILENAME)

def calculate_champion_counts(champions):
    """Calculate a dictionary of champion names to number of wins."""
    champion_to_count = {}
    countries = set()
    for country, name in champions:
        champion_to_count[name] = champion_to_count.get(name, 0) + 1

main()