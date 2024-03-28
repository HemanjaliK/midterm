import pandas as pd
import os

class HistoryManager:
    def __init__(self, filepath='history.csv'):
        self.filepath = filepath
        self.history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=self.history_df.columns)
        print("History cleared.")
        