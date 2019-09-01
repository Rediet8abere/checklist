#try adding colors to the terminal output
checklist = list()
def create(item):
    checklist.append(item)
def read(index):
    item = checklist[index]
    return item
def update(index, item):
    checklist[index] = item
def destroy(index):
    checklist.pop(index)
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format (str(index), list_item))
        index += 1

def mark_completed(index):
    checklist[int(index)] = str('√') + checklist[int(index)]
    print(checklist[index])

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        # Remember that item_index must actually exist or our program will crash.
        read(int(item_index))
    # update item
    elif function_code == "U":
        item_index_tobeupdated = user_input("Index Number To be Updated?")
        input_item_toupdate = user_input("Input item to replace:")
        update(int(item_index_tobeupdated), input_item_toupdate)
    # destroy item
    elif function_code == "D":
        item_index_tobedestroyed = user_input("Index Number To be Destroyed?")
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
    #create("hi")
    checklist.append("HI")

    mark_completed(0)
    ##create("Purple sox")
    ##create("red cloak")

    ##print(read(0))
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
    selection = user_input("Press C to add list, R to Read from list, P to display list, U to update an item, D to destroy, and Q quit: ")
    running = select(selection.upper())
