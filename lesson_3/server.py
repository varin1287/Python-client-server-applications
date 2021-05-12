from socket import *
import pickle
import sys
import argparse

PORT_DEFAULT = 7777
IP_ADRESS_DEFAULT = ''


def create_port():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=PORT_DEFAULT)
    parser.add_argument('-a', default=IP_ADRESS_DEFAULT)
    return parser


if __name__ == '__main__':
    parser = create_port()
    namespace = parser.parse_args(sys.argv[1:])
    port = namespace.p
    ip_adress = namespace.a

s = socket(AF_INET, SOCK_STREAM)
try:
    s.bind((ip_adress, int(port)))
except ValueError:
    print('Неверные параметры командной строки ')
    print('будут использованны параметры по умолчанию')
    port = PORT_DEFAULT
    ip_adress = IP_ADRESS_DEFAULT
    s.bind((ip_adress, int(port)))

s.listen(5)

while True:
    print(f'TCP-порт для работы {port}')
    if ip_adress:
        print(f'IP-адрес для прослушивания {ip_adress}')
    else:
        print(f'сервер слушает все доступные IP-адреса')
    client, addr = s.accept()
    data = client.recv(1024)

    response = {
        "response": 200,
        "action": "probe",
        "time": "< unix timestamp >",
    }
    client.send(pickle.dumps(response))
    client.close()
