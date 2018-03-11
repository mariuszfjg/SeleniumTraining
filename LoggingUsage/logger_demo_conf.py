import logging
import logging.config


class LoggerDemoConf:
    def __init__(self):
        self.logger = None

    def test_log(self):
        # create logger
        self.initialize_logger_with_conf_file('demo_log.conf')

        # log messages
        self.test_messages()

    def initialize_logger_with_conf_file(self, log_configuration_file_name):
        logging.config.fileConfig(log_configuration_file_name)
        self.logger = logging.getLogger(LoggerDemoConf.__name__)

    def test_messages(self):
        self.logger.debug("debug message")
        self.logger.info("info message")
        self.logger.warning("warning message")
        self.logger.error("error message")
        self.logger.critical("critical message")


def main():
    logger_demo_conf = LoggerDemoConf()
    logger_demo_conf.test_log()


if __name__ == '__main__':
    main()
