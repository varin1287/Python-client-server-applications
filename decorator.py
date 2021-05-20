from functools import wraps
import inspect
from log.log_config import get_loger


def my_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log = get_loger()
        log.debug(f'Функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return func(*args, **kwargs)

    return wrapper
