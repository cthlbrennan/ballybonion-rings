# import time for sleep method
import time
import os
import sys

# PRICES below is capitalised, as per the convention 
# for denoting some variables as constants which should
# not be changed 

PRICES = {
	'small_onion_rings': 3,
	'mozarella_sticks': 3,
	'small_chips': 3,
	'medium_chips': 3.50,
	'large_chips': 4,
	'onion_rings_supreme':6,
	'onion_rings_deluxe':7,
	'ballybonion_super_box':10,
	'coke':2,
	'water':2,
	'nutella_onion_rings':5, 
	'pistachio_onion_rings':5.50,
	}

class NewOrder:
    def __init__(self):
        self.new_order = {
	'small_onion_rings': None,
	'mozzarella_sticks': None,
	'small_chips': None,
	'medium_chips': None,
	'large_chips': None,
	'onion_rings_supreme':None,
	'onion_rings_deluxe':None,
	'ballybonion_super_box':None,
	'coke':None,
	'water':None,
	'nutella_onion_rings':None, 
	'pistachio_onion_rings':None,
	}

    def add_item(self, item, quantity):
        if (item in self.new_order and self.new_order[item] == None):
            self.new_order[item] = quantity
        elif (item in self.new_order and self.new_order[item] != None):
            existing_quantity = self.new_order[item]
            new_quantity = quantity + existing_quantity
            self.new_order[item] = new_quantity
        else:
            print(f"Item '{item}' not found.")

    def remove_item(self, item):
        if (item in self.new_order):
            self.new_order[item] = None
        else:
            print(f"Item '{item}' not found.")

    def display_order(self):
        for category, items in self.ordered_items.items():
            print(f"{category.capitalize()}:")
            for item, quantity in items.items():
                if quantity is not None:
                    print(f"  - {item}: {quantity}")
                else:
                    print(f"  - {item}: Not ordered")
        print()

    def get_ordered_items(self):
        ordered = {}
        for category, items in self.ordered_items.items():
            ordered[category] = {item: quantity for item, quantity in items.items() if quantity is not None}
        return ordered

def startscreen():
    clear()
    print("Welcome to BallybOnion Rings, Ballybunion's greatest purveyor of")
    print("pun-based (or should we say pun-ion-based) fast foods!")
    make_an_order = input("Would you like to make an order? y/n\n")

    if (make_an_order.lower() == 'y'):
        main_menu()
    elif (make_an_order.lower() == 'n'):
        not_make_order()
    else:
        print('Input is invalid')
        startscreen()

# code based on https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    if sys.platform.startswith('win'):
        os.system('cls')  
    else:
        os.system('clear')

def not_make_order():
    clear()
    print("That's ok! Come back s3oon when you're not so poor and/or feckless!")
    print('Please vacate the premises immediately or we will notify An Garda Síochana.')
    answer = input('New customer? y/n\n')
    while True:
        if (answer.lower() == 'y'):
            startscreen()
            break
        elif (answer.lower() == 'n'):
            vacate_premises()
            break
        else:
            print('Invalid input, please try again')
            time.sleep(1)
            continue

def vacate_premises():
    clear()
    print("This terminal has recorded a photographic image of you.")
    print("It will be relayed to An Garda Siochána and will be the basis for a")
    print("trespassing charge against you.")
    print("Please remove yourself from the premises and allow the next customer to order.")
    time.sleep(5)
    startscreen()

def main_menu():
    clear()
    print("Please select from one of the following sub menus:")
    print("1. Starters")
    print("2. Sides")
    print("3. Mains")
    print("4. Drinks")
    print("5. Desserts")
    print("6. Cancel items from order")
    print("7. Finalise order")
    
    while True:
        menu_selection = input("Please input the number which corresponds with your selection\n")
        match (menu_selection):
            case '1':
                starters_menu()
                break
            case '2':
                sides_menu()
                break
            case '3':
                mains_menu()
                break
            case '4':
                drinks_menu()
                break
            case '5':
                desserts_menu()
                break
            case '6':
                cancel_items()
                break
            case '7':
                finalise_order()
                break
            case _:
                print('Invalid selection, try again.')

def starters_menu():
    while True:
        clear()
        print('Starters:')
        print('1. Small Onion Rings: €3')
        print('2. Mozzarella Sticks: €3')
        print('3. Return back to Main Menu')
        print('4. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4']
        if selection not in menu_options:
            print('Invalid selection, please try again')
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('small_onion_rings', ordered_quantity)
                            print(f'{ordered_quantity} x Small Onion Rings added to your order')
                            time.sleep(2)
                    except ValueError:
                        print('Invalid input, try again.')
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('mozzarella_sticks', ordered_quantity)
                            print(f'{ordered_quantity} x Mozzarella Sticks added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '3':
                    main_menu()
                    break
                case '4':
                    finalise_order()
                    break
                case _:
                    print('Invalid input, please try again.')

def sides_menu():
    while True:
        clear()
        print('Sides:')
        print('1. Small Chips: €3')
        print('2. Medium Chips: €3.50')
        print('3. Large Chips: €4')
        print('4. Return back to Main Menu')
        print('5. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4', '5']
        if selection not in menu_options:
            print('Invalid selection, please try again')
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('small_chips', ordered_quantity)
                            print(f'{ordered_quantity} x Small Chips added to your order')
                            time.sleep(2)
                    except ValueError:
                        print('Invalid input, try again.')
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('medium_chips', ordered_quantity)
                            print(f'{ordered_quantity} x Medium Chips added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '3':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('large_chips', ordered_quantity)
                            print(f'{ordered_quantity} x Large Chips added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '4':
                    main_menu()
                    break
                case '5':
                    finalise_order()
                    break
                case _:
                    print('Invalid input, please try again.')


def mains_menu():
    while True:
        clear()
        print('Mains:')
        print('1. Onion Rings Supreme: €6')
        print('2. Onion Rings Deluxe: €7')
        print('3. BallybOnion Super Box: €10')
        print('4. Return back to Main Menu')
        print('5. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4', '5']
        if selection not in menu_options:
            print('Invalid selection, please try again')
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('onion_rings_supreme', ordered_quantity)
                            print(f'{ordered_quantity} x Onion Rings Supreme added to your order')
                            time.sleep(2)
                    except ValueError:
                        print('Invalid input, try again.')
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('onion_rings_deluxe', ordered_quantity)
                            print(f'{ordered_quantity} x Onion Rings Deluxe added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '3':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('ballybonion_super_box', ordered_quantity)
                            print(f'{ordered_quantity} x BallybOnion Super Box added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '4':
                    main_menu()
                    break
                case '5':
                    finalise_order()
                    break
                case _:
                    print('Invalid input, please try again.')

def drinks_menu():
    while True:
        clear()
        print('Drinks:')
        print('1. Coke: €2')
        print('2. Water: €2')
        print('3. Return back to Main Menu')
        print('4. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4']
        if selection not in menu_options:
            print('Invalid selection, please try again')
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('coke', ordered_quantity)
                            print(f'{ordered_quantity} x Coke added to your order')
                            time.sleep(2)
                    except ValueError:
                        print('Invalid input, try again.')
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('water', ordered_quantity)
                            print(f'{ordered_quantity} x Water added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '3':
                    main_menu()
                    break
                case '4':
                    finalise_order()
                    break
                case _:
                    print('Invalid input, please try again.')

def drinks_menu():
    while True:
        clear()
        print('Desserts:')
        print('1. Nutella Onion Rings: €5')
        print('2. Pistachio Onion Rings: €5.50')
        print('3. Return back to Main Menu')
        print('4. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4']
        if selection not in menu_options:
            print('Invalid selection, please try again')
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('nutella_onion_rings', ordered_quantity)
                            print(f'{ordered_quantity} x Nutella Onion Rings added to your order')
                            time.sleep(2)
                    except ValueError:
                        print('Invalid input, try again.')
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('pistachio_onion_rings', ordered_quantity)
                            print(f'{ordered_quantity} x Pistachio Onion Rings added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '3':
                    main_menu()
                    break
                case '4':
                    finalise_order()
                    break
                case _:
                    print('Invalid input, please try again.')

def main():
    new_order = NewOrder()
    startscreen()

new_order = NewOrder()
startscreen()


