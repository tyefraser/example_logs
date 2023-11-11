# L8_main.py

import logging

from L8_logger_config import configure_logger
from L8_sub import multiplier, divider

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
    divider(1, 5)
    logger.info("Program finished")



