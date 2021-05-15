from socket import *
import pickle
import sys

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


def main():
    start_params = get_params()
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((start_params['ip_adress'], int(start_params['port'])))
    except ValueError:
        print('Неверные параметры командной строки проверьте правильность ввода')
        print('Вначале вводите ip-адрес затем tcp-порт')
        print('операция прерванна')
    except ConnectionRefusedError:
        print('Отказано в подключении, проверьте парраметры подключения')
    else:
        s.send(pickle.dumps(msg))
        data = s.recv(1024)
        print('Сообщение сервера: ', pickle.loads(data))

    s.close()

if __name__ == '__main__':
    main()

