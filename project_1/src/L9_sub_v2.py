# L8_sub.py

import logging
from L9_logger_config import configure_module_logger

# Get the logger for the sub-module
logger = logging.getLogger(__name__)

# Call the configure_module_logger function to set up logging for the sub-module
configure_module_logger(logger, __name__)



def multiplier_v2(num1: float, num2: float) -> float:
    logger.info(f"Multiplying {num1} and {num2}")
    #module_logger.info(f"Modile logger - Multiplying {num1} and {num2}")
    #module_logger.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divider_v2(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} by {num2}")
    return num1 / num2




# Add logs to Hive

class HiveDBHandler(logging.Handler):
    def __init__(self, connection_params):
        super().__init__()
        # Initialize your Hive database connection here using connection_params

    def emit(self, record):
        # Implement the logic to insert log records into the Hive database
        log_message = self.format(record)
        
        # Example: Insert log_message into Hive database
        # hive_database_insert(log_message)

def configure_logger_with_hive_handler():
    # Create an instance of HiveDBHandler with appropriate connection parameters
    hive_handler = HiveDBHandler(connection_params={'host': 'your_hive_host', 'port': 10000, 'user': 'your_user', 'password': 'your_password', 'database': 'your_database'})

    # Create a formatter for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    hive_handler.setFormatter(formatter)

    # Get the root logger and add the HiveDBHandler
    root_logger = logging.getLogger()
    root_logger.addHandler(hive_handler)

if __name__ == "__main__":
    # Configure the logger with the HiveDBHandler
    configure_logger_with_hive_handler()

    # Log some messages
    logging.info('This log message will be stored in the Hive database.')
    logging.warning('Another warning message for testing.')




# to do for SQL logger


import logging
import mysql.connector
from mysql.connector import errorcode

def configure_logger(series, pool, payment_date, runtime, log_to_database=False, database_config=None):
    log_folder = f"logs/{series}/{pool}"
    log_file = f"{log_folder}/run_{pool}_{payment_date}_{runtime}.log"

    # Create log folder if it doesn't exist
    os.makedirs(log_folder, exist_ok=True)

    # Configure the logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a file handler and set the formatter
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a database connection
    if log_to_database and database_config:
        conn = create_mysql_connection(database_config)
        create_logs_table(conn)
        database_handler = MySQLHandler(conn)
        database_handler.setFormatter(formatter)
        logger.addHandler(database_handler)
        return logger, conn
    else:
        return logger, None

def create_mysql_connection(config):
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
        raise

def create_logs_table(conn):
    # Create a 'logs' table in the database if it doesn't exist
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                series VARCHAR(255),
                pool VARCHAR(255),
                payment_date VARCHAR(255),
                runtime VARCHAR(255),
                log_level VARCHAR(10),
                message TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    conn.commit()

class MySQLHandler(logging.Handler):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def emit(self, record):
        log_entry = {
            'series': record.series,
            'pool': record.pool,
            'payment_date': record.payment_date,
            'runtime': record.runtime,
            'log_level': record.levelname,
            'message': record.msg
        }

        with self.conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO logs (series, pool, payment_date, runtime, log_level, message)
                VALUES (%(series)s, %(pool)s, %(payment_date)s, %(runtime)s, %(log_level)s, %(message)s)
            ''', log_entry)

        self.conn.commit()

# Example usage:
if __name__ == "__main__":
    series = "example_series"
    pool = "example_pool"
    payment_date = "2023-11-10"
    runtime = "1"

    # MySQL database configuration
    db_config = {
        'host': 'your_mysql_host',
        'user': 'your_mysql_user',
        'password': 'your_mysql_password',
        'database': 'your_mysql_database'
    }

    # Create logger instance
    logger, database_conn = configure_logger(series, pool, payment_date, runtime, log_to_database=True, database_config=db_config)

    # Log some messages
    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

    # Close the database connection if applicable
    if database_conn:
        database_conn.close()
