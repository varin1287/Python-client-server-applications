'''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс
'''


def time(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = (seconds % 3600) % 60
    return h, m, s


# seconds = input('введите время в секундах: ')
seconds = 35425
if __name__ == "__main__":
    res = time(seconds)
    res = f'{res[0]}:{res[1]}:{res[2]}'
    print(res)

'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''

def sum_max_number(my_list):
    return [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

my_list = [15, 2, 3, 1, 7, 5, 4, 10]

if __name__ == "__main__":
    my_new_list = sum_max_number(my_list)


