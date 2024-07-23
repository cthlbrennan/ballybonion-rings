import time

def startscreen():
    print("Welcome to BallybOnion Rings, Ballybunion's greatest purveyor of")
    print("pun-based (or should we say pun-ion-based) fast foods!")
    make_an_order = input("Would you like to make an order? y/n\n")

    if (make_an_order.lower() == 'y'):
        mainmenu()
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
    print("Please remove yourself from the premises and allow the next customer to order")
    time.sleep(5)
    startscreen()

startscreen()