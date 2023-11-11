import logging

# Get the logger for the sub-module
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('L5_app.log')
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def multiplier(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divider(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2
