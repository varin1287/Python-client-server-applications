from socket import *
import pickle
import sys
import argparse
import log.server_log_config as server_log
from datetime import datetime

PORT_DEFAULT = 7777
IP_ADRESS_DEFAULT = ''

authorized_users = []


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=PORT_DEFAULT)
    parser.add_argument('-a', default=IP_ADRESS_DEFAULT)
    return parser


def get_socket(ip_adress, port):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind((ip_adress, int(port)))
    except Exception as e:
        log.warning(f'описание ошибки: {e}')
        log.info('будут использованны параметры по умолчанию')
        port = PORT_DEFAULT
        ip_adress = IP_ADRESS_DEFAULT
        s.bind((ip_adress, int(port)))
    s.listen(5)
    return s


def checking_data(message):
    if len(message) > 640:
        return {
            "response": 400,
            "time": datetime.now(),
            "error": "Длина текста больше 640 символов",
        }

    dict_of_commands = {
        "presence": presence,
        "quit": log_out_chat,
        "create": add_user_in_chat,
    }
    data = pickle.loads(message)
    action = data["action"]
    if action not in dict_of_commands:
        return {"response": 404, "time": datetime.now(), "error": f"Неизвестная команда {action}"}
    processing_the_action = dict_of_commands[action]
    return processing_the_action(**data)


def add_user_in_chat(**kwargs):
    user_name = kwargs["user"]["account_name"]
    if user_name in authorized_users:
        return {
            "response": 409,
            "time": datetime.now(),
            "error": f"Пользователь {user_name} уже присутствует в чате ",
        }
    authorized_users.append(user_name)
    return {
        "response": 200,
        "time": datetime.now(),
        "alert": f"Пользователь {user_name} добавлен в чат ",
    }


def presence(**kwargs):
    user_name = kwargs["user"]["account_name"]
    if user_name in authorized_users:
        return {
            "response": 200,
            "time": datetime.now(),
            "alert": f"Хорошо, {user_name} присутсвует в списке подключенных пользователей",
        }
    return {"response": 404, "time": datetime.now(), "error": f"пользователь {user_name} отсутствует на сервере"}


def log_out_chat(**kwargs):
    user_name = kwargs["user"]["account_name"]
    if user_name in authorized_users:
        authorized_users.remove(user_name)
        return {"response": 200, "time": datetime.now(), "alert": f"Пользователь {user_name} вышел из чата"}
    return {"response": 404, "time": datetime.now(),
            "error": f"Пользователь {user_name} не входил в чат или вышел из чата ранее"}


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    port = namespace.p
    ip_adress = namespace.a

    s = get_socket(ip_adress, port)

    while True:
        log.info(f'TCP-порт для работы {port}')
        if ip_adress:
            log.info(f'IP-адрес для прослушивания {ip_adress}')
        else:
            log.info(f'сервер слушает все доступные IP-адреса')
        client, addr = s.accept()
        data = client.recv(1024)

        response = checking_data(data)
        client.send(pickle.dumps(response))
        client.close()
        print(authorized_users)


if __name__ == '__main__':
    log = server_log.get_loger()
    main()
    # main_test()
