# logger_config.py

import logging

def configure_logger():
    # Check if the logger has already been configured
    if not logging.getLogger().hasHandlers():
        # Configure logging only if not already configured
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

        # Create a file handler and set the file path
        file_handler = logging.FileHandler('L6_app.log')
        file_handler.setLevel(logging.INFO)

        # Create a formatter for the file handler
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler.setFormatter(file_formatter)

        # Get the root logger and add the file handler
        logger = logging.getLogger()
        logger.addHandler(file_handler)

# Call the configure_logger function when the module is imported
configure_logger()
