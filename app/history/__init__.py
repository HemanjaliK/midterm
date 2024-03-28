import pandas as pd
import os

class CalculationHistory:
    # Corrected the initialization method name from _init_ to __init__
    def __init__(self, csv_file='./data/cal_history.csv'):
        self.csv_file = csv_file
        # Make sure the data directory exists
        os.makedirs(os.path.dirname(csv_file), exist_ok=True)
        self.history_df = self.load_history()

    def load_history(self):
        if os.path.exists(self.csv_file):
            try:
                return pd.read_csv(self.csv_file)
            except Exception as e:
                print(f"Error loading history from CSV: {e}")
                return pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])
        else:
            return pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])

    def save_history(self):
        try:
            self.history_df.to_csv(self.csv_file, index=False)
            print(f"History saved to CSV at '{self.csv_file}'.")
        except Exception as e:
            print(f"Error saving history to CSV: {e}")

    def add_record(self, operation, value1, value2):
        # Create a new DataFrame for the record to be added
        new_record_df = pd.DataFrame([[operation, value1, value2]], columns=['Operation', 'Value1', 'Value2'])
        # Append the new record to the existing DataFrame
        self.history_df = pd.concat([self.history_df, new_record_df], ignore_index=True)
        # Save updated history
        self.save_history()

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])
        # Optionally, also save the cleared history to CSV to reflect the changes immediately
        self.save_history()

    def delete_record(self, index):
        try:
            # Ensure the index is within the DataFrame's range
            if index in self.history_df.index:
                self.history_df.drop(index=index, inplace=True)
                self.save_history()  # Save after deleting the record
                print(f"Record at index {index} deleted from history.")
            else:
                print(f"Index {index} not found in history.")
        except Exception as e:
            print(f"Error deleting record from history: {e}")
