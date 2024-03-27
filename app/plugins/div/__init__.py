import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        try:
            value1 = int(input('Enter the first value >> '))
            value2 = int(input('Enter the second value >> '))
            if value2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = value1 / value2
                print(f"The quotient of {value1} divided by {value2} is {result}")
            
            logging.info(f"DivideCommand executed with result: {result}")
        except ValueError:
            print("Please enter valid integers.")
            logging.error("Invalid input for DivideCommand.")
            