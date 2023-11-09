import logging

logger = logging.getLogger('calculator_project.simple_maths')

def multiplier(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divider(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2