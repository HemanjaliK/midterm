import logging

class SubtractionCommand:
    def execute(self, a, b):
        result = a - b
        logging.info(f"Subtraction result: {result}")
        print(f"Subtraction result: {result}")

# Example usage:
logging.basicConfig(level=logging.INFO)
sub_command = SubtractionCommand()
sub_command.execute(3, 1)
