"""
CP1404/CP5632 - Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            # using pass tell python do nothing so previous answer remains
            # using this down here will tell python to return a blank which is better
            self.root.ids.output_label.text = ""


SquareNumberApp().run()
