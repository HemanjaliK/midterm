import logging

# Define operation commands
class AdditionCommand:
    def execute(self, a, b):
        return a + b

class SubtractionCommand:
    def execute(self, a, b):
        return a - b

class MultiplicationCommand:
    def execute(self, a, b):
        return a * b

class DivisionCommand:
    def execute(self, a, b):
        if b == 0:
            return "Error: Division by zero."
        else:
            return a / b

# Menu System
class Menu:
    def __init__(self):
        self.commands = {
            '1': AdditionCommand(),
            '2': SubtractionCommand(),
            '3': MultiplicationCommand(),
            '4': DivisionCommand()
        }

    def display_menu(self):
        print("""
        Choose an arithmetic operation:
        1) Addition
        2) Subtraction
        3) Multiplication
        4) Division
        5) Exit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '5':
                print("Exiting...")
                break
            elif choice in self.commands:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = self.commands[choice].execute(a, b)
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please choose again.")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    menu = Menu()
    menu.run()
