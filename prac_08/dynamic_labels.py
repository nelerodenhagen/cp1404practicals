"""
Kivy for CP1404
Dynamically create labels
Nele Rodenhagen
"""

from kivy.app import App
from kivy.core.text import Label
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Nele', 'Tom', 'Ralf', 'Tina']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.main.clear_widgets()


DynamicLabelsApp().run()
