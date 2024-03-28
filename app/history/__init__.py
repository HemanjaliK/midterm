import pandas as pd
import os

class CalculationHistoryManager:

    def __init__(self, filepath='history.csv'):
        self.filepath = filepath
        # Initialize DataFrame with appropriate columns
        self.history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        self.load_history()  # Load existing history, if any

    def load_history(self):
        """Load calculation history from a CSV file."""
        if os.path.exists(self.filepath):
            self.history_df = pd.read_csv(self.filepath)
            print("History loaded successfully.")
        else:
            print("No existing history file found.")

    def save_history(self):
        """Save the current calculation history to a CSV file."""
        self.history_df.to_csv(self.filepath, index=False)
        print("History saved to file.")

    def clear_history(self):
        """Clear the current calculation history."""
        self.history_df = self.history_df.iloc[0:0]  # Clear DataFrame
        print("History cleared.")

    def delete_history_record(self, index):
        """Delete a specific record from the history."""
        if index < len(self.history_df):
            self.history_df = self.history_df.drop(self.history_df.index[index])
            print(f"Deleted record at index {index}.")
        else:
            print("Invalid index. No record deleted.")

    def add_to_history(self, operation, operand1, operand2, result):
        """Add a new calculation record to the history."""
        new_record = {
            'Operation': operation, 
            'Operand1': operand1, 
            'Operand2': operand2, 
            'Result': result
        }
        self.history_df = self.history_df.append(new_record, ignore_index=True)

    def view_history(self):
        """Print the current calculation history."""
        if self.history_df.empty:
            print("No history available.")
        else:
            print(self.history_df)

# Example of using the class in a REPL loop
def main():
    manager = CalculationHistoryManager()
    manager.add_to_history('add', 1, 2, 3)  # Example operation
    manager.save_history()
    manager.view_history()

if __name__ == '__main__':
    main()
