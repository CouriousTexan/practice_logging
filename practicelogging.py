import logging
import datetime

# Create and configure logger [WARNING: hard coded]
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:/data/lumberjack.log", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

# Test the logger
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")