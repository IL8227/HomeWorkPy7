import os


def import_file():
    with open('file.txt', 'r', encoding='utf-8') as f:
        with open('file_2.txt', 'w', encoding='utf-8') as d:
            for i in f:
                d.write(i)


def export_file():
    path = input('Введите путь к файлу ')
    with open('file.txt', 'r', encoding='utf-8') as f:
        with open(path, 'w', encoding='utf-8') as d:
            for i in f:
                d.write(i)
                