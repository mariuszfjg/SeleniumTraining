import logging


class LoggerDemoConsole:
    def __init__(self):
        self.logger = None
        self.console_handler = None
        self.formatter = None

    def test_log(self):
        self.initialize_logger(log_name=LoggerDemoConsole.__name__,
                               log_level=logging.INFO)

        self.initialize_console_handler(log_level=logging.INFO)

        self.initialize_formatter()
        self.add_formatter_to_console_handler()
        self.add_console_handler_to_logger()

        self.test_messages()

    def initialize_logger(self, log_name, log_level):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)

    def initialize_console_handler(self, log_level):
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(log_level)

    def initialize_formatter(self):
        self.formatter = logging.Formatter('%(asctime)s - '
                                           '%(name)s - '
                                           '%(levelname)s: '
                                           '%(message)s',
                                           datefmt='%d/%m/%Y '
                                                   '%H:%M:%S')

    def add_formatter_to_console_handler(self):
        self.console_handler.setFormatter(self.formatter)

    def add_console_handler_to_logger(self):
        self.logger.addHandler(self.console_handler)

    def test_messages(self):
        self.logger.debug("Example for debug message")
        self.logger.info("Example for info message")
        self.logger.warning("Example for warning message")
        self.logger.error("Example for error message")
        self.logger.critical("Example for critical message")

def main():
    logger_demo_console = LoggerDemoConsole()
    logger_demo_console.test_log()


if __name__ == '__main__':
    main()
