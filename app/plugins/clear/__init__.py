import logging
from app.commands import Command
from app.history import CalculationHistory  # Ensure this import matches your project structure

class ClearHistoryCommand(Command):
    def __init__(self, history_manager=None):
        # If no history manager is provided, create a new instance
        self.history_manager = history_manager if history_manager else CalculationHistory()

    def execute(self):
        # Simply call the clear_history method of CalculationHistory
        self.history_manager.clear_history()
        print("Calculation history has been cleared.")
        logging.info("ClearHistoryCommand executed: History cleared.")
