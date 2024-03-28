import logging
from app.commands import Command
from app.history import CalculationHistory  # Ensure this import matches your project structure

class AddCommand(Command):
    def __init__(self, history_manager=None):
        # If no history manager is provided, create a new instance
        self.history_manager = history_manager if history_manager else CalculationHistory()

    def execute(self):
        try:
            value1 = int(input('Enter the first value >> '))
            value2 = int(input('Enter the second value >> '))
            result = value1 + value2
            print(f"The sum of {value1} and {value2} is {result}")

            # Record the operation in history
            self.history_manager.add_record('Addition', value1, value2)

            logging.info(f"AddCommand executed with result: {result}")
        except ValueError:
            print("Please enter valid integers.")
            logging.error("Invalid input for AddCommand.")
