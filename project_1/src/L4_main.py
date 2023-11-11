# Path: project_1/src/logger.py
import logging
import logging.config
import L4_sub
import datetime

# get date and time in a string format for the log file name
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

# define formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# define handlers
s_handler = logging.StreamHandler()
s_handler.setFormatter(formatter) # add formatter to handler
# s_handler.setLevel(logging.INFO) # can set level here
f_handler = logging.FileHandler(f'L4_logs_{date_time}.log')
f_handler.setFormatter(formatter) # add formatter to handler
f_handler.setLevel(logging.INFO)

# add handlers to logger
logger.addHandler(s_handler)
logger.addHandler(f_handler)

logger.debug('A DEBUG message')
logger.info('An INFO message')
logger.warning('A WARNING message')
logger.error('An ERROR message')
logger.critical('A CRITICAL message')


# Define functions
def add_numbers(num1: float, num2: float) -> float:
    logging.info(f"Adding {num1} and {num2}")
    return num1 + num2

def subtract_numbers(num1: float, num2: float) -> float:
    logging.info(f"Subtracting {num2} from {num1}")
    return num1 - num2

def multiply_numbers(num1: float, num2: float) -> float:
    logging.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divide_numbers(num1: float, num2: float) -> float:
    logging.info(f"Dividing {num1} by {num2}")
    return num1 / num2

def main():
    logging.info("Welcome to the calculator!")    
    print("Welcome to the calculator!")
    print("Please enter two numbers")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print("What would you like to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Multiply (using L4_sub)")
    print("6. Divide (using L4_sub)")
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
        result = L4_sub.multiplier(num1, num2)
        print(f"Result: {result}")
    elif choice == 6:
        result = L4_sub.divider(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice!")
    

if __name__ == "__main__":
    logger.info("Program started")
    main()
    logger.info("Program finished")
