from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation, outputting result to label widget via StringProperty."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_km = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update the text input with new value, and calculate."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_validated_miles(self):
        """Get text from text entry widget, convert to float, or return 0 if invalid."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
