# import randrange
import random

# PROMBLEM 1
class Instrument:
    # 1.1 - initializer
    def __init__(self, model, brand, strength):
        # attributes
        self.model = model
        self.brand = brand
        self.strength = strength

    # 1.2 - string representation
    def __str__(self):
        # variables
        strength_percentage = self.strength * 100
        instrument_string = f"{self.brand} {self.model} ({strength_percentage} / 100 strength)"

        # return
        return instrument_string
    
    # 1.3 - has the instrument broken?
    def does_break(self):
        # variables
        random_float = random.random() # generates a random decimal number [0.0, 1.0)

        # condtionals
        if random_float < (self.strength / 2):
            # return
            return True # instrument has broken
        
        else:
            # return
            return False # instrument has not broken
        

# PROBLEM 2
class Musician:
    # 2.1 - initializer
    def __init__(self, stage_name, instruments):
        # attributes
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(self.instruments)
    
    # 2.2 - official string representation (repr)
    def __repr__(self):
        # condtionals
        if self.number_of_instruments > 0:
            # variable
            musician_string = f"Musician object '{self.stage_name}', owning a "

            # for-loop
            for instrument_index in range(self.number_of_instruments):
                # conditionals
                if instrument_index == (self.number_of_instruments - 1):
                    musician_string += f"and a {self.instruments[instrument_index]}"

                else:
                    musician_string += f"{self.instruments[instrument_index]}, "

        else:
            # variable
            musician_string = f"Musician object '{self.stage_name}' does not own any instruments"
            
        # return
        return musician_string
    

    # 2.3 - pick an instrument
    def pick_instrument(self, instrument_index = None):
        # conditionals
        if self.number_of_instruments == 0:
            # return
            return None
        
        elif instrument_index == None:
            # variable
            instrument_index = random.randrange(self.number_of_instruments)
            chosen_instrument = self.instruments[instrument_index]

        elif instrument_index >= self.number_of_instruments:
            # variable
            chosen_instrument = self.instruments[-1]

        else:
            # variable
            chosen_instrument = self.instruments[instrument_index]

        # return
        return chosen_instrument


# PROBLEM 3
# 3.1
def get_name_of_battle_winner(musician1, musician2):
    # conditionals
    if (musician1.number_of_instruments == 0) and (musician2.number_of_instruments == 0):
        return "NO CONTEST"
    
    elif (musician1.number_of_instruments == 0) or (musician2.number_of_instruments == 0):
        # codntionals
        if musician1.number_of_instruments == 0:
            winner = musician2

        else:
            winner = musician1
    
    else: # battle occurs
         # pick instrument for first musician 
            # input --> user chooses whether or not to pass in a value for the first musician's instrument index
        instrument_index1 = input(f"If you would like to pass in a value for {musician1.stage_name}'s instrument index, enter an integer, otherwise ENTER: ")

            # conditionals
        if instrument_index1 == "":
            instrument1 = musician1.pick_instrument()
        
        else:
            instrument1 = musician1.pick_instrument(int(instrument_index1))

        # pick random instrument for second musician
            # input --> user chooses whether or not to pass in a value for the first musician's instrument index
        instrument_index2 = input(f"If you would like to pass in a value for {musician2.stage_name}'s instrument index, enter an integer, otherwise ENTER: ")

            # conditionals
        if instrument_index2 == "":
            instrument2 = musician2.pick_instrument()
        
        else:
            instrument2 = musician2.pick_instrument(int(instrument_index2))

        # pre-prints
        print(f"{musician1.stage_name} picked a {instrument1}")
        print(f"{musician2.stage_name} picked a {instrument2}")

        # condtionals
        if instrument1.strength > instrument2.strength: # musician1's
            # condtionals
            if instrument1.does_break():
                # pre-print
                print(f"{musician1.stage_name}'s {instrument1} broke!")

                # variable
                winner = musician2.stage_name

            else:
                # variable
                winner = musician1.stage_name
        
        elif instrument1.strength < instrument2.strength:
            # condtionals
            if instrument2.does_break():
                # pre-print
                print(f"{musician2.stage_name}'s {instrument2} broke!")

                # variable
                winner = musician1.stage_name

            else:
                # variable
                winner = musician2.stage_name

        else:
            # variable
            coin_toss = random.randint(1,2)

            # pre-print
            print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")

            # conditionals
            if coin_toss == 1: # heads
                winner = musician1.stage_name

            else: # tails
                winner = musician2.stage_name

    # return
    return winner


def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)

    gear = [danelectro, fender_vi, four_double_o_one]

    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)

    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10

    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")

main()
