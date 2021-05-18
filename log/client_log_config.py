import logging


def to_stream_log():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    _log_format = '%(message)s'
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def to_file_log():
    file_handler = logging.FileHandler('log/client.log')
    file_handler.setLevel(logging.WARNING)
    _log_format = '%(asctime)s  %(levelname) - 10s  %(module)s   %(message)s'
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_loger():
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(to_stream_log())
    log.addHandler(to_file_log())
    return log
