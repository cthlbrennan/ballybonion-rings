# import time for sleep method
import time

# random module to generate random order number for customer at end of order
import random

# import os and sys for self-defined clear function
import os
import sys

# import regular expressions module for re.match() method for payment process -
# based on Harvard's CS50P course -
# https://www.youtube.com/watch?v=hy3sd9MOAcc&t=1s
import re

# use of pyfiglet based on code found in
# https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
import pyfiglet

# use of colorama based on code found in
# https://www.geeksforgeeks.org/print-colors-python-terminal/
from colorama import init, Fore, Back

# The dictionaries NAMES and PRICES below are capitalised,
# as per the convention
# for denoting variables as constants which should
# not be changed - https://peps.python.org/pep-0008/#constants

NAMES = {
    "small_onion_rings": "Small Onion Rings",
    "mozzarella_sticks": "Mozzarella Sticks",
    "small_chips": "Small Chips",
    "medium_chips": "Medium Chips",
    "large_chips": "Large Chips",
    "onion_rings_supreme": "Onion Rings Supreme",
    "onion_rings_deluxe": "Onion Rings Deluxe",
    "ballybonion_super_box": "BallybOnion Super Box",
    "coke": "Coke",
    "water": "Water",
    "nutella_onion_rings": "Nutella Onion Rings",
    "pistachio_onion_rings": "Pistachio Onion Rings",
}

PRICES = {
    "small_onion_rings": 3.00,
    "mozzarella_sticks": 3.00,
    "small_chips": 3.00,
    "medium_chips": 3.50,
    "large_chips": 4.00,
    "onion_rings_supreme": 6.00,
    "onion_rings_deluxe": 7.00,
    "ballybonion_super_box": 10.00,
    "coke": 2.00,
    "water": 2.00,
    "nutella_onion_rings": 5.00,
    "pistachio_onion_rings": 5.50,
}


class NewOrder:
    def __init__(self):
        self.new_order = {
            "small_onion_rings": None,
            "mozzarella_sticks": None,
            "small_chips": None,
            "medium_chips": None,
            "large_chips": None,
            "onion_rings_supreme": None,
            "onion_rings_deluxe": None,
            "ballybonion_super_box": None,
            "coke": None,
            "water": None,
            "nutella_onion_rings": None,
            "pistachio_onion_rings": None,
        }

    def add_item(self, item, quantity):
        """this method adds a number of a selected menu item to the
        new_order instance variable's dictionary"""
        if item in self.new_order and self.new_order[item] is None:
            self.new_order[item] = quantity
        elif item in self.new_order and self.new_order[item] is not None:
            existing_quantity = self.new_order[item]
            new_quantity = quantity + existing_quantity
            self.new_order[item] = new_quantity
        else:
            print(f"Item '{item}' not found.")


def startscreen():
    """this function brings up the welcome screen"""
    clear()
    result = pyfiglet.figlet_format(
        "Welcome to BallybOnion Rings", font="bulbhead"
        )
    print(Fore.YELLOW + result)
    print("Ballybunion's greatest purveyor of pun-based")
    print("(or should we say pun-ion-based) fast foods!" + Fore.RESET)
    make_an_order = input("Would you like to make an order? y/n\n")

    if make_an_order.lower() == "y":
        main_menu()
    elif make_an_order.lower() == "n":
        not_make_order()
    else:
        print(
            Fore.RED
            + f"{make_an_order} is invalid. Please input either y or n"
            + Fore.RESET
        )
        time.sleep(2)
        startscreen()


# code based on https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    """this function clears text on the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def not_make_order():
    """if a customer at the welcome screen decides not to make an order,
    this is the screen which they are sent to"""
    clear()
    print("That's ok! Come back soon when you're not so poor and/or feckless!")
    print(
        Fore.RED
        + "Please vacate the premises immediately."
        + Fore.RESET
    )
    answer = input(Fore.GREEN + "New customer? y/n\n" + Fore.RESET)
    while True:
        if answer.lower() == "y":
            startscreen()
            break
        elif answer.lower() == "n":
            vacate_premises()
            break
        else:
            print(
                Fore.RED
                + f"{answer} is an invalid input, please try again"
                + Fore.RESET
            )
            time.sleep(1)
            not_make_order()


def vacate_premises():
    """this function threatens an awkward non-customer with legal action"""
    clear()
    print(Fore.RED + "This terminal has recorded a photographic image of you.")
    print("It will be relayed to An Garda Siochána")
    print("and will be the basis for a")
    print("trespassing charge against you.")
    print("Please remove yourself from the premises")
    print("and allow the next customer to order." + Fore.RESET)
    time.sleep(7)
    startscreen()


def main_menu():
    """This brings up the main menu, with various
    options from sub menus to cancellations to finalising an order"""
    clear()
    display = pyfiglet.figlet_format("Main Menu", font="bulbhead")
    print(Fore.YELLOW + display)
    print("Please select from one of the following sub menus:")
    print("1. Starters")
    print("2. Sides")
    print("3. Mains")
    print("4. Drinks")
    print("5. Desserts")
    print("6. Display current order")
    print("7. Cancel items from current order")
    print("8. Finalise order")
    print("9. Cancel order" + Fore.RESET)

    while True:
        # use of match cases based on
        # https://www.youtube.com/watch?v=_b6NgY_pMdw
        menu_selection = input(
            "Please input the number which corresponds with your selection\n"
        )
        match (menu_selection):
            case "1":
                starters_menu()
                break
            case "2":
                sides_menu()
                break
            case "3":
                mains_menu()
                break
            case "4":
                drinks_menu()
                break
            case "5":
                desserts_menu()
                break
            case "6":
                display_order()
                break
            case "7":
                cancel_items()
                break
            case "8":
                finalise_order()
            case "9":
                cancel_order()
                break
            case _:
                print(
                    Fore.RED
                    + f"{menu_selection} is an invalid selection."
                    + Fore.RESET
                )
                time.sleep(2)
                main_menu()


def cancel_order():
    """this code represents the cancel order selection from the main menu"""
    while True:
        clear()
        print(Fore.BLUE + "Just pack it in and go home? y/n" + Fore.RESET)
        answer = input("\n")
        if answer.lower() == "y":
            clear()
            print("Fair enough, come back when you're")
            print("not going to waste our time!")
            time.sleep(3)
            reset_new_order()
            startscreen()
            break
        elif answer.lower() == "n":
            clear()
            print("Then get busy buying stuff please!")
            time.sleep(3)
            main_menu()
            break
        else:
            print(
                Fore.RED +
                f"{answer} is an invalid input. Try again, y/n"
                + Fore.RESET
                )
            time.sleep(2)


def starters_menu():
    """the starters menu as selected from the main menu"""
    while True:
        clear()
        display = pyfiglet.figlet_format("Starters", font="bulbhead")
        print(Fore.YELLOW + display)
        print("Starters:")
        print("1. Small Onion Rings: €3")
        print("2. Mozzarella Sticks: €3")
        print("3. Return back to Main Menu")
        print("4. Finalise your order" + Fore.RESET)

        selection = input("Please select from the options above\n")
        menu_options = ["1", "2", "3", "4"]
        if selection not in menu_options:
            print(
                Fore.RED
                + f'"{selection}" is an invalid selection, please try again'
                + Fore.RESET
            )
            time.sleep(2)
        else:
            match selection:
                case "1":
                    # use of try and except keywords based on Code Institute
                    # Python Essentials module
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to "
                                + "add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "small_onion_rings",
                                ordered_quantity
                                )
                            if new_order.new_order['small_onion_rings'] is not None:
                                print(
                                    f"{ordered_quantity} x Small Onion Rings"
                                    + " added to your order"
                                    )
                            else:
                                print('Failed to add small onion rings to your order')
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "2":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item"
                                + " to add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "mozzarella_sticks",
                                ordered_quantity
                                )
                            print(
                                f"{ordered_quantity} x Mozzarella Sticks"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "3":
                    main_menu()
                    break
                case "4":
                    finalise_order()
                    break
                case _:
                    print(
                        Fore.RED
                        + f'"{ordered_quantity}" is an invalid input,'
                        + ' try again.'
                        + Fore.RESET
                    )
                    time.sleep(2)


def sides_menu():
    """the sides menu as selected from the main menu"""
    while True:
        clear()
        display = pyfiglet.figlet_format("Sides", font="bulbhead")
        print(Fore.YELLOW + display)
        print("Sides:")
        print("1. Small Chips: €3")
        print("2. Medium Chips: €3.50")
        print("3. Large Chips: €4")
        print("4. Return back to Main Menu")
        print("5. Finalise your order" + Fore.RESET)

        selection = input("Please select from the options above\n")
        menu_options = ["1", "2", "3", "4", "5"]
        if selection not in menu_options:
            print(
                Fore.RED
                + f'"{selection}" is an invalid selection, please try again'
                + Fore.RESET
            )
            time.sleep(2)
        else:
            match selection:
                case "1":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item("small_chips", ordered_quantity)
                            print(
                                f"{ordered_quantity} x Small Chips"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "2":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "medium_chips",
                                ordered_quantity
                                )
                            print(
                                f"{ordered_quantity} x Medium Chips"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "3":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item("large_chips", ordered_quantity)
                            print(
                                f"{ordered_quantity} x Large Chips"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except:
                        print(Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET)
                        time.sleep(2)
                case "4":
                    main_menu()
                    break
                case "5":
                    finalise_order()
                    break
                case _:
                    print(
                        Fore.RED
                        + f'"{ordered_quantity}" is an invalid input,'
                        + ' try again.'
                        + Fore.RESET
                        )
                    time.sleep(2)


def mains_menu():
    """the mains menu as selected from the main menu"""
    while True:
        clear()
        display = pyfiglet.figlet_format("Mains", font="bulbhead")
        print(Fore.YELLOW + display)
        print("Mains:")
        print("1. Onion Rings Supreme: €6")
        print("2. Onion Rings Deluxe: €7")
        print("3. BallybOnion Super Box: €10")
        print("4. Return back to Main Menu")
        print("5. Finalise your order" + Fore.RESET)

        selection = input("Please select from the options above\n")
        menu_options = ["1", "2", "3", "4", "5"]
        if selection not in menu_options:
            print(
                Fore.RED
                + f'"{selection}" is an invalid selection, please try again'
                + Fore.RESET
            )
            time.sleep(2)
        else:
            match selection:
                case "1":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "onion_rings_supreme",
                                ordered_quantity
                                )
                            print(
                                f"{ordered_quantity} x Onion Rings Supreme"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "2":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "onion_rings_deluxe",
                                ordered_quantity
                                )
                            print(
                                f"{ordered_quantity} x Onion Rings Deluxe"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "3":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "ballybonion_super_box", ordered_quantity
                            )
                            print(
                                f"{ordered_quantity} x BallybOnion Super Box"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "4":
                    main_menu()
                    break
                case "5":
                    finalise_order()
                    break
                case _:
                    print(
                        Fore.RED
                        + f'"{ordered_quantity}" is an invalid input,'
                        + ' try again.'
                        + Fore.RESET
                        )
                    time.sleep(2)


def drinks_menu():
    """the drinks menu as selected from the main menu"""
    while True:
        clear()
        display = pyfiglet.figlet_format("Drinks", font="bulbhead")
        print(Fore.YELLOW + display)
        print("Drinks:")
        print("1. Coke: €2")
        print("2. Water: €2")
        print("3. Return back to Main Menu")
        print("4. Finalise your order" + Fore.RESET)

        selection = input("Please select from the options above\n")
        menu_options = ["1", "2", "3", "4"]
        if selection not in menu_options:
            print(
                Fore.RED
                + f'"{selection}" is an invalid selection, please try again'
                + Fore.RESET
            )
            time.sleep(2)
        else:
            match selection:
                case "1":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item("coke", ordered_quantity)
                            print(
                                f"{ordered_quantity} x Coke"
                                + " added to your order"
                                )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "2":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item("water", ordered_quantity)
                            print(
                                f"{ordered_quantity} x Water"
                                + " added to your order")
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "3":
                    main_menu()
                    break
                case "4":
                    finalise_order()
                    break
                case _:
                    print(
                        Fore.RED
                        + f'"{ordered_quantity}" is an invalid input,'
                        + ' try again.'
                        + Fore.RESET
                        )
                    time.sleep(2)


def desserts_menu():
    """the desserts menu as selected from the main menu"""
    while True:
        clear()
        display = pyfiglet.figlet_format("Desserts", font="bulbhead")
        print(Fore.YELLOW + display)
        print("Desserts:")
        print("1. Nutella Onion Rings: €5")
        print("2. Pistachio Onion Rings: €5.50")
        print("3. Return back to Main Menu")
        print("4. Finalise your order" + Fore.RESET)

        selection = input("Please select from the options above\n")
        menu_options = ["1", "2", "3", "4"]
        if selection not in menu_options:
            print(
                Fore.RED
                + f'"{selection}" is an invalid selection, please try again'
                + Fore.RESET
            )
            time.sleep(2)
        else:
            match selection:
                case "1":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "nutella_onion_rings",
                                ordered_quantity
                                )
                            print(
                                f"{ordered_quantity} x Nutella Onion Rings"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "2":
                    try:
                        ordered_quantity = input("How many?\n")
                        if ordered_quantity == "0":
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " You must order at least 1 item to"
                                + " add it to your order."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif int(ordered_quantity) < 0:
                            print(
                                Fore.RED
                                + f"You entered {ordered_quantity}:"
                                + " This is an invalid input, please try again."
                                + Fore.RESET
                            )
                            time.sleep(2)
                        elif ordered_quantity.isdigit():
                            ordered_quantity = int(ordered_quantity)
                            new_order.add_item(
                                "pistachio_onion_rings", ordered_quantity
                            )
                            print(
                                f"{ordered_quantity} x Pistachio Onion Rings"
                                + " added to your order"
                            )
                            time.sleep(2)
                    except ValueError:
                        print(
                            Fore.RED
                            + f'"{ordered_quantity}" is an invalid input,'
                            + ' try again.'
                            + Fore.RESET
                        )
                        time.sleep(2)
                case "3":
                    main_menu()
                    break
                case "4":
                    finalise_order()
                    break
                case _:
                    print(
                        Fore.RED
                        + f'"{ordered_quantity}" is an invalid input,'
                        + ' try again.'
                        + Fore.RESET
                        )
                    time.sleep(2)


# cancel items functionality based on code set out in
# https://www.geeksforgeeks.org/iterate-python-dictionary/
def cancel_items():
    """the functionality within the cancel items sub menu
    to remove individual items from an order"""
    clear()
    valid_items = []
    total = 0
    for name, quantity in new_order.new_order.items():
        if quantity is not None:
            valid_items.append((name, quantity))

    if valid_items == []:
        print(
            "There are no items currently on your order." +
            " Returning to Main Menu"
            )
        time.sleep(2)
        main_menu()
    else:
        print("0. Return to Main Menu")
        for index, (name, quantity) in enumerate(valid_items, start=1):
            subtotal = quantity * PRICES[name]
            total += subtotal
            print(
                f"{index}. Cancel {quantity} x {NAMES[name]}: €{subtotal:.2f}?"
            )
        print(f"Total: €{total:.2f}")
        print(
            Fore.RED
            + "Please note that selecting an item will remove every")
        print("portion of it from your order." + Fore.RESET)
        print("")
        print("Please select option")
        while True:
            try:
                selection = input("\n")
                if selection.isdigit() == False:
                    print(f'{selection} is an invalid option, please try again.')
                    time.sleep(2)
                    cancel_items()
                elif selection.isdigit() == True:
                    selection = int(selection)
                if selection == 0:
                    main_menu()
                    break
                # Check if selection is within valid range
                elif selection <= len(valid_items):
                    remove_item(selection)
                    if not valid_items:
                        print(
                            "There are no items currently on your order."
                            + " Returning to Main Menu"
                        )
                        time.sleep(2)
                        main_menu()
                        break
                else:
                    print(
                        Fore.RED
                        + f"{selection} is an invalid input."
                        + Fore.RESET
                        )
                    time.sleep(2)
                    cancel_items()
            except ValueError:
                print(
                    Fore.RED
                    + f"{selection} is an invalid input."
                    + " Please enter a number."
                    + Fore.RESET
                )


# remove item functionality based on code set out in
# https://www.geeksforgeeks.org/python-filter-non-none-dictionary-keys/
def remove_item(index):
    """function used in cancel_items() to remove an item from an order"""
    # adjust index for zero-based indexing
    adjusted_index = index - 1

    # list comprehension based on
    # https://www.w3schools.com/python/python_lists_comprehension.asp
    items = [(k, v) for k, v in new_order.new_order.items() if v is not None]

    try:
        # Remove the item based on the adjusted index
        removed_item = items.pop(adjusted_index)
        del new_order.new_order[removed_item[0]]
        print(
            Fore.MAGENTA
            + f"Item '{NAMES[removed_item[0]]}' has been removed."
            + Fore.RESET
        )
        time.sleep(2)
        cancel_items()
    except IndexError:
        print(
            Fore.RED
            + "Invalid selection. Please choose a valid index." + Fore.RESET
        )
        time.sleep(2)
        cancel_items()


def display_order():
    """functionality for display order sub menu"""
    clear()
    current_order = []
    total = 0
    for name, quantity in new_order.new_order.items():
        if quantity is not None:
            current_order.append((name, quantity))

    if current_order == []:
        print(
            "There are no items currently on your order."
            + " Returning to Main Menu")
        time.sleep(2)
        main_menu()
    else:
        print(Fore.YELLOW + "Your Order:")
        print("")
        for name, quantity in current_order:
            subtotal = quantity * PRICES[name]
            total += subtotal
            print(f"{quantity} x {NAMES[name]}: €{subtotal:.2f}")
        print(f"Total: €{total:.2f}" + Fore.RESET)
        print("")
        print("1. Return to Main Menu")
        print("2. Cancel items")
        print("3. Finalise order")
        while True:
            answer = input("Please make selection\n")
            if answer not in ["1", "2", "3"]:
                print(
                    Fore.RED
                    + f"{answer} is not a valid input, please try again"
                    + Fore.RESET
                )
                time.sleep(2)
                display_order()
            else:
                match (answer):
                    case "1":
                        main_menu()
                        break
                    case "2":
                        cancel_items()
                        break
                    case "3":
                        finalise_order()
                        break


def finalise_order():
    """functionality for finalise order sub menu"""
    display_finalised_order()
    print("")
    print(
        "This is your order. Would you like to make any changes"
        + " before submitting it?"
    )
    print("")
    print("1. Return to Main Menu")
    print("2. Cancel items from order")
    print(Fore.GREEN + "3. Proceed to Payment" + Fore.RESET)
    while True:
        answer = input("Please make selection\n")
        if answer not in ["1", "2", "3"]:
            print(
                Fore.RED
                + f"{answer} is not a valid input, please try again"
                + Fore.RESET
            )
            time.sleep(2)
            finalise_order()
        else:
            match (answer):
                case "1":
                    main_menu()
                    break
                case "2":
                    cancel_items()
                    break
                case "3":
                    process_payment()
                    break


def display_finalised_order():
    """function used as part of finalise_order()"""
    clear()
    current_order = []
    total = 0
    for name, quantity in new_order.new_order.items():
        if quantity is not None:
            current_order.append((name, quantity))

    if current_order == []:
        print(
            "There are no items currently on your order."
            + " Returning to Main Menu"
        )
        time.sleep(2)
        main_menu()
    else:
        print(Fore.YELLOW + "Your Finalised Order:")
        print("")
        for name, quantity in current_order:
            subtotal = quantity * PRICES[name]
            total += subtotal
            print(f"{quantity} x {NAMES[name]}: €{subtotal:.2f}")
        print(f"Total: €{total:.2f}" + Fore.RESET)


def process_payment():
    """functionality for when user selects Proceed to Payment
    from Finalise Order menu"""
    clear()
    pattern = r"^[0-9]{4}$"
    print(Fore.BLUE + "Processing Order")
    time.sleep(0.3)
    clear()
    print("Processing Order.")
    time.sleep(0.3)
    clear()
    print("Processing Order..")
    time.sleep(0.3)
    clear()
    print("Processing Order...")
    time.sleep(0.3)
    clear()
    print("Processing Order")
    time.sleep(0.3)
    clear()
    print("Processing Order.")
    time.sleep(0.3)
    clear()
    print("Processing Order..")
    time.sleep(0.3)
    clear()
    print("Processing Order..." + Fore.RESET)
    time.sleep(0.3)
    clear()
    while True:
        # as stated above, code below based on CS50P's lecture on regex
        pin = input(
            "Please enter your four-digit bank card pin number"
            + " that we will not record...\n"
        )
        match = re.match(pattern, pin)
        if match:
            clear()
            print(Fore.GREEN + "Thank you" + Fore.RESET)
            time.sleep(1)
            clear()
            print(Fore.BLUE + "Processing Payment")
            time.sleep(0.3)
            clear()
            print("Processing Payment.")
            time.sleep(0.3)
            clear()
            print("Processing Payment..")
            time.sleep(0.3)
            clear()
            print("Processing Payment...")
            time.sleep(0.3)
            clear()
            print("Processing Payment")
            time.sleep(0.3)
            clear()
            print("Processing Payment.")
            time.sleep(0.3)
            clear()
            print("Processing Payment..")
            time.sleep(0.3)
            clear()
            print("Processing Payment..." + Fore.RESET)
            time.sleep(0.3)
            clear()
            print(Fore.GREEN + "Payment Approved." + Fore.RESET)
            print("")
            time.sleep(2)
            clear()
            display = pyfiglet.figlet_format(
                "Thanks for your Custom",
                font="bulbhead"
                )
            print(Fore.YELLOW + display + Fore.RESET)
            order_number = random_number()
            print(
                Fore.YELLOW
                + "Your order number is " 
                + Fore.RESET
                + Fore.RED
                + str(order_number)
                + Fore.RESET
                )
            print(
                Fore.YELLOW
                + "Please collect your order from the desk "
                + "when your number is called."
                )
            print(
                "Once you have your stuff, please remove" 
                + " yourself from the premises!"
                + Fore.RESET
                )
            time.sleep(8)
            reset_new_order()
            startscreen()
            break
        else:
            print(
                Fore.RED
                + f"'{pin}' is not a valid four digit pin code,"
                + " please try again."
                + Fore.RESET
            )
            time.sleep(2)
            clear()


def random_number():
    '''function to generate a 4 digit 
    random integer for the process payment function'''
    random_number = random.randint(1000, 9999)
    return random_number


def reset_new_order():
    """within dictionary of NewOrder object instance,
    every value is set to None ahead of a new order from a new user"""
    for i in new_order.new_order:
        new_order.new_order[i] = None


# code below is based on best practice for command line applications that
# import modules
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    clear()
    init()
    new_order = NewOrder()
    startscreen()
