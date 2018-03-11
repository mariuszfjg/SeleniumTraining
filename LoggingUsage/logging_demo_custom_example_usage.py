import logging
from logging_demo_custom import custom_logger as cl


class LoggingDemo2:

    LOGGER = cl(log_level=logging.DEBUG)

    def method1(self):
        self.LOGGER.debug("Example for debug message")
        self.LOGGER.info("Example for info message")
        self.LOGGER.warning("Example for warning message")
        self.LOGGER.error("Example for error message")
        self.LOGGER.critical("Example for critical message")

    def method2(self):
        m2_logger = cl(log_level=logging.INFO)
        m2_logger.debug("Example for debug message")
        m2_logger.info("Example for info message")
        m2_logger.warning("Example for warning message")
        m2_logger.error("Example for error message")
        m2_logger.critical("Example for critical message")

    def method3(self):
        m3_logger = cl(log_level=logging.CRITICAL)
        m3_logger.debug("Example for debug message")
        m3_logger.info("Example for info message")
        m3_logger.warning("Example for warning message")
        m3_logger.error("Example for error message")
        m3_logger.critical("Example for critical message")


def main():
    demo2 = LoggingDemo2()
    demo2.method1()
    demo2.method2()
    demo2.method3()


if __name__ == '__main__':
    main()
