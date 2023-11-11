# L8_main.py

import logging

from L9_logger_config import configure_logger
from L9_sub import multiplier, divider
from L9_sub_v2 import multiplier_v2

# Call the configure_logger function to set up logging
configure_logger()

# Get the logger for the main module
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Program started")

    logger.debug('MAIN: A DEBUG message')
    logger.info('MAIN: An INFO message')
    logger.warning('MAIN: A WARNING message')
    logger.error('MAIN: An ERROR message')
    logger.critical('MAIN: A CRITICAL message')
    
    multiplier(1, 5)
    multiplier_v2(2, 2)
    divider(1, 5)
    logger.info("Program finished")


