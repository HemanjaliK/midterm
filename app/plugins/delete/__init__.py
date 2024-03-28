import pandas as pd
import os

class HistoryManager:
    def __init__(self, filepath='history.csv'):
        self.filepath = filepath
        self.history_df = pd.DataFrame()

    def delete_history_record(self, index):
        if 0 <= index < len(self.history_df):
            self.history_df.drop(index, inplace=True)
            self.history_df.reset_index(drop=True, inplace=True)
            print(f"Record at index {index} deleted.")
        else:
            print("Invalid index.")
