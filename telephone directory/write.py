def writefile():
    a = input('Фамилия ')
    b = input('Имя ')
    c = input('Телефон ')
    d = input('Информация ')
    with open('file.txt', 'a', encoding='utf-8') as f:
        f.write(f'{a};{b};{c};{d}\n')


def readfile():
    with open('file.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        print(text)


