import pandas as pd
import os

class HistoryManager:
    def __init__(self, filepath='history.csv'):
        self.filepath = filepath
        self.history_df = None
        self.load_history()

    def load_history(self):
        if os.path.exists(self.filepath):
            self.history_df = pd.read_csv(self.filepath)
            print("History loaded successfully.")
        else:
            print("History file not found. Starting with an empty DataFrame.")
            self.history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

