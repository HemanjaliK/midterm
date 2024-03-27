import logging
from app.commands import Command

class AddCommand(Command):
    def execute(self):
        try:
            value1 = int(input('Enter the first value >> '))
            value2 = int(input('Enter the second value >> '))
            result = value1 + value2
            print(f"The sum of {value1} and {value2} is {result}")
            logging.info(f"AddCommand executed with result: {result}")
        except ValueError:
            print("Please enter valid integers.")
            logging.error("Invalid input for AddCommand.")
