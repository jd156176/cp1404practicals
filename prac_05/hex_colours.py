"""
CP1404 Week 5 Practical
Hex colours stored in constant dictionary
"""

NAME_TO_HEX = {"brightube": "#d19fe8", "bubblegum": "#ffc1cc", "carminepink": "eb4c42", "celadongreen": "#2f847c",
               "denim": "#1560bd", "fuzzywuzzy": "87421f", "genericveridian": "#007f66", "jazzberryjam": "#a50b5e",
               "macaroniandcheese": "fffbd88", "mysticmaroon": "#ad4379"}

colour_name = input("Enter code name: ").lower()

while colour_name != "":
    try:
        print(f"{colour_name} has hex code: {NAME_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid Colour Name.")
    colour_name = input("Enter code name: ").lower()