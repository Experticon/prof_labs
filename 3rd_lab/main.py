import csv
from pathlib import Path
import codecs


def add_new_data(d):
    number_value = input("Код студента: ")
    name_value = input("ФИО студента: ")
    email_value = input("email студента: ")
    group_value = input("Группа: ")
    with codecs.open("Студенты/data.csv", "a") as f:
        f.write(f"{number_value};{name_value};{email_value};{group_value}\r")
    d.update({len(d)+1: {"number": int(number_value), "name": name_value, "email": email_value, "group": group_value}})


if __name__ == '__main__':
    choice = int(input("Как словарь выведется?\n"
                   "1 - сортировка по числу (номеру студента),\n2 - сортировка по строке (ФИО студента),\n"
                   "3 - по принадлжености к группе ИВТАСбд\n"))
    if choice != 1 and choice != 2 and choice != 3:
        print("Неверные данные")
        exit()

    folder_name = "Студенты"
    folder = Path(folder_name)
    print(f"В папке {folder_name} есть {len(list(folder.iterdir()))} объектов")
    file = codecs.open('Студенты/data.csv', 'r')
    dicti = {}

    text = file.read().splitlines()
    i = 0
    for line in text:
        number_value, name_value, email_value, group_value = line.split(";")
        dicti.update({i: {"number": int(number_value), "name": name_value, "email": email_value, "group": group_value}})
        i += 1
    if choice == 1:
        sorted_dic = dict(sorted(dicti.items(), key=lambda item: item[1]["number"]))
        for k, v in sorted_dic.items():
            print(v)
    elif choice == 2:
        sorted_dic = dict(sorted(dicti.items(), key=lambda item: item[1]["name"]))
        for k, v in sorted_dic.items():
            print(v)
    elif choice == 3:
        for k, v in dicti.items():
            if v["group"] >= "ИВТАСбд":
                print(v)
    choice = int(input("Добавить новый элемент?\n1 - да, 2 - нет\n"))
    if choice == 1:
        print("Первый выбор")
        add_new_data(dicti)
        for k, v in dicti.items():
            print(v)
    elif choice == 2:
        print("Второй выбор (ладно)")
        exit()
    else:
        print("Неверные данные")
        exit()


