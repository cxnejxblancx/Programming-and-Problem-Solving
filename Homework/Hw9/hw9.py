# import deepcopy
from copy import deepcopy

# PART 1
def get_chord_dictionary(filepath):
    # try-except --> open file
    try:
        chord_dataset = open(filepath, 'r')
    except FileNotFoundError:
        return {}

    # get rid of header
    chord_dataset.readline()

    # contants
    ROOT_IDX, CHORD_IDX, NOTES_IDX = 0, 1, 2

    # variable
    keys = []
    chord_dict = {}
    ind_chor_info = {}

    # for-loop --> iterate through each line of the file
    for line in chord_dataset:
        line = line.strip().split(',') # create a list of the line
        line[NOTES_IDX] = tuple(line[NOTES_IDX].split('-')) # make a tuple of the notes

        # conditional --> Check if key/root already is in the list
        if line[ROOT_IDX] not in keys:
            keys.append(line[ROOT_IDX]) # Add each disctinct key/root to the keys list

        # conditional --> Check if key is in the dictionary
        if key in chord_dict
            # conditional --> determine whether the root in the line is the one of the keys in keys list
            if line[ROOT_IDX] == key:
                ind_chor_info[line[CHORD_IDX]] = line[NOTES_IDX] # Add key-value pair to the ind_chor_infor when key is the chord and the value is the notes
                ind_chor_info.update(ind_chor_info) # Add each new chord-notes pair to the dictionary
                chord_dict[key] = deepcopy(ind_chor_info) # Add a full copy of the ind_chor dictionary as the value for the key
              
    # return
    return chord_dict


# PART 2
def get_possible_chords(given_notes, given_chord_dict):
    # variable
    possible_chords = [] # originally a list, so it can be modified/mutated

    # for-loop --> iterate through each root-value pair in the OVERARCHING dictionary
    for root, value in given_chord_dict.items(): 
        if root == given_notes[0]:
            # for-loop --> iterate through each chord name and tuple of notes pair WITHIN the general VALUES for each root
            for chord_name, notes_tuple in value.items(): 
                # flag
                all_notes_in_chord = True

                # for-loop --> iterate through each note in the given list of notes for each tuple of notes in every root every value in the loop
                for note in given_notes:
                    # conditional -->
                    if note not in notes_tuple:
                        # adjust flag
                        all_notes_in_chord = False

                # conditional --> determine if all of the notes in the given list of notes are in that individual chord for the root
                if all_notes_in_chord:
                    possible_chords.append(f"{root}{chord_name}")

    # adjust variable
    possible_chords = tuple(possible_chords)

    # return
    return possible_chords


# PART 3
def get_chord_progression(song_filepath, chord_dict_filepath):
    # try-except --> open the file
    try:
        song = open(song_filepath, 'r')
    except FileNotFoundError:
        return []
    
    # variables
    chord_progression = []
    dictionary = get_chord_dictionary(chord_dict_filepath)
  
    # for-loop --> iterate through each line of the broken song
    for line in song:
        line = line.strip().split(',')
        chord_progression.append(get_possible_chords(line, dictionary))

    # return
    return chord_progression


# PART 4
def write_progression_file(progression, filename):
    # open file
    prog_file = open(filename, 'w')

    # for-loop
    for item in progression:
        item = list(item)
        item = ','.join(item)
        print(item, file = prog_file)
        
    # close file
    prog_file.close()
