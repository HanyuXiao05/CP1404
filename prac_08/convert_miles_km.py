from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class ConvertMilesToKm(App):
    """Main program - Box Layout of kivy."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, text):
        """Convert the miles to km"""
        miles = self.convert_to_number(text)
        self.update_label(miles)

    @staticmethod
    def convert_to_number(text):
        """convert text to float,return 0.0 if invalid"""
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_increment(self, text, number_of_change):
        """increase the number of input label"""
        miles = self.convert_to_number(text) + number_of_change
        self.root.ids.input_text.text = str(miles)

    def update_label(self, miles):
        """update the output label"""
        self.output_km = str(miles * CONVERSION_FACTOR)


ConvertMilesToKm().run()
