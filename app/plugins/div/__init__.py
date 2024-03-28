import logging
from app.commands import Command
from app.history import CalculationHistory  # Adjust import path as needed

class DivideCommand(Command):
    def __init__(self, history_manager=None):
        # If no history manager is provided, create a new instance
        self.history_manager = history_manager if history_manager else CalculationHistory()

    def execute(self):
        try:
            value1 = int(input('Enter the dividend (value 1) >> '))
            value2 = int(input('Enter the divisor (value 2) >> '))
            
            # Check for division by zero
            if value2 == 0:
                print("Error: Division by zero is not allowed.")
                logging.error("Division by zero attempted in DivideCommand.")
                return
            
            result = value1 / value2
            print(f"The result of dividing {value1} by {value2} is {result}")

            # Record the operation in history
            self.history_manager.add_record('Division', value1, value2)

            logging.info(f"DivideCommand executed with result: {result}")
        except ValueError:
            print("Please enter valid integers.")
            logging.error("Invalid input for DivideCommand.")
