import time
import sys

def input_order():
    ordering = True
    while ordering is True:
        item_menu = {1: 'Chicken Strips',
                         2: 'French Fries',
                         3: 'Hamburger',
                         4: 'Hotdog',
                         5: 'Large Drink',
                         6: 'Medium Drink',
                         7: 'Milk Shake',
                         8: 'Salad',
                         9: 'Small Drink'}
        price_list = {1: 3.50,
                          2: 2.50,
                          3: 4.00,
                          4: 3.50,
                          5: 1.75,
                          6: 1.50,
                          7: 2.25,
                          8: 3.75,
                          9: 1.25}
        print("Today's menu is:")
        for i in range(1,len(item_menu)):
            print(str(i) + '   ' + str(item_menu[i]) + '   ' + str(price_list[i]))
        print("Please type the numbers you wish to order without any spaces.")
        while True:
            n = ''
            try:
                n = int(input())
            except ValueError:
                print("Please make sure you ONLY have numbers and there are NO spaces.")
            if type(n) == int:
                break
        order = str(n)
        order_list= []
        for i in range(len(order)):
            order_list.append(int(order[i]))
        cost,orderlist = get_cost(item_menu,price_list,order_list)
        print("Calculating order...")
        time.sleep(1.5)
        print ('')
        for i in range(len(orderlist)):
            print (orderlist[i])
        print('Price: %d' % cost)
        print("Place another order?")
        asking = True
        while asking is True:
            repeat = input().lower()
            if repeat != 'yes' and repeat != 'no':
                print("Please answer only yes or no.")
                continue
            elif repeat == 'yes':
                asking = False
            elif repeat == 'no':
                sys.exit()
                
    
def get_cost(item,price,order):
    items_ordered = []
    prices_items = []
    for i in range(len(order)):
        items_ordered.append(item[order[i]])
        prices_items.append(price[order[i]])
    total_cost = sum(prices_items)
    return total_cost, items_ordered
    

input_order()
