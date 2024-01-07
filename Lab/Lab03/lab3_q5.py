# initial value
resale_price = 5

# initial input
is_rare = input("Welcome to the Pokémon card price calculator! Is your card of a special rarity? (Y/N) ")

    # conditional
if is_rare == "Y":
    is_uncommon = input("Is your card uncommon? (Y/N) ")
    
    if is_uncommon == "Y":
        resale_price += 5
        
    else:
        is_rare = input("Is your card rare? (Y/N) ")

        if is_rare == "Y":
            resale_price += 15

# input continued...
is_holographic = input("Is your card holographic? (Y/N) ")

    # conditional
if is_holographic == "Y":
    is_reverse_holo = input("Is your card a reverse holo? (Y/N) ")

    if is_reverse_holo == "Y":
        resale_price += 10

    else:
        is_holo = input("Is your card a holo? (Y/N) ")

        if is_holo == "Y":
            resale_price += 15

        else:
            is_full_holo = input("Is your card a full holo? (Y/N) ")

            if is_full_holo == "Y":
                resale_price += 20

# input continued...
is_special = input("Is your card of a special Pokémon? (Y/N) ")

# conditional
if is_special == "Y":
    is_starter = input("Is your card of a starter? (Y/N) ")

    if is_starter == "Y":
        resale_price += 5

    else:
        is_legendary = input("Is your card of a legendary? (Y/N) ")

        if is_legendary == "Y":
            resale_price += 30

# final print
print("Your card has a final resale price of: $" + str(resale_price))
