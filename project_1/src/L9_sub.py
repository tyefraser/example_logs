# L8_sub.py

import logging
from L9_logger_config import configure_module_logger
from L9_sub_v2 import multiplier_v2

# Get the logger for the sub-module
logger = logging.getLogger(__name__)

# Call the configure_module_logger function to set up logging for the sub-module
configure_module_logger(logger, __name__)

### module_logger = logging.getLogger("project_1.src.L8_sub")
### 
### module_file_handler = logging.FileHandler('L9_log.log')
### module_file_handler.setLevel(logging.DEBUG)
### 
### # Create a formatter for the file handler
### file_formatter = logging.Formatter(
###     "%(asctime)s - %(levelname)s - %(name)s - %(message)s")
### module_file_handler.setFormatter(file_formatter)
### 
### # Get the root logger and add the file handler
### # logger = logging.getLogger(__name__)  # Consider using a specific logger name
### #logger = logging.getLogger()  # Consider using a specific logger name
### module_logger.addHandler(module_file_handler)


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



def multiplier(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    #module_logger.info(f"Modile logger - Multiplying {num1} and {num2}")
    #module_logger.info(f"Multiplying {num1} and {num2}")
    multiplier_v2(num1, num2)
    return num1 * num2

def divider(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2
