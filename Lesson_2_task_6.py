main_question=input("Вы желаете добвить товары, да или нет? ")
quantity_question=int(input("сколько товаров Вы хотите добавить? ")) if main_question=="да" else exit("досвидания")
if quantity_question==1:
    item_1_name = input("введите название товара 1: ")
    price_item_1 = input("введите цену товара 1: ")
    quantaty_item_1 = input("введите количество товара 1:")
    item_1 = (1, {'название: ': item_1_name, 'цена: ': price_item_1, 'количество: ': quantaty_item_1, 'ед': 'шт.'})
    print(item_1)
    name_characteristic = {'название товаров: ': [item_1_name]}
    print(name_characteristic)
    price_characteristic = {'цена товаров: ': [price_item_1]}
    print(price_characteristic)
    quantaty_characteristic = {'количество товаров: ': [quantaty_item_1]}
    print(quantaty_characteristic)
    pics_characteristic= {'ед': 'шт.'}
    print(pics_characteristic)
if quantity_question==2:
    item_1_name = input("введите название товара 1: ")
    price_item_1 = input("введите цену товара 1: ")
    quantaty_item_1 = input("введите количество товара 1:")
    item_2_name = input("введите название товара 2: ")
    price_item_2 = input("введите цену товара 2: ")
    quantaty_item_2 = input("введите количество товара 2:")
    item_1 = (1, {'название: ': item_1_name, 'цена: ': price_item_1, 'количество: ': quantaty_item_1, 'ед': 'шт.'})
    print(item_1)
    item_2 = (2, {'название: ': item_2_name, 'цена: ': price_item_2, 'количество: ': quantaty_item_2, 'ед': 'шт.'})
    print(item_2)
    name_characteristic = {'название товаров: ': [item_1_name, item_2_name]}
    print(name_characteristic)
    price_characteristic = {'цена товаров: ': [price_item_1, price_item_2]}
    print(price_characteristic)
    quantaty_characteristic = {'количество товаров: ': [quantaty_item_1, quantaty_item_2]}
    print(quantaty_characteristic)
    pics_characteristic = {'ед': 'шт.'}
    print(pics_characteristic)
if quantity_question==3:
    item_1_name = input("введите название товара 1: ")
    price_item_1 = input("введите цену товара 1: ")
    quantaty_item_1 = input("введите количество товара 1:")
    item_2_name = input("введите название товара 2: ")
    price_item_2 = input("введите цену товара 2: ")
    quantaty_item_2 = input("введите количество товара 2:")
    item_3_name=input("введите название товара 3: ")
    price_item_3=input("введите цену товара 3: ")
    quantaty_item_3=input("введите количество товара 3:")
    item_1 = (1, {'название: ': item_1_name, 'цена: ': price_item_1, 'количество: ': quantaty_item_1, 'ед': 'шт.'})
    print(item_1)
    item_2 = (2, {'название: ': item_2_name, 'цена: ': price_item_2, 'количество: ': quantaty_item_2, 'ед': 'шт.'})
    print(item_2)
    item_3 = (3, {'название: ': item_3_name, 'цена: ': price_item_3, 'количество: ': quantaty_item_3, 'ед': 'шт.'})
    print(item_3)
    name_characteristic = {'название товаров: ': [item_1_name, item_2_name, item_3_name]}
    print(name_characteristic)
    price_characteristic = {'цена товаров: ': [price_item_1, price_item_2, price_item_3]}
    print(price_characteristic)
    quantaty_characteristic = {'количество товаров: ': [quantaty_item_1, quantaty_item_2, quantaty_item_3]}
    print(quantaty_characteristic)
    pics_characteristic = {'ед': 'шт.'}
    print(pics_characteristic)
