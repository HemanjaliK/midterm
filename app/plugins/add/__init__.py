import logging

class AdditionCommand:
    def execute(self, a, b):
        result = a + b
        logging.info(f"Addition result: {result}")
        print(f"Addition result: {result}")

# Example usage:
logging.basicConfig(level=logging.INFO)
add_command = AdditionCommand()
add_command.execute(1, 2)
