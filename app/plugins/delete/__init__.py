import logging
from app.commands import Command
from app.history import CalculationHistory  # Ensure this import matches your project structure

class DeleteCommand(Command):
    def __init__(self, history_manager=None):
        # If no history manager is provided, create a new instance
        self.history_manager = history_manager if history_manager else CalculationHistory()

    def execute(self):
        try:
            # Display the current history to the user
            print("Current Calculation History:")
            print(self.history_manager.load_history())
            index = int(input('Enter the index of the record to delete >> '))

            # Perform the deletion
            self.history_manager.delete_record(index)

            logging.info(f"DeleteCommand executed, record at index {index} deleted.")
        except ValueError:
            print("Please enter a valid integer for the index.")
            logging.error("Invalid input for DeleteCommand.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Error in DeleteCommand: {e}")
