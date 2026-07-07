"""
Wimbledon
Estimated Time: 45 minutes
Actual Time: 40 minutes
"""

FILENAME = "wimbledon.csv"
CHAMPION_COUNTRY_COLUMN = 1
CHAMPION_NAME_COLUMN = 2

def load_file(filename):
    """Load the data from the CSV file."""
    champions = []
    with open(filename, "r", encoding = "utf-8-sig") as in_file:
        in_file.readline()  # Remove CSV header row
        for line in in_file:
            parts = line.strip().split(",")
            champions.append(parts)

    return champions

def main():
    """Run the main Wimbledon program."""
    champions = load_file(FILENAME)
    champion_to_count, countries = calculate_champion_counts(champions)
    display_results(champion_to_count, countries)

def calculate_champion_counts(champions):
    """Calculate a dictionary of champion names to number of wins."""
    champion_to_count = {}
    countries = set()
    for champion in champions:
        countries.add(champion[CHAMPION_COUNTRY_COLUMN])
        try:
            champion_to_count[champion[CHAMPION_NAME_COLUMN]] += 1
        except KeyError:
            champion_to_count[champion[CHAMPION_NAME_COLUMN]] = 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Displays Champions and Countries."""
    print("Wimbledon Champions: ")

    for name, count in champion_to_count.items():
        print(name, count)
    print()
    print(f"These {len(countries)} have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()