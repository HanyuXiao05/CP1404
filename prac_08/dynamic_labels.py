from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamic labels creation."""

    def __init__(self):
        """Construct main app."""
        super().__init__()
        self.names = [
            "James", "John", "Robert", "Michael", "William",
            "David", "Richard", "Joseph", "Charles", "Thomas"
        ]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (1,1,0,1)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
