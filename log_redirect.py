import inspect
import logging
import re

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1
        message = record.getMessage()
        # remove timestamp like [19/Sep/2023 14:08:16]
        message = re.sub(r"\[\d+/\w+/\d{4} \d{2}:\d{2}:\d{2}\] ", "", message)
        # remove terminal color code
        message = re.sub(r"\x1b\[\d+m", "", message)
        message = re.sub(r"\x1b\[\d+;\d+m", "", message)
        logger.opt(depth=depth, exception=record.exc_info).log(level, message)


def redirect_logging(level="INFO"):
    logging.basicConfig(handlers=[InterceptHandler()], level=level, force=True)
