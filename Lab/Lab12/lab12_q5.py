def add_entry(contacts, name, number):
    """
    Adds a new entry to a dictionary of contacts
    :param contacts: dictionary of contacts
    :param name: str of contact name
    :param number: str of contact's phone number
    """

    # conditionals
    if name not in contacts:
        if (len(number) == 10) and (number.isdigit()):
            contacts[name] = number

        else:
            print(f"ERROR: {number} is not a valid phone number.")

    else:
        print(f"ERROR: {name} is already in the contact list .")

def lookup(contacts, name):
    """
    Returns phone number for a contact name if contact exists in contacts
    :param contactS: dictionary of contacts
    :param name: str of contact name
    :return: str of contact's number if contact in contacts, otherwise error
    """
    # conditionals
    if name in contacts:
        print(contacts[name])
    else:
        print(f"ERROR: {name} is not in the contact list")

def delete_entry(contacts, name):
    """
    Deletes a contact from a contacts dictionary
    :param contacts: dictionary of contacts
    :param name: str of contact name
    """
    
    # conditionals
    if name in contacts:
        del contacts[name]

    else:
        print(f"ERROR: {name} is not in the contact list")

def print_all(contacts):
    """
    Displays all contacts in contacts
    :param contacts: dictionary of contacts
    """

    # for-loop
    for name in contacts:
        print(name, contacts[name], sep = '\t\t')

def main():
    # input
    option = input("Please enter an option: ")

    # variable
    contact_list = {}

    # while-loop
    while option != 'Q':
        # conditionals
        if option == 'A':
            # variables
            new_name = input("Please enter a name: ")
            new_number = input("Please enter a phone number: ")

            # function call
            add_entry(contact_list, new_name, new_number)
            print()

        elif option == "L":
            # variable
            desired_name = input("Please enter a name: ")

            # function call
            lookup(contact_list, desired_name)
            print()

        elif option == "D":
            # variable
            undesired_name = input("Please enter a name: ")

            # function call
            delete_entry(contact_list, undesired_name)
            print()

        elif option == "P":
            # function call
            print_all(contact_list)
            print()
        
        # input
        option = input("Please enter an option: ")

main()
