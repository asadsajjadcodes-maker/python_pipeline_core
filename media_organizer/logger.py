import logging
from gui_handler import GuiHandler

# Create or retrieve the central application logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Shared GUI handler instance so main window can connect to its signal
gui_handler = GuiHandler()
gui_handler.setLevel(logging.INFO)

# Prevent attaching duplicate handlers on multiple imports
if not logger.handlers:

    # 1. Console Stream Handler (Outputs logs to standard terminal output)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 2. File Handler (Appends logs into a local log file)
    file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # Define unique formatters for each output target
    console_formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    file_formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(filename)s]:%(funcName)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    gui_formatter = logging.Formatter(
        fmt="[%(levelname)s] %(message)s"
    )

    # Attach formatters to respective handlers
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)
    gui_handler.setFormatter(gui_formatter)

    # Attach all three handlers to enable triple logging (Console, File, GUI)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(gui_handler)


# Helper wrapper functions for logging across modules
def log_info(message: str) -> None:
    """Log informational messages."""
    logger.info(message)

def log_warning(message: str) -> None:
    """Log warning messages."""
    logger.warning(message)

def log_error(message: str) -> None:
    """Log error messages."""
    logger.error(message)