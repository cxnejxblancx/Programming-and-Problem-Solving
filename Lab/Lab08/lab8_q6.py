# PART A: Prompt the User For a Password
def prompt_user_for_pw():
    """
    Prompts for input for a password
    Returns a string of the user's input
    """

    # input
    user_pw = input("Please create a password: ")
    
    # retur
    return user_pw

# PART B: Validating the Password's Strength
def is_strong_pw(pw):
    """
    Returns a bool indicating whether the given string is a strong password according
    to the rules defined previously
    """
    # a STRONG PASSWORD is a pw that:
        # Is greater than or equal to 8 characters in length
        # Contains at least 1 special character from the following: "!", "@", "#", "*"
        # Contains at least 1 uppercase character
        # Contains at least 1 lowercase character
        # Contains at least 1 number

    # booleans
    is_of_sufficient_length = False
    has_special_char = False
    has_upper = False
    has_lower = False
    has_number = False

    # conditional
    if len(pw) >= 8:
        is_of_sufficient_length = True
    
    # for-loop
    for char in pw:
        # conditionals
        if char in "!@#*":
            has_special_char = True

        if char.isupper():
            has_upper = True
        
        if char.islower():
            has_lower = True

        if char.isdigit():
            has_number = True

    # booleans
    is_strong_pw = (is_of_sufficient_length and has_special_char and has_upper and has_lower and has_number)

    # return
    return is_strong_pw

# PART C: Repeatedly Prompt For A Password
def main():
    # pre-print
    print("Welcome! ")
    password = prompt_user_for_pw()

    # while-loop
    while not is_strong_pw(password):
        print('Password too weak! Strong passwords must be greater than or equal to 8 characters in length, contain at least 1 special character from the following: "!", "@", "#", "*" contain at least 1 uppercase character, contain at least 1 lowercase character, and contain at least 1 number')
        password = prompt_user_for_pw()

    # final print
    print("Thank you! Your password is considered strong.")

main()
