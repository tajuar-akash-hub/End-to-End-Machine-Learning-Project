from us_visa.logger import logging 
from us_visa.exception import USvisaException
import sys


# logging.info("This is a log message")

try: 
    r= 3/0
except Exception as e:
    logging.info((e))
    raise USvisaException(e, sys)