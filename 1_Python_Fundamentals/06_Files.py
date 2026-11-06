# При роботі з файлами розрізняють дві ситуації:
# - робота з файловою системою (пошук, копіювання,
#   видалення файлів та директорій тощо)
# - робота з даними, що зберігаються у файлах
#

def write_file():
    '''Приклад роботи з файлом без автоматичного
    управління ресурсами'''
    try:
        file = open("data_1.txt", "w")
        file.write("Latin charset data\n")
        file.write("Кириличні дані\n")
        file.flush()
    except OSError as err:
        print("write_file():", err)
    finally:
            file.close()


def main():
    write_file()