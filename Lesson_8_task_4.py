class Warehouse:
    print("Добро пожаловать в программу склад!")

class Office:
    welcome_message_2=int(input("Выберите действие, введите цифру: 1. добавить товар 2. удалить товар(продажа, перемещение) 3. показать товары, введите число: "))
    if welcome_message_2 == 1:
        add_goods = int(input("Введите цифру товара,который хотете добавить: 1.Принтер, 2.Сканер, 3.Копир "))
        if add_goods == 1:
            Printer.add_1()
class Printer(Office):
    def add_1(printer_in_stock):
        print("Добавляем товар на склад: ")
        new_name = input("Введите производителя и модель: ")
        new_quantity = int(input("Введите количество цифрой: "))
        new_price = int(input("Введите цену нового товара числом: "))
        printer_in_stock.update({new_name: new_quantity, 'цена': new_price})
        return printer_in_stock
    printer_in_stock = {'Samsung X100': 3, 'цена': 10000}
