from socket import *
import pickle
import sys
import log.client_log_config as client_log

IP_ADRESS = 'localhost'
PORT = 7777

msg = {
    "action": "presence",
    "time": "<unix timestamp>",
    "type": "status",
    "user": {
        "account_name": "my_name",
        "status":
            "Yes, I am here!"
    }
}


def get_params(ip_adress=IP_ADRESS, port=PORT):
    if __name__ == "__main__":
        if len(sys.argv) == 2:
            ip_adress = sys.argv[1]
        elif len(sys.argv) == 3:
            ip_adress = sys.argv[1]
            port = sys.argv[2]
    return {'ip_adress': ip_adress, 'port': port}


log = client_log.get_loger()


def main():
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
    main()
