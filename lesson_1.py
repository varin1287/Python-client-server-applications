'''
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
'''

print('\nзадание 1')
words = ['разработка', 'сокет', 'декоратор']

for word in words:
    print(f'тип: {type(word)} - содержание: {word}')

'Что здесь требуется?'
print('\nОнлайн-конвертер в формат Unicode выдает')
words_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                 '\u0441\u043e\u043a\u0435\u0442',
                 '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for word in words_unicode:
    print(f'тип: {type(word)} - содержание: {word}')

print('\nword.encode("utf-8") выдает')
words_unicode = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
                 b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
                 b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

for word in words_unicode:
    print(f'тип: {type(word)} - содержание: {word}')

'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

print('\nзадание 2')
words = [b'class', b'function', b'method']

for word in words:
    print(f'тип: {type(word)}, содержимое: {word}, длинна: {len(word)}')

'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

print('\nзадание 3')
words = ['attribute', 'класс', 'функция', 'type']

flag = True
for word in words:
    try:
        word.encode('ascii')
    except:
        print(f'нельзя записать в ascii слово: {word}')
        flag = False

if flag:
    print('в ascii можно записать все из заданных слов')


flag = True
for word in words:
    try:
        word.encode('utf-8')
    except:
        print(f'нельзя записать в utf-8: {word}')
        flag = False

if flag:
    print('в utf-8 можно записать все из заданных слов')

'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
 и выполнить обратное преобразование (используя методы encode и decode).
'''

print('\nзадание 4')
words = ['разаботка', 'адмиинстрирование', 'protocol', 'standard']

for word in words:
    res = word.encode(encoding='utf-8')
    print(res)
    res = res.decode(encoding='utf-8')
    print(res)

'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в 
строковый тип на кириллице.
'''

print('\nзадание 5')

import subprocess

web_resources = ['yandex.ru', 'youtube.com']

for web_resource in web_resources:
    print(f'работа с {web_resource}')
    args = ['ping', web_resource]
    subprocess_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for i, line in enumerate(subprocess_ping.stdout):
        if i > 2:
            break
        print(line)
        print(line.decode('utf-8'))


'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''

print('\nзадание 6')
words = ['сетевое програмирование', 'сокет', 'декоратор']
with open('task_6.txt', 'w', encoding='utf-8') as f:
    for word in words:
        f.write(f'{word}\n')

print('Данные из файла\n')
with open('task_6.txt', 'r', encoding='utf-8') as f:
    print(f.read())
