import pandas as pd
from app.commands import Command

class HistoryManager(Command):
    def __init__(self, filepath='history.csv'):
        self.history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        self.filepath = filepath

    def load_history(self):
        try:
            self.history_df = pd.read_csv(self.filepath)
            print("History loaded successfully.")
        except FileNotFoundError:
            print("History file does not exist.")

    def save_history(self):
        self.history_df.to_csv(self.filepath, index=False)
        print("History saved successfully.")

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        print("History cleared.")

    def delete_history_record(self, index):
        try:
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            print(f"Record {index} deleted successfully.")
        except KeyError:
            print("Invalid index. No record deleted.")

    def add_to_history(self, operation, operand1, operand2, result):
        new_record = {'Operation': operation, 'Operand1': operand1, 'Operand2': operand2, 'Result': result}
        self.history_df = self.history_df.append(new_record, ignore_index=True)

    def view_history(self):
        print(self.history_df)
