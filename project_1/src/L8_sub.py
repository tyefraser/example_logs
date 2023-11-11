# L8_sub.py

import logging

# Get the logger for the sub-module
logger = logging.getLogger(__name__)


def multiplier(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")    
    #module_logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divider(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2


# from L8_logger_config import configure_logger

# Call the configure_main_logger function to set up logging for the main module
# configure_logger()
# 

# 
# 
# main_handlers = logger.handlers
# 
# main_file_handler = None
# for handler in main_handlers:
#     if isinstance(handler, logging.FileHandler):
#         main_file_handler = handler
#         print(f'Found the main_file_handler: {main_file_handler}')
#         break

# Check if the main_file_handler is found
# if main_file_handler:
#     folder_location = main_file_handler.baseFilename.rsplit('/', 1)[0]
#     print("Found the folder:v")
#     print(folder_location)
#     print("Found the folder:^")
# 
#     # Call the configure_sub_logger function to set up logging for the sub-module
#     #configure_sub_logger(folder_location)
# 
#     # Get the logger for the sub-module
#     module_logger = logging.getLogger(__name__)
