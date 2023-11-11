# logger_config.py
import datetime
import logging
import os
from pathlib import Path

def configure_logger(
        arg_series: str = 'missing_series',
        arg_pool: str = 'missing_pool',
        LOGS_DIR: str = str(Path(__file__).parent.parent / "logs"),
        # custom_file_handler: logging.Handler = None,
        # custom_formatter: logging.Formatter = None,
        log_level: int = logging.DEBUG) -> None:
    
    # Check if the logger has already been configured
    if not logging.getLogger().hasHandlers():

        # Create a directory for the logs based on arguments
        log_dir = os.path.join(LOGS_DIR, str(arg_series), str(arg_pool))
        os.makedirs(log_dir, exist_ok=True)

        # Configure logging only if not already configured
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

        # Create a file handler with the dynamically generated log file path                
        date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        log_file = f'L8_logs_{date_time}.log'
        log_file_path = os.path.join(log_dir, log_file)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter for the file handler
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler.setFormatter(file_formatter)

        # Get the root logger and add the file handler
        # logger = logging.getLogger(__name__)  # Consider using a specific logger name
        logger = logging.getLogger()  # Consider using a specific logger name
        logger.addHandler(file_handler)

# Call the configure_logger function when the module is imported
# configure_logger()