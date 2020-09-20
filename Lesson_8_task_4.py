class Office:
    def __init__(self):
        self.add_goods = add_goods

    def add_printer(printer_in_stock):
        print("Добавляем товар на склад: ")
        new_name = input("Введите производителя и модель: ")
        try:
            new_quantity = int(input("Введите количество цифрой: "))
        except ValueError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if new_quantity <= 0:
            print("Добавление пустой позиции недопустимо.")
            exit(0)
        try:
            new_price = int(input("Введите цену нового товара числом: "))
        except ValueError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if new_price <= 0:
            print("Продавать товары бесплатно это плохой бизнес!")
            exit(0)
        printer_in_stock.update({new_name: new_quantity, f'цена {new_name}': new_price})
        return printer_in_stock

    def add_scaner(scaner_in_stock):
        print("Добавляем товар на склад: ")
        new_name = input("Введите производителя и модель: ")
        try:
            new_quantity = int(input("Введите количество цифрой: "))
        except ValueError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if new_quantity <= 0:
            print("Добавление пустой позиции недопустимо.")
            exit(0)
        try:
            new_price = int(input("Введите цену нового товара числом: "))
        except ValueError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if new_price <= 0:
            print("Продавать товары бесплатно это плохой бизнес!")
            exit(0)
        scaner_in_stock.update({new_name: new_quantity, f'цена {new_name}': new_price})
        return scaner_in_stock

    def add_copier(copier_in_stock):
        print("Добавляем товар на склад: ")
        new_name = input("Введите производителя и модель: ")
        try:
            new_quantity = int(input("Введите количество цифрой: "))
        except ValueError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if new_quantity <= 0:
            print("Добавление пустой позиции недопустимо.")
            exit(0)
        try:
            new_price = int(input("Введите цену нового товара числом: "))
        except ValueError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if new_price <= 0:
            print("Продавать товары бесплатно это плохой бизнес!")
            exit(0)
        copier_in_stock.update({new_name: new_quantity, f'цена {new_name}': new_price})
        return copier_in_stock

    def delete_printer(printer_in_stock):
        print(printer_in_stock)
        print("Удаляем товар со склада")
        delete_choice = input("Введите название и модель принтера, единицу которого вы хотите удалить :")
        temp_value = printer_in_stock.get(delete_choice)
        try:
            temp_value = temp_value - 1
        except TypeError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if temp_value <= 0:
            printer_in_stock.pop(delete_choice, None)
            printer_in_stock.pop(f'цена {delete_choice}', None)
        else:
            printer_in_stock.update({delete_choice: temp_value})
        return printer_in_stock

    def delete_scaner(scaner_in_stock):
        print(scaner_in_stock)
        print("Удаляем товар со склада")
        delete_choice = input("Введите название и модель сканера, единицу которого вы хотите удалить :")
        temp_value = scaner_in_stock.get(delete_choice)
        try:
            temp_value = temp_value - 1
        except TypeError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if temp_value <= 0:
            scaner_in_stock.pop(delete_choice, None)
            scaner_in_stock.pop(f'цена {delete_choice}', None)
        else:
            scaner_in_stock.update({delete_choice: temp_value})
        scaner_in_stock.update({delete_choice: temp_value})
        return scaner_in_stock

    def delete_copier(copier_in_stock):
        print(copier_in_stock)
        print("Удаляем товар со склада")
        delete_choice = input("Введите название и модель принтера, единицу которого вы хотите удалить :")
        temp_value = copier_in_stock.get(delete_choice)
        try:
            temp_value = temp_value - 1
        except TypeError:
            print("Вы введи недопустимое название товара")
            exit(0)
        if temp_value <= 0:
            copier_in_stock.pop(delete_choice, None)
            copier_in_stock.pop(f'цена {delete_choice}', None)
        else:
            copier_in_stock.update({delete_choice: temp_value})
        copier_in_stock.update({delete_choice: temp_value})
        return copier_in_stock

    printer_in_stock = {'Samsung X100': 1, 'цена Samsung X100': 10000}
    scaner_in_stock = {'BBK 1200': 2, 'цена BBK 1200': 2000}
    copier_in_stock = {'Brothers XL100': 5, 'цена Brothers XL100': 4000}


class Printer(Office):
    def in_stock():
        print(f'Всего на балансе склада принтеров - {Office.printer_in_stock}')


class Scaner(Office):
    def in_stock():
        print(f'Всего на балансе склада сканеров - {Office.scaner_in_stock}')


class Copier(Office):
    def in_stock():
        print(f'Всего на балансе склада копиров - {Office.copier_in_stock}')


print("Добро пожаловать в программу склад!")
try:
    welcome_message_2 = int(input(
        "Выберите действие, введите цифру: 1. добавить товар 2. удалить товар(продажа, перемещение) 3. показать товары, введите число: "))
except ValueError:
    print("Допустим ввод только числа!")
    exit(0)
if welcome_message_2 == 1:
    try:
        add_goods = int(input("Введите цифру товара,который хотете добавить: 1.Принтер, 2.Сканер, 3.Копир "))
    except ValueError:
        print("Допустим ввод только числа!")
        exit(0)
    if add_goods == 1:
        Office.add_printer(Office.printer_in_stock)
        Printer.in_stock()
    if add_goods == 2:
        Office.add_scaner(Office.scaner_in_stock)
        Scaner.in_stock()
    if add_goods == 3:
        Office.add_copier(Office.copier_in_stock)
        Copier.in_stock()
    if add_goods > 3:
        print("Ошибка ввода, вы ввели недопустимое число!")
        exit(0)
    if add_goods <= 0:
        print("Ошибка ввода, вы ввели недопустимое число!")
        exit(0)
if welcome_message_2 == 2:
    try:
        delete_goods = int(
            input("Введите цифру группы товара, где вы хотите произвести удаление: 1.Принтер, 2.Сканер, 3.Копир : "))
    except ValueError:
        print("Вы ввели не число!")
        exit(0)
    if delete_goods > 3:
        print("Вы введи недопустимое число")
        exit(0)
    if delete_goods <= 0:
        print("Вы введи недопустимое число")
        exit(0)
    if delete_goods == 1:
        Office.delete_printer(Office.printer_in_stock)
        Printer.in_stock()
    if delete_goods == 2:
        Office.delete_scaner(Office.scaner_in_stock)
        Scaner.in_stock()
    if delete_goods == 3:
        Office.delete_copier(Office.copier_in_stock)
        Copier.in_stock()
if welcome_message_2 == 3:
    try:
        show_goods = int(
            input("Введите цифру группы товара, наличие который Вы хотите узнать: 1.Принтер, 2.Сканер, 3.Копир :  "))
    except ValueError:
        print("Вы ввели не число!")
        exit(0)
    if show_goods > 3:
        print("Вы введи недопустимое число")
        exit(0)
    if show_goods <= 0:
        print("Вы введи недопустимое число")
        exit(0)
    if show_goods == 1:
        Printer.in_stock()
    if show_goods == 2:
        Scaner.in_stock()
    if show_goods == 3:
        Copier.in_stock()
if welcome_message_2 > 3:
    print("Ошибка ввода, вы ввели недопустимое число!")
    exit(0)
if welcome_message_2 <= 0:
    print("Ошибка ввода, вы ввели недопустимое число!")
    exit(0)
if welcome_message_2 > 3:
    print("Ошибка ввода, вы ввели недопустимое число!")
    exit(0)
if welcome_message_2 <= 0:
    print("Ошибка ввода, вы ввели недопустимое число!")
    exit(0)
