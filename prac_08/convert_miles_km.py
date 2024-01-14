"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Nele Rodenhagen'

MILESTOKM = 1.6

class MilesKmApp(App):
    result = StringProperty()
    miles = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_km(self, miles):
        self.result = str(float(miles) * MILESTOKM)

    def up(self):
        try:
            self.miles = str(int(self.root.ids.input_miles.text) + 1)
        except ValueError:
            self.miles = 1

    def down(self):
        try:
            self.miles = str(int(self.root.ids.input_miles.text) - 1)
        except ValueError:
            self.miles = 1


MilesKmApp().run()
