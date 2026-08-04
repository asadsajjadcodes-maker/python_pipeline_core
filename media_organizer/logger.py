import logging
# setup logging 
logging.basicConfig(
    level= logging.INFO,
    format= "%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S"
)
# gives logging a nick name 
logger = logging.getLogger(__name__)
# for info output 
def log_info(message : str) -> None:
    logger.info(message)
# for warning output 
def log_warning(message : str) -> None:
    logger.warning(message)
# for error output 
def log_error(message : str) -> None:
    logger.error(message)


