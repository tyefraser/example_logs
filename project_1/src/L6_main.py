# L5_main.py

import logging
from L6_logger_config import configure_logger
from L6_sub import multiplier, divider

# Call the configure_logger function to set up logging
configure_logger()

# Get the logger for the main module
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Program started")
    multiplier(1, 5)
    divider(1, 5)
    logger.info("Program finished")
