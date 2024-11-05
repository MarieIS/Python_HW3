goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42}
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520}
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150}
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97}
    ]
}

# проходим по всем товарам в словаре goods
for item_name in goods.keys():
    # получаем код товара из словаря goods
    item_code = goods[item_name]

    # инициализируем переменные для подсчета общего количества и стоимости
    total_quantity = 0
    total_cost = 0

    # проходим по всем записям для данного товара в словаре store
    for entry in store[item_code]:
        # увеличиваем общее количество товара
        total_quantity += entry['quantity']
        # увеличиваем общую стоимость товара
        total_cost += entry['price'] * entry['quantity']
    
    # выводим информацию о товаре
    print('{} - {} штук, стоимость {} рубля(ей).'.format(item_name, total_quantity, total_cost))