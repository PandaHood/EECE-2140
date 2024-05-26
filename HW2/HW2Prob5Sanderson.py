import operator
parts = [('38','Electric sander',11,24.09),('42','Power saw',18,89.82),('77','Sledge hammer',7,57.98),('7','Hammer',76,11.99)]
description = sorted(parts, key = operator.itemgetter(1))
print(f'Sorted list by part description: {description}.')

quantity = []
for i in range(len(parts)):
    quantity.append((parts[i][1],parts[i][2]))

quantity = sorted(quantity,key = operator.itemgetter(1))
print(f'List containing tuples with only description and quantity and sorted by quantity: {quantity}')

price = []
for x in range(len(parts)):
    price.append((parts[x][1],parts[x][2] * parts[x][3]))
price = sorted(price, key = operator.itemgetter(1))
print(f'List sorted by price and only containg price and description: {price}')

filtered_price = []
for elements in range(len(price)):
    if price[elements][1] < 1000 and price[elements][1] > 200:
        filtered_price.append((price[elements][0], price[elements][1]))
print(f'Filtered price between 200 and 1000 dollars: {filtered_price}')

total = 0
for elements in range(len(price)):
    total += price[elements][1] 
print(f'The total cost of all invoices: {total:6.2f}')