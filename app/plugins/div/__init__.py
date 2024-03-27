import logging

class DivisionCommand:
    def execute(self, a, b):
        if b == 0:
            logging.error("Error: Division by zero.")
            print("Error: Division by zero.")
        else:
            result = a / b
            logging.info(f"Division result: {result}")
            print(f"Division result: {result}")

# Example usage:
logging.basicConfig(level=logging.INFO)
div_command = DivisionCommand()
div_command.execute(8, 2)
