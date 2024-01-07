def create_grocery_inventory():
    """
    Prompts for user input to populate a grocery list
    :return: a dictionary of item keys with their quantities as values
    """

    # input
    inventory_entry = input("Please enter the item and quantity you own separated by a comma or DONE when complete: ")

    # variable
    inventory = {}

    # while-loop
    while inventory_entry != "DONE":
        # adjust variable
        inventory_entry = inventory_entry.split(',')

        # constants
        item_name = inventory_entry[0]
        item_amount = int(inventory_entry[1])

        # conditionals
        if item_name in inventory:
            inventory[item_name] += item_amount

        else:
            inventory[item_name] = item_amount

        # input
        inventory_entry = input("Please enter the item and quantity you own separated by a comma or DONE when complete: ")
    
    # return
    return inventory

def create_grocery_shopping_list(fridge_inventory):
    """
    Prompts for user input to populate a grocery shopping list given the
    current inventory of items
    :param fridge_inventory: dictionary of str key (item name) and int quantity
    :return: dictionary of item keys with their quantities to buy as values
    """

    # input
    shopping_entry = input("Please enter the item and quantity you desire separated by a comma or DONE when complete: ")

    # variable
    grocery_list = {}

    # while-loop
    while shopping_entry != "DONE":
        # adjust variable
        shopping_entry = shopping_entry.split(',')

        # constants
        desired_item = shopping_entry[0]
        desired_amount = int(shopping_entry[1])

        # conditionals
        if desired_item in fridge_inventory:
            # conditionals
            if fridge_inventory[desired_item] >= desired_amount:
                grocery_list[desired_item] = 0
            
            else:
                grocery_list[desired_item] = (desired_amount - fridge_inventory[desired_item])

        else:
            grocery_list[desired_item] = desired_amount

        # input 
        shopping_entry = input("Please enter the item and quantity you desire separated by a comma or DONE when complete: ")
    
    # return
    return grocery_list

def main():
    fridge_inventory = create_grocery_inventory()
    print()
    grocery_list = create_grocery_shopping_list(fridge_inventory)
    print()
    print("Your shopping list, based off of what you have in your fridge, should be:")
    print(grocery_list)

main()
