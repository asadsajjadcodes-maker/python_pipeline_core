import logging

# Create the logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#  Create the StreamHandler 
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create the formate for log message
log_formate = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S"
)

# Attach the log formate to the handler  
console_handler.setFormatter(log_formate)

# Attach the handler to the logger 
logger.addHandler(console_handler)





# for info output 
def log_info(message : str) -> None:
    logger.info(message)
# for warning output 
def log_warning(message : str) -> None:
    logger.warning(message)
# for error output 
def log_error(message : str) -> None:
    logger.error(message)


