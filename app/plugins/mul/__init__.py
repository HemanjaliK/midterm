import logging

class MultiplicationCommand:
    def execute(self, a, b):
        result = a * b
        logging.info(f"Multiplication result: {result}")
        print(f"Multiplication result: {result}")

# Example usage:
logging.basicConfig(level=logging.INFO)
mul_command = MultiplicationCommand()
mul_command.execute(4, 2)
