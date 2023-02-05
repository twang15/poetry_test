# ./my_hello_world_lib/module_2.py

from lib.module_1 import add
# insteas of 
#from . import import add
import logging

logger = logging.getLogger(__name__)

def say_hello():
    logger.info('hello world!')

add(2, 2)
