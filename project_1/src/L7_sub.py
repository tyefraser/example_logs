# L5_sub.py

import logging
from L7_logger_config import configure_logger

# Call the configure_logger function to set up logging
configure_logger()

# Get the logger for the sub-module
logger = logging.getLogger(__name__)

def multiplier(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divider(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2
