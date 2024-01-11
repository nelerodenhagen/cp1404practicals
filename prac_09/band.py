"""
Band class
"""
from prac_09.musician import Musician


class Band:

    def __init__(self, name=""):
        """Construct a Musician with a name and empty instrument collection."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.members})"

    def add(self, musician):
        """Add a member to the band"""
        self.members.append(musician)

    def play(self):
        """Return a string showing the members and the instrument playing their first (or no) instrument."""
        for member in self.members:
            print(member.play())
