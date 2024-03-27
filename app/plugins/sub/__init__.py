import logging
from app.commands import Command

class SubtractionCommand(Command):
    def execute(self):
        try:
            value1 = int(input('Enter the first value >> '))
            value2 = int(input('Enter the second value >> '))
            result = value1 - value2
            print(f"The difference between {value1} and {value2} is {result}")
            logging.info(f"SubtractionCommand executed with result: {result}")
        except ValueError:
            print("Please enter valid integers.")
            logging.error("Invalid input for SubtractionCommand.")
            