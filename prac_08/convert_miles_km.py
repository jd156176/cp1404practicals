"""
CP1404 - Prac 8
Miles to Kilometer Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKilometer(App):
    #declare the StringProperty that the KV file will listen to
    result_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the KV file"""
        self.title = "Miles to Kilometer Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self, text_input):
        """Convert miles input to kilometers and update the StringProperty"""
        try:
            miles = float(text_input)
            km = miles * MILES_TO_KM
            self.result_text = str(km)
        except ValueError:
            self.result_text = "0.0"

    def handle_increment(self, text_input, change):
        """Increment of decrement input value safely and return string result."""
        miles = self.get_valid_miles(text_input) + change
        return str(miles)

    @staticmethod
    def get_valid_miles(text):
        """Safely convert text input to float, defaulting to 0.0 on an error."""
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == "__main__":
    ConvertMilesKilometer().run()