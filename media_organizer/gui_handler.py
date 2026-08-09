import logging


class GuiHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        message = self.format(record)
        print(f"GUI: {message}")
        