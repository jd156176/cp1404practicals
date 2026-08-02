"""
CP1404 Prac 8 - Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label

class DynamicLabels(App):
    label_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Charlotte", "Annabelle", "Vivianne", "Eime"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the data and add them to the GUI"""
        for name in self.names:
            temp_label = Label(text = name)
            self.root.ids.entries_box.add_widget(temp_label)

if __name__ == "__main__":
    DynamicLabels().run()