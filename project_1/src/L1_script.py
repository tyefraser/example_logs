# Path: project_1/src/logger.py
import logging
import simple_maths
import datetime

# get date and time in a string format for the log file name
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
# create logger with 'calculator_project'
logger = logging.getLogger('calculator_project')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(f'L1_calculator_{date_time}.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO) # logging.ERROR
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

rt = logging.FileHandler('L1_calculator.log')
rt.setLevel(logging.DEBUG)
rt.setFormatter(formatter)
logging.getLogger('').addHandler(rt)

def add_numbers(num1: float, num2: float) -> float:
    logger.info(f"Adding {num1} and {num2}")
    logger.info(f"Adding {num1} and {num2}")
    return num1 + num2

def subtract_numbers(num1: float, num2: float) -> float:
    logger.info(f"Subtracting {num2} from {num1}")
    return num1 - num2

def multiply_numbers(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divide_numbers(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2

def main():
    logger.info("Welcome to the calculator!")    
    print("Welcome to the calculator!")
    print("Please enter two numbers")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print("What would you like to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Multiply (using simple_maths)")
    print("6. Divide (using simple_maths)")
    choice = int(input("Your choice: "))
    if choice == 1:
        result = add_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 2:
        result = subtract_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 3:
        result = multiply_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 4:
        result = divide_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 5:
        result = simple_maths.multiplier(num1, num2)
        print(f"Result: {result}")
    elif choice == 6:
        result = simple_maths.divider(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice!")
    
if __name__ == "__main__":
    main()

