# Path: project_1/src/logger.py
import logging
import logging.config

# logger = logging.getLogger(__name__)
logger = logging.getLogger('app.sub')

logger.debug('sub_process: A DEBUG message')
logger.info('sub_process: An INFO message')
logger.warning('sub_process: A WARNING message')
logger.error('sub_process: An ERROR message')
logger.critical('sub_process: A CRITICAL message')


def multiplier(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divider(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2

