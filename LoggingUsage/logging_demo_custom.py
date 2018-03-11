import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    logger.setLevel(log_level)

    file_handler = logging.FileHandler(filename='{0}.log'
                                       .format(logger_name),
                                       mode='w'
                                       )
    formatter = logging.Formatter('%(asctime)s - '
                                  '%(name)s - '
                                  '%(levelname)s'
                                  ': %(message)s',
                                  datefmt='%d/%m/%Y %H:%M:%S'
                                  )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def main():
    pass


if __name__ == '__main__':
    main()
