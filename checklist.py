#try adding colors to the terminal output
#from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.lightgrey + 'and with a green background')
#from colorama import init, Fore, Back, Style
checklist = list()
def create(item):
    checklist.append(item)
def read(index):
    item = mark_completed(index)
    return item
def update(index, item):
    checklist[index] = item
def destroy(index):
    checklist.pop(index)
def list_all_items():
    index = 0
    for list_item in checklist:
        print(" \u001b[33m {} {}".format (str(index), list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "√" + checklist[index]
    return checklist[index]
def unmark(index):
    item = checklist[index]
    #print(item)
    if item[0] == "√":
        item = item.replace(item[0], '')
        #print(item)
        return item
    else:
        print("Item was not marked no need to unmark")

def index_exist(index):
    if index < len(checklist):
        return True
    else:
         print("\u001b[31 Index out of bound, please enter a value between %d and %d" % (0, len(checklist)-1))

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("\u001b[36m Input item: ")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = user_input("\u001b[35m Index Number? ")
        # Remember that item_index must actually exist or our program will crash.
        if index_exist(int(item_index)):
            print(read(int(item_index)))
            #print(check_index(int(item_index)))
        #item_index = check_index(int(item_index))
    elif function_code == "X":
        index_unmarked = user_input("\u001b[35m Index Number? ")
        unmarked_item = unmark(int(index_unmarked))
        update (int(index_unmarked), unmarked_item)
    # update item
    elif function_code == "U":
        item_index_tobeupdated = user_input("\u001b[36m Index Number To be Updated? ")
        input_item_toupdate = user_input("Input item to replace:")
        if index_exist(int(item_index_tobeupdated)):
            update(int(item_index_tobeupdated), input_item_toupdate)
    # destroy item
    elif function_code == "D":
        item_index_tobedestroyed = user_input("\u001b[33m Index Number To be Destroyed?")
        if index_exist(int(item_index_tobedestroyed)):
            destroy(int(item_index_tobedestroyed))
    # Print all items
    elif function_code == "P":
        list_all_items()
    # This is where we want to stop our loop
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for the user input
    user_input = input(prompt)
    return user_input

def test():
    create("Purple socks")
    create("Yellow hat")
    create("Pink pants")

    #checklist.append("HI")

    #print(read(0))

    #mark_completed(0)
    #mark_completed(1)
    #mark_completed(2)
    ##create("Purple sox")
    ##create("red cloak")


    ##print(read(1))

    ##update(0, "Purple socks")

    ##destroy(1)

    ##print(read(0))

    ##mark_completed(0)

    #select("C")
    ##print(checklist)
    #list_all_items()

    #select("R")
    #print(read(index))
    #list_all_items()

    #select("P")
    #select("O")

    #user_value = user_input("Please Enter a value:")
    #print(user_value)

    #fix this if you have time redi :)
    #print(read(1))
test()

running = True
while running:

    selection = user_input("\033[32m Press C to add list, R to Read from list, X to unmark list, P to display list, U to update an item, D to destroy, and Q quit: \033[m")
    running = select(selection.upper())
