import logging
import logging.config
import datetime

from L5_sub import multiplier, divider

# Configure logging in the main module
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# Get the logger for the main module
logger = logging.getLogger(__name__)

# Create a file handler and set the file path
file_handler = logging.FileHandler('L5_app.log')
file_handler.setLevel(logging.INFO)

# Create a formatter for the file handler
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

if __name__ == "__main__":
    logger.info("Program started")
    multiplier(1, 5)
    divider(1, 5)
    logger.info("Program finished")
