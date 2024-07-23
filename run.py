# import time for sleep method
import time

# PRICES below is capitalised, as per the convention 
# for denoting some variables as constants which should
# not be changed

PRICES = {
	'small-onion-rings': 3,
	'mozarella-sticks': 3,
	'small-chips': 3,
	'medium-chips': 3.50,
	'large-chips': 4,
	'onion-rings-supreme':6,
	'onion-rings-deluxe':7,
	'onion-rings-ballybonion-super-box':10,
	'coke':2,
	'water':2,
	'nutella-onion-rings':5, 
	'pistachio-onion-rings':5.50,
	}

class NewOrder:
    def __init__(self):
        self.new_order = {
	'small-onion-rings': None,
	'mozzarella-sticks': None,
	'small-chips': None,
	'medium-chips': None,
	'large-chips': None,
	'onion-rings-supreme':None,
	'onion-rings-deluxe':None,
	'ballybonion-super-box':None,
	'coke':None,
	'water':None,
	'nutella-onion-rings':None, 
	'pistachio-onion-rings':None,
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

def not_make_order():
    print("That's ok! Come back soon when you're not so poor and/or feckless!")
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
            continue

def vacate_premises():
    print("This terminal has recorded a photographic image of you.")
    print("It will be relayed to An Garda Siochána and will be the basis for a")
    print("trespassing charge against you.")
    print("Please remove yourself from the premises and allow the next customer to order.")
    time.sleep(5)
    startscreen()

def main_menu():
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
    print('Starters:')
    print('1. Small Onion Rings: €3')
    print('2. Mozzarella Sticks: €3')
    print('3. Return back to Main Menu')
    print('4. Finalise your order')
    
    while True:
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
                            new_order.add_item('small-onion-rings', ordered_quantity)
                            print(f'{ordered_quantity} x Small Onion Rings added to your order')
                    except ValueError:
                        print('Invalid input, try again.')
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity.isdigit and int(ordered_quantity) >= 0:
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('mozzarella-sticks', ordered_quantity)
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







def main():
    new_order = NewOrder()
    startscreen()

new_order = NewOrder()
startscreen()
