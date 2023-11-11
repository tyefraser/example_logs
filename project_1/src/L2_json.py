# Path: project_1/src/logger.py
import logging
import logging.config
import simple_maths
import datetime
import json

CONFIG = '''
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(levelname)-8s - %(message)s"
        }
    },
    "filters": {
        "warnings_and_below": {
            "()" : "__main__.filter_maker",
            "level": "WARNING"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"]
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "L2_app.log",
            "mode": "w"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stderr",
            "stdout",
            "file"
        ]
    }
}
'''

def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter

logging.config.dictConfig(json.loads(CONFIG))
logging.debug('A DEBUG message')
logging.info('An INFO message')
logging.warning('A WARNING message')
logging.error('An ERROR message')
logging.critical('A CRITICAL message')



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

# Run like this
# python main.py

# Then use:
# python main.py 2>stderr.log
# Notice the stderr.log file

# Finally:
# python main.py 2>stderr.log >stdout.log
# Note: you wont be able to see the user input using this method,
# just write 1, enter, 1, enter, 5, enter
# 
# We can see the results are as expected:
# $ more *.log
# ::::::::::::::
# app.log
# ::::::::::::::
# DEBUG    - A DEBUG message
# INFO     - An INFO message
# WARNING  - A WARNING message
# ERROR    - An ERROR message
# CRITICAL - A CRITICAL message
# ::::::::::::::
# stderr.log
# ::::::::::::::
# ERROR    - An ERROR message
# CRITICAL - A CRITICAL message
# ::::::::::::::
# stdout.log
# ::::::::::::::
# INFO     - An INFO message
# WARNING  - A WARNING message