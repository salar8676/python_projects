# Define the menu of Restaurant
menu={
    'Pizza':1000,
    'Pasta':500,
    'Burger':200,
    'Salad':300,
    'Coffee':150
}

import random
import pyfiglet

text="SK Restaurant"
welcome=pyfiglet.figlet_format(text,font='graffiti')
print(welcome)

print('Pizza:Rs1000\nPasta:Rs500\nBurger:Rs200\nSalad:Rs300\nCoffee:150')

order_total= 0

item_1 = input('Enter the name of item you want to order: ')
if item_1 in menu:
    order_total += menu[item_1]
    print(f'Your item {item_1} has been added to your order')

else:
    print(f'Ordered item {item_1} is not available yes!')

another_order = input('Do you want to add another item? (Yes/No) ')
if another_order == 'Yes':
    item_2 = input('Enter the name of second item: ')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'item {item_2} has been added to your order')
    else:
        print(f'ordered item {item_2} is not available!')
print(f'The total amount of items to pay is: {order_total}')


