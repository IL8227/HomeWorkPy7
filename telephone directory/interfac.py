from write import writefile
from write import readfile
from imp_exp import import_file
from imp_exp import export_file


def sort():
    while True:
        print('1. Просмотр записей')
        print('2. Добавление записи')
        print('3. Импорт')
        print('4. Экспорт')
        print('5. Выход из программы')
        n = input('Выберите пункт меню. ')

        if n == '1':
            readfile()
        elif n == '2':
            writefile()
        elif n == '3':
            import_file()
        elif n == '4':
            export_file()
        elif n == '5':
            break
        else:
            print('Неправильное значение, введите ещё раз! ')