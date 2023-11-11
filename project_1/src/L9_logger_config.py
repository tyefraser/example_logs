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
        logger = logging.getLogger()  # Consider using a specific logger name
        logger.addHandler(file_handler)


def configure_module_logger(
        logger: logging.Logger,
        script_name: str = 'missing_script',
        log_directory: str = '',
        log_level: int = logging.DEBUG):
    """
    Configure and add a file handler to the specified logger.

    Parameters:
    - logger (logging.Logger): Logger to which the file handler will be added.
    - file_path (str): Path to the log file.
    - log_level (int): Logging level (default is logging.DEBUG).
    """
    # Create a file handler with the specified log file path
    #script_name = os.path.splitext(script_name)[0]
    l = get_root_logger_folder_location(logger)
    print(l)
    log_file_path = os.path.join(log_directory, f'{script_name}.log')
    module_file_handler = logging.FileHandler(log_file_path)
    module_file_handler.setLevel(log_level)

    # Create a formatter for the file handler
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    module_file_handler.setFormatter(file_formatter)

    # Add the file handler to the logger
    logger.addHandler(module_file_handler)



# Decomission - make a LOGS_DIR and use that instead
def get_root_logger_folder_location(logger):
    """
    Get the folder location of the root logger's file handler.

    Returns:
    - str: Folder location.
    """
    # Get the root logger
    # root_logger = logging.getLogger()

    # Find the first FileHandler in the root logger's handlers
    root_file_handler = next((handler for handler in logger.handlers if isinstance(handler, logging.FileHandler)), None)

    if root_file_handler:
        # Use os.path to join path components and extract the folder location
        folder_location = os.path.dirname(root_file_handler.baseFilename)
        return folder_location
    else:
        return None
    
def logs_dir(LOGS_DIR: str = str(Path(__file__).parent.parent / "logs")):
    os.makedirs(LOGS_DIR, exist_ok=True)
    print(LOGS_DIR)
    return LOGS_DIR