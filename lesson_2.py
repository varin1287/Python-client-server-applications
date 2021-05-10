'''
1.a
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);'''

import csv
import re


def get_data():
    sought_parameter_list = {'Изготовитель системы': [], 'Название ОС': [],
                             'Код продукта': [], 'Тип системы': []}

    for k in range(1, 4):
        used_file = f'info_{k}.txt'

        with open(used_file, 'r', encoding='windows-1251') as f:
            f_n_reader = csv.reader(f)

            for line in f_n_reader:
                for param in sought_parameter_list.keys():
                    if re.search(param, line[0]):
                        (sought_parameter_list[param]).append(re.sub(f'{param}[:,\s_]+', '', line[0]))

    os_prod_list = sought_parameter_list['Изготовитель системы']
    os_name_list = sought_parameter_list['Название ОС']
    os_code_list = sought_parameter_list['Код продукта']
    os_type_list = sought_parameter_list['Тип системы']

    print('Списки значений каждого параметра')
    print(os_prod_list)
    print(os_name_list)
    print(os_code_list)
    print(os_type_list)

    main_data = [[], [], [], []]

    for elem in sought_parameter_list:
        main_data[0].append(elem)
        main_data[1].append(sought_parameter_list[elem][0])
        main_data[2].append(sought_parameter_list[elem][1])
        main_data[3].append(sought_parameter_list[elem][2])

    return main_data


'''
1.b
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;
'''


# Из задания "в которую передавать ссылку на CSV-файл", на какой CSV-файл в исходных данных три файла
# Буду считать что CSV-файл в который нужно записать

def write_to_csv(file_name):
    main_data = get_data()
    print('*' * 100)
    print('подготовленные данные')
    for el in main_data:
        print(el)
    with open(file_name, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in main_data:
            f_n_writer.writerow(row)


'''
1.c
Проверить работу программы через вызов функции write_to_csv()
'''
write_to_csv('main_data.csv')

'''
2.a Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
'''

import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_order_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'w') as f_n:
        json.dump(dict_order_to_json, f_n, indent=4)


'''
2.b Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
'''

write_order_to_json('товар', 3, 1200, 'покупатель', '2.05.21')

print('\nЗадание 2')
print('Данные из файла')
with open('orders.json') as f_n:
    print(f_n.read())

'''
3.a Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
'''

import yaml

print('\nЗадание 3')
my_dict = {
    '1': [1, 2, 3],
    '2': 10,
    '3': {'1€': 1, '2€': 2}
}

'''
3.b Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;
'''

with open('file.yaml', 'w') as f_n:
    yaml.dump(my_dict, f_n, default_flow_style=False, allow_unicode = True)

'''
3.c
Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными.
'''
with open('file.yaml') as f_n:
    print(f_n.read())
