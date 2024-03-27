import sys
from app.commands import Command

class AddCommand(Command):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        result = self.value1 + self.value2
        print(value = value1 + value2)
