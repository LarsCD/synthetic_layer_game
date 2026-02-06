import datetime
import logging
import sys
from pathlib import Path

class DevLogger:
    def __init__(self, logging_class, log_level=logging.DEBUG, print_level=logging.INFO):
        """
        logging_class: class object, not instance
        log_level: file + internal log level
        print_level: console verbosity level
        """

        self.logger_enabled = True
        self.class_name = logging_class.__name__
        self.logger_name = f"DEV::{self.class_name}"

        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(log_level)

        # Prevent duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers(log_level, print_level)

        # Prevent propagation to root logger (avoids duplicate logs)
        self.logger.propagate = False
        Path("logs/dev.log").open("a").write(f'\n======================== [{datetime.datetime.now().strftime("%a %d %b %Y at %H:%M:%S")}] ========================\n')

    def _setup_handlers(self, log_level, print_level):
        formatter = logging.Formatter(
            "[%(levelname)s][%(asctime)s]: %(name)s > %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console handler
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(print_level)
        console.setFormatter(formatter)

        # File handler
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "dev.log")
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file_handler)

    # REQUIRED API
    def log(self, level, message):
        if self.logger_enabled:
            self.logger.log(level, message)

    def separator(self, text):
        for h in self.logger.handlers:
            if isinstance(h, logging.FileHandler):
                h.emit(logging.LogRecord(
                    name=self.logger.name,
                    level=logging.INFO,
                    pathname="",
                    lineno=0,
                    msg=text,
                    args=None,
                    exc_info=None
                ))
