from app.commands import Command
from app.history import CalculationHistory  # Adjust the import path as necessary

class LoadHistoryCommand(Command):
    def __init__(self, history_manager=None):
        # If no history manager is provided, create a new instance
        self.history_manager = history_manager if history_manager else CalculationHistory()

    def execute(self):
        history_df = self.history_manager.load_history()
        if history_df.empty:
            print("No history records found.")
        else:
            print("Calculation History:")
            print(history_df.to_string(index=False))
