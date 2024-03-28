import logging
import os
import pandas as pd
from app.commands import Command

class HistoryManager(Command):
    def __init__(self, filepath='./data/history.csv'):
        self.filepath = filepath
        # Ensure the 'data' directory exists
        data_dir = os.path.dirname(filepath)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return
        self.history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        # Load existing history if available
        self.load_history()

    def load_history(self):
        if os.path.exists(self.filepath):
            self.history_df = pd.read_csv(self.filepath)
            logging.info("History loaded successfully.")
        else:
            logging.info("No existing history file found. Starting fresh.")

    def save_history(self):
        self.history_df.to_csv(self.filepath, index=False)
        logging.info(f"History saved to '{self.filepath}'.")

    def add_to_history(self, operation, operand1, operand2, result):
        new_record = {'Operation': operation, 'Operand1': operand1, 'Operand2': operand2, 'Result': result}
        self.history_df = self.history_df.append(new_record, ignore_index=True)
        self.save_history()  # Auto-save after adding

    # Implement other methods (clear_history, delete_history_record, view_history) as needed

    def execute(self):
        # Implementation for interactive execution or specific history manipulation
        pass
