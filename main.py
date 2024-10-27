cart = []
storage = {
    'rice':{'price':4.50},
    'beans':{'price':5.00},
    'pasta': {'price':3.50},
    'sugar':{'price':3.50},
    'eggs':{'price':0.50},
    'coffe':{'price':4.00},
    'water':{'price':2.00},
    'tomato':{'price':1.00}
}
total = 0

while True:
    product = input('Type your product (Q to quit): \n').lower()
    if product == 'q':
        break
    if product not in storage:
        print(f'There is no {product} in our storage')
    else:
        cart += [product]
        getInfo = storage[product]
        price = getInfo['price']
        total += price

print('===== Your products =====')
print(' | '.join(cart))
print(f'You need to pay R$ {total:,.2f}')