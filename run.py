# import time for sleep method
import time
import os
import sys
import re
import pyfiglet 
  
 
# The dictionaries NAMES and PRICES below are capitalised, as per the convention 
# for denoting some variables as constants which should
# not be changed 

NAMES = {
    'small_onion_rings': 'Small Onion Rings',
	'mozzarella_sticks': 'Mozzarella Sticks',
	'small_chips': 'Small Chips',
	'medium_chips': 'Medium Chips',
	'large_chips': 'Large Chips',
	'onion_rings_supreme':'Onion Rings Supreme',
	'onion_rings_deluxe': 'Onion Rings Deluxe',
	'ballybonion_super_box': 'BallybOnion Super Box',
	'coke': 'Coke',
	'water': 'Water',
	'nutella_onion_rings': 'Nutella Onion Rings', 
	'pistachio_onion_rings': 'Pistachio Onion Rings',
}

PRICES = {
	'small_onion_rings': 3.00,
	'mozzarella_sticks': 3.00,
	'small_chips': 3.00,
	'medium_chips': 3.50,
	'large_chips': 4.00,
	'onion_rings_supreme':6.00,
	'onion_rings_deluxe':7.00,
	'ballybonion_super_box': 10.00,
	'coke':2.00,
	'water':2.00,
	'nutella_onion_rings':5.00, 
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
	'onion_rings_deluxe': None,
	'ballybonion_super_box': None,
	'coke': None,
	'water': None,
	'nutella_onion_rings': None, 
	'pistachio_onion_rings': None,
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

def startscreen():
    clear()
    result = pyfiglet.figlet_format("Welcome to BallybOnion Rings", font = "bulbhead" ) 
    print(result)
    print("Ballybunion's greatest purveyor of pun-based")
    print("(or should we say pun-ion-based) fast foods!")
    make_an_order = input("Would you like to make an order? y/n\n")

    if (make_an_order.lower() == 'y'):
        main_menu()
    elif (make_an_order.lower() == 'n'):
        not_make_order()
    else:
        print(f'{make_an_order} is invalid. Please input either y or n')
        time.sleep(2)
        startscreen()

# code based on https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def not_make_order():
    clear()
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
            print(f'{answer} is an invalid input, please try again')
            time.sleep(1)
            not_make_order()

def vacate_premises():
    clear()
    print("This terminal has recorded a photographic image of you.")
    print("It will be relayed to An Garda Siochána and will be the basis for a")
    print("trespassing charge against you.")
    print("Please remove yourself from the premises and allow the next customer to order.")
    time.sleep(7)
    startscreen()

def main_menu():
    clear()
    display = pyfiglet.figlet_format("Main Menu", font = "bulbhead" )
    print(display)
    print("Please select from one of the following sub menus:")
    print("1. Starters")
    print("2. Sides")
    print("3. Mains")
    print("4. Drinks")
    print("5. Desserts")
    print("6. Display current order")    
    print("7. Cancel items from current order")
    print("8. Finalise order")
    print("9. Cancel order")
    
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
                display_order()
                break
            case '7':
                cancel_items()
                break
            case '8':
                finalise_order()
            case '9':
                cancel_order()
                break
            case _:
                print(f'{menu_selection} is an invalid selection, please try again.')
                time.sleep(2)
                main_menu()

def cancel_order():
    while True:
        clear()
        print('Just pack it in and go home? y/n')
        answer = input('\n')
        if answer.lower() == 'y':
            print("Fair enough, come back when you're not going to waste our time!") 
            time.sleep(3)
            reset_new_order()
            startscreen()
            break
        elif answer.lower() == 'n':
            print('Then get busy buying stuff please!')
            time.sleep(3)
            main_menu()
            break
        else:
            print(f'{answer} is an invalid input. Try again, y/n')
            time.sleep(2)

def starters_menu():
    while True:
        clear()
        display = pyfiglet.figlet_format("Starters", font = "bulbhead" )
        print(display)
        print('Starters:')
        print('1. Small Onion Rings: €3')
        print('2. Mozzarella Sticks: €3')
        print('3. Return back to Main Menu')
        print('4. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4']
        if selection not in menu_options:
            print(f'"{selection}" is an invalid selection, please try again')
            time.sleep(2)
        else:
            match selection:
                case '1': 
                    try:
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('small_onion_rings', ordered_quantity)
                            print(f'{ordered_quantity} x Small Onion Rings added to your order')
                            time.sleep(2)                                     
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '2':
                    try:
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('mozzarella_sticks', ordered_quantity)
                            print(f'{ordered_quantity} x Mozzarella Sticks added to your order')
                            time.sleep(2)   
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '3':
                    main_menu()
                    break
                case '4':
                    finalise_order()
                    break
                case _:
                    print(f'"{ordered_quantity}" is an invalid input, try again.')
                    time.sleep(2)

def sides_menu():
    while True:
        clear()
        display = pyfiglet.figlet_format("Sides", font = "bulbhead" )
        print(display)        
        print('Sides:')
        print('1. Small Chips: €3')
        print('2. Medium Chips: €3.50')
        print('3. Large Chips: €4')
        print('4. Return back to Main Menu')
        print('5. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4', '5']
        if selection not in menu_options:
            print(f'"{selection}" is an invalid selection, please try again')
            time.sleep(2)
        else:
            match selection:
                case '1': 
                    try:
                        ordered_quantity = input('How many?\n')                        
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('small_chips', ordered_quantity)
                            print(f'{ordered_quantity} x Small Chips added to your order')
                            time.sleep(2)                              
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('medium_chips', ordered_quantity)
                            print(f'{ordered_quantity} x Medium Chips added to your order')
                            time.sleep(2)                        
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '3':
                    try:
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('large_chips', ordered_quantity)
                            print(f'{ordered_quantity} x Large Chips added to your order')
                            time.sleep(2)           
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '4':
                    main_menu()
                    break
                case '5':
                    finalise_order()
                    break
                case _:
                    print(f'"{ordered_quantity}" is an invalid input, try again.')
                    time.sleep(2)


def mains_menu():
    while True:
        clear()
        display = pyfiglet.figlet_format("Mains", font = "bulbhead" )
        print(display)        
        print('Mains:')
        print('1. Onion Rings Supreme: €6')
        print('2. Onion Rings Deluxe: €7')
        print('3. BallybOnion Super Box: €10')
        print('4. Return back to Main Menu')
        print('5. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4', '5']
        if selection not in menu_options:
            print(f'"{selection}" is an invalid selection, please try again')
            time.sleep(2)
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  # Make sure to call isdigit()
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('onion_rings_supreme', ordered_quantity)
                            print(f'{ordered_quantity} x Onion Rings Supreme added to your order')
                            time.sleep(2)
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '2':
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('onion_rings_deluxe', ordered_quantity)
                            print(f'{ordered_quantity} x Onion Rings Deluxe added to your order')
                            time.sleep(2)
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '3':
                    try:
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('ballybonion_super_box', ordered_quantity)
                            print(f'{ordered_quantity} x BallybOnion Super Box added to your order')
                            time.sleep(2)                             
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '4':
                    main_menu()
                    break
                case '5':
                    finalise_order()
                    break
                case _:
                    print(f'"{ordered_quantity}" is an invalid input, try again.')
                    time.sleep(2)

def drinks_menu():
    while True:
        display = pyfiglet.figlet_format("Drinks", font = "bulbhead" )
        print(display)        
        clear()
        print('Drinks:')
        print('1. Coke: €2')
        print('2. Water: €2')
        print('3. Return back to Main Menu')
        print('4. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4']
        if selection not in menu_options:
            print(f'"{selection}" is an invalid selection, please try again')
            time.sleep(2)
        else:
            match selection:
                case '1': 
                    try:            
                        ordered_quantity = input('How many?\n')
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('coke', ordered_quantity)
                            print(f'{ordered_quantity} x Coke added to your order')
                            time.sleep(2)  
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '2':
                    try:
                        ordered_quantity = input('How many?\n')                                                
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('water', ordered_quantity)
                            print(f'{ordered_quantity} x Water added to your order')
                            time.sleep(2)                                    
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '3':
                    main_menu()
                    break
                case '4':
                    finalise_order()
                    break
                case _:
                    print(f'"{ordered_quantity}" is an invalid input, try again.')
                    time.sleep(2)

def desserts_menu():
    while True:
        clear()
        display = pyfiglet.figlet_format("Desserts", font = "bulbhead" )
        print(display)        
        print('Desserts:')
        print('1. Nutella Onion Rings: €5')
        print('2. Pistachio Onion Rings: €5.50')
        print('3. Return back to Main Menu')
        print('4. Finalise your order')
    
        selection = input('Please select from the options above\n')
        menu_options = ['1', '2', '3', '4']
        if selection not in menu_options:
            print(f'"{selection}" is an invalid selection, please try again')
            time.sleep(2)
        else:
            match selection:
                case '1': 
                    try:
                        ordered_quantity = input('How many?\n')                                                
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('nutella_onion_rings', ordered_quantity)
                            print(f'{ordered_quantity} x Nutella Onion Rings added to your order')
                            time.sleep(2)           
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '2':
                    try:
                        ordered_quantity = input('How many?\n')                        
                        if ordered_quantity == '0':
                            print(f'You entered {ordered_quantity}: You must order at least 1 item to add it to your order.')
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(f'You entered {ordered_quantity}: This is an invalid input, please try again.')
                            time.sleep(2)
                        elif ordered_quantity.isdigit():  
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item('pistachio_onion_rings', ordered_quantity)
                            print(f'{ordered_quantity} x Pistachio Onion Rings added to your order')
                            time.sleep(2) 
                    except ValueError:
                        print(f'"{ordered_quantity}" is an invalid input, try again.')
                        time.sleep(2)
                case '3':
                    main_menu()
                    break
                case '4':
                    finalise_order()
                    break
                case _:
                    print(f'"{ordered_quantity}" is an invalid input, try again.')
                    time.sleep(2)

# cancel items functionality based on code set out in https://www.geeksforgeeks.org/iterate-python-dictionary-using-enumerate-function/
def cancel_items():
    clear()
    valid_items = []
    total = 0
    for name, quantity in new_order.new_order.items():
        if quantity is not None:
            valid_items.append((name, quantity))
    
    if valid_items == []:
        print('There are no items currently on your order. Returning to Main Menu')
        time.sleep(2)
        main_menu()
    else:
        print('0. Return to Main Menu')
        for index, (name, quantity) in enumerate(valid_items, start=1):
            subtotal = (quantity * PRICES[name])
            total += subtotal 
            print(f'{index}. Cancel {quantity} x {NAMES[name]}: €{subtotal:.2f}?')
        print(f'Total: €{total:.2f}')
        print('Please note that selecting an item will remove every portion of it from your order.')
        print('')
        print("Please select option")    
        while True:
            try:
                selection = int(input('\n'))
                if selection == 0:
                    main_menu()
                    break
                elif selection <= len(valid_items):  # Check if selection is within valid range
                    remove_item(selection)
                    if not valid_items:
                        print('There are no items currently on your order. Returning to Main Menu')
                        time.sleep(2)
                        main_menu()
                        break
                else:
                    print(f'{selection} is an invalid input.')
            except ValueError:
                print(f"{selection} is an invalid input. Please enter a number.")
                        
# remove item functionality based on code set out in https://www.geeksforgeeks.org/python-filter-non-none-dictionary-keys/
def remove_item(index):
    # Adjust index for zero-based indexing
    adjusted_index = index - 1
    
    # Filter out None values and convert dictionary items to a list
    items_list = [(k, v) for k, v in new_order.new_order.items() if v is not None]
    
    try:
        # Remove the item based on the adjusted index
        removed_item = items_list.pop(adjusted_index)
        del new_order.new_order[removed_item[0]]
        print(f"Item '{NAMES[removed_item[0]]}' has been removed.")
        time.sleep(2)
        cancel_items()
    except IndexError:
        print("Invalid selection. Please choose a valid index.")
        time.sleep(2)
        cancel_items()


def display_order():
    clear()
    current_order = []
    total = 0
    for name, quantity in new_order.new_order.items():
        if quantity is not None:
            current_order.append((name, quantity))
    
    if current_order == []:
        print('There are no items currently on your order. Returning to Main Menu')
        time.sleep(2)
        main_menu()
    else:
        print('Your Order:')
        print('')
        for name, quantity in current_order:
            subtotal = (quantity * PRICES[name])
            total += subtotal 
            print(f'{quantity} x {NAMES[name]}: €{subtotal:.2f}')
        print(f'Total: €{total:.2f}')
        print('')
        print('1. Return to Main Menu')
        print('2. Cancel items')
        print('3. Finalise order')
        while True:
            answer = input('Please make selection\n')
            if answer not in ['1', '2', '3']:
                print(f'{answer} is not a valid input, please try again')
            else:
                match (answer):
                    case '1':
                        main_menu()
                        break
                    case '2':
                        cancel_items()
                        break
                    case '3':
                        finalise_order()
                        break

def finalise_order():
    display_finalised_order()
    print('')
    print('This is your order. Would you like to make any changes before submitting it to our ununionised onion peddlers?')
    print('')
    print('1. Return to Main Menu')
    print('2. Cancel items from order')
    print('3. Proceed to Payment')
    while True:
            answer = input('Please make selection\n')
            if answer not in ['1', '2', '3']:
                print(f'{answer} is not a valid input, please try again')
                time.sleep(2)
                finalise_order()
            else:
                match (answer):
                    case '1':
                        main_menu()
                        break
                    case '2':
                        cancel_items()
                        break
                    case '3':
                        process_payment()
                        break

def display_finalised_order():
    clear()
    current_order = []
    total = 0
    for name, quantity in new_order.new_order.items():
        if quantity is not None:
            current_order.append((name, quantity))
    
    if current_order == []:
        print('There are no items currently on your order. Returning to Main Menu')
        time.sleep(2)
        main_menu()
    else:
        print('Your Finalised Order:')
        print('')
        for name, quantity in current_order:
            subtotal = (quantity * PRICES[name])
            total += subtotal 
            print(f'{quantity} x {NAMES[name]}: €{subtotal:.2f}')
        print(f'Total: €{total:.2f}')

def process_payment():
    clear()
    pattern = r'^[0-9]{4}$'
    print('Processing Order')
    time.sleep(0.3)
    clear()
    print('Processing Order.')
    time.sleep(0.3)
    clear()
    print('Processing Order..')
    time.sleep(0.3)
    clear()
    print('Processing Order...')
    time.sleep(0.3)
    clear()
    print('Processing Order')
    time.sleep(0.3)
    clear()
    print('Processing Order.')
    time.sleep(0.3)
    clear()
    print('Processing Order..')
    time.sleep(0.3)
    clear()
    print('Processing Order...')
    time.sleep(0.3)
    clear()
    while True:
        pin = input('Please enter your four-digit bank card pin number that we will not record on our servers...\n')
        match = re.match(pattern, pin)
        if match:
            clear()
            print('Thank you')
            time.sleep(1)
            clear()
            print('Processing Payment')
            time.sleep(0.3)
            clear()
            print('Processing Payment.')
            time.sleep(0.3)
            clear()
            print('Processing Payment..')
            time.sleep(0.3)
            clear()
            print('Processing Payment...')
            time.sleep(0.3)
            clear()       
            print('Processing Payment')
            time.sleep(0.3)
            clear()
            print('Processing Payment.')
            time.sleep(0.3)
            clear()
            print('Processing Payment..')
            time.sleep(0.3)
            clear()
            print('Processing Payment...')
            time.sleep(0.3)
            clear()
            print('Payment Approved.')
            print('')
            display = pyfiglet.figlet_format("Thanks for your Custom", font = "bulbhead" )
            print(display)
            time.sleep(2)
            reset_new_order()
            startscreen()
            break
        else:
            print(f"'{pin}' is not a valid four digit pin code, please try again.")
            time.sleep(2)

def reset_new_order():
    for i in new_order.new_order:
        new_order.new_order[i] = None


if __name__ == "__main__":
    clear()
    new_order = NewOrder()
    startscreen()