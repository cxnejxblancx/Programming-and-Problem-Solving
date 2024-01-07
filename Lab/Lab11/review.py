# 1
    # a --> var = [1, 8, 3]
    # b --> var = "Exam ii"
    # c --> ERROR
    # d --> var = 1
    # e --> var = ERROR
    # f --> var = [1, 2, 3, [4, 5]]
    # g --> ERROR
    # h --> -1 (if find is can't find the value in the string, it will return -1)
    # i --> var = "abc"
    # j --> var = [1, 2, 3, 20, 30]

# 2
"""
    >>> main msg1: n = 10
    >>> func1 msg2: n = 9 # n = 9
    >>> func2 msg2: n = 7 # n = 7
                          # n = 5
    >>> func2 msg3: n = 5
    >>> func2 msg3: n = 9
    >>> main msg2: n = 10

"""

# 3
"""
    func1([''])
    # char_list = ['']
    # chars = '!$%\t\t&*()_+=-}{[]|."'
    # char_list = [')_+=']
    # char_list = [')_+=', '{}-']
    # char_list = [')_+=', '{}-', '\']
    # char_list = [')_+=', '{}-', '\', '+']
    # char_list = ['."', '{}-', '\', '+']
    # char_list = ['."', '|', '{}-', '\', '+']

    func2(['."', '|', '{}-', '\', '+'], 'ot$frozn$iyo$q2wu') --> returns func3(some_str.upper())
    # some_str = 'ot\frozn\iyo\q2wu'
    # some_list = ['u', 'y', 'n']
    # some_str = 'u-y-n' 
        # return func3('U-Y-N') --> 'N-Y-U'

            func3('U-Y-N')
            # output = ''
            # output --> each character gets added before the previous chracter --> reverse the string
            # output = 'N-Y-U'   

    >>> N-Y-U
"""

# 4
PokeWorld = [['Pichu','Pikachu','Raichu'], ['Abra', 'Kadabra', 'Alakazam'], ['Oshawott', 'Dewott', 'Samurott']]

def cardInDeck(user_deck, given_card): # return True or false
    if given_card in user_deck:
        return True
    else:
        return False

def getEvolutionSet(PokeWorld, name_poke_card):
    for pokemon in PokeWorld:
        if pokemon[0] == name_poke_card: # if basic
            return []
        elif pokemon[1] == name_poke_card: # if Stage 1
            return [pokemon[0]]
        elif pokemon[2] == name_poke_card: # if Stage 2
            return [pokemon[0], pokemon[1]] 

def canPlayCard(PokeWorld, player_deck, single_card):
    can_be_played = True
    list_of_previous_stages = getEvolutionSet(PokeWorld, single_card)
    if len(list_of_previous_stages) > 0: # if card not basic
        for card in list_of_previous_stages:
            if card not in player_deck: # if card isn't in the player's deck
                can_be_played = False
    return can_be_played

def checkDeck(PokeWorld, player_deck):
    unplayable_cards = []
    for ind_card in player_deck:
        if not canPlayCard(PokeWorld, player_deck, ind_card):
            unplayable_cards.append(ind_card)

    return unplayable_cards

def main():
    print(checkDeck(PokeWorld, ['Raichu', 'Samurott', 'Pikachu', 'Pichu', 'Dewott']))

main()

"""
dict = {1: "Hello",
        2: "no"}
for value in dict: # just iterating through thebasically dict.keys()
    print(dict[value])

dict.update({5: "five"})
for key in dict:
    print(f"dict({key}) = {dict[key]}")
"""
