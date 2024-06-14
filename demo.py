from us_visa_prediction.logger import logging
from us_visa_prediction.exception import USvisaException
import sys

try:
    res = 1/0
except Exception as e:
    raise USvisaException(e, sys) from e