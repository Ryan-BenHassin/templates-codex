import logging

class LoggingService:
    def __init__(self, log_file='app.log', level='DEBUG'):
        self.log_file = log_file
        self.level = level
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename=self.log_file, level=getattr(logging, self.level))
        logging.debug('Logging has been initialized')

    def info(self, message):
        logging.info(message)

    def debug(self, message):
        logging.debug(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)


service = LoggingService()
service.info('This is an info message')
service.debug('This is a debug message')
service.warning('This is a warning message')
service.error('This is an error message')
service.critical('This is a critical message')