from src.exception import CustomException
import sys
from src.logger import logging

def test_logger_and_exception():
    try:
        logging.info("Testing logger setup...")
        logging.info("This is a test log message.")

        # Raise a test exception
        raise CustomException("Test Exception", sys)

    except CustomException as ce:
        logging.error(ce)
        print(str(ce))

if __name__ == "__main__":
    test_logger_and_exception()