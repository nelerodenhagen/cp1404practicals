"""
CP1404 Practical
Project class
"""
import datetime


class Project:

    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {datetime.datetime.strftime(self.start_date, "%d/%m/%y")}, priority "
                f"{self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def update(self, new_completion, new_priority):
        self.completion = new_completion
        self.priority = new_priority
