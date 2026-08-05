import logging

# Create the logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers: # # Prevent duplicate handlers
    #  Create the StreamHandler 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # Create the file handler 
    file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # Create the formate for log message
    log_formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S"
    )

    # Attach the log formate to the handler  
    console_handler.setFormatter(log_formatter)
    file_handler.setFormatter(log_formatter)

    # Attach the handler to the logger 
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)





# for info output 
def log_info(message : str) -> None:
    logger.info(message)
# for warning output 
def log_warning(message : str) -> None:
    logger.warning(message)
# for error output 
def log_error(message : str) -> None:
    logger.error(message)


