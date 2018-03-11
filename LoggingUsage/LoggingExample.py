import logging

path = 'C:\\Users\\mariu\\Desktop\\'
log_file_name = "test_log.txt"

logging.basicConfig(filename=path + log_file_name,
                    level=logging.DEBUG)


def main():
    logging.debug("Example for debug message")
    logging.info("Example for info message")
    logging.warning("Example for warning message")
    logging.error("Example for error message")
    logging.critical("Example for critical message")


if __name__ == '__main__':
    main()
