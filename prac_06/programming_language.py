"""
CP1404
estimated time: 15 Minutes
needed time: 12 Minutes
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="Static", reflection=True , year=0):
        self.name = name
        self.typing = typing.lower()
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, {self.reflection}, {self.year}"

    def is_dynamic(self):
        if self.typing == "dynamic":
            return True
        else:
            return False

