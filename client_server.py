from socket import *
import pickle
import sys
import log.log_config as client_log
from datetime import datetime
from functools import wraps
import inspect

IP_ADRESS = 'localhost'
PORT = 7777


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(f'Функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return func(*args, **kwargs)

    return wrapper


@log
def get_params(ip_adress=IP_ADRESS, port=PORT):
    if len(sys.argv) == 2:
        ip_adress = sys.argv[1]
    elif len(sys.argv) == 3:
        ip_adress = sys.argv[1]
        port = sys.argv[2]
    return {'ip_adress': ip_adress, 'port': port}


def main(msg):
    start_params = get_params()
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((start_params['ip_adress'], int(start_params['port'])))
    except ValueError as e:
        log.warning(f'описание ошибки: {e}')
        log.info('операция прерванна')
        log.info('Неверные параметры командной строки проверьте правильность ввода')
        log.info('Вначале вводите ip-адрес затем tcp-порт')

    except ConnectionRefusedError as e:
        log.warning(f'описание ошибки: {e}')
        log.info('Отказано в подключении, проверьте парраметры подключения')
    except Exception as e:
        log.warning(f'неучтенная ошибка: {e}')
    else:
        s.send(pickle.dumps(msg))
        data = s.recv(1024)
        print('Сообщение сервера: ', pickle.loads(data))

    s.close()


if __name__ == '__main__':
    log = client_log.get_loger()
    msg = {
        "action": "presence",
        "time": datetime.now(),
        "type": "status",
        "user": {"account_name": "my_name", "status": "Yes, I am here!"}
    }

    main(msg)

'''
    msg_list = []

    msg_list.append({
        "action": "presence",
        "time": datetime.now(),
        "type": "status",
        "user": {"account_name": "my_name", "status": "Yes, I am here!"}
    })

    msg_list.append({
        "action": "create",
        "time": datetime.now(),
        "type": "status",
        "user": {"account_name": "my_name", "status": "Yep, I am here!"},
    })

    msg_list.append({
        "action": "quit",
        "time": datetime.now(),
        "type": "status",
        "user": {"account_name": "my_name", "status": "Yep, I am here!"},
    })

    msg_list.append({
        "action": "server_not_this_command",
        "time": datetime.now(),

    })

    # Длинна текста больше допустимой
    import random
    import string

    def generate_random_string(length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    long_str = generate_random_string(700)

    msg_list.append({
        "action": "presence",
        "time": datetime.now(),
        "type": "status",
        "user": {"account_name": "my_name", "status": f"very long text Yep, I am here! {long_str} "},
    })

    print('пользователь отсутствует "action": "presence" ')
    main(msg_list[0])
    print('пользователь отсутствует "action": "create" ')
    main(msg_list[1])
    print('пользователь зарегестрированн "action": "presence" ')
    main(msg_list[0])
    print('пользователь зарегестрированн "action": "create" ')
    main(msg_list[1])
    print('пользователь зарегестрированн "action": "quit" ')
    main(msg_list[2])
    print('пользователь отсутствует "action": "quit" ')
    main(msg_list[2])
    print('неизвестная команда')
    main(msg_list[3])
    print('очень длинный текст')
    main(msg_list[4])
'''
