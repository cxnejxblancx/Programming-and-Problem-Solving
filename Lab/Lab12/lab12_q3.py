def count_vowels(filename):
    """
    Counts total number of each vowel in the given file.
    :param filename: str of the file to read from
    :return: dict of format {"vowel": int}
    """
    # open file
    text = open("sample_text.txt", 'r')

    # variables
    string = ""
    vowels = "AEIOU"

    # for-loop
    for line in text:
      line = line.strip().upper()
      for char in line:
        if char in vowels:
          string += char

    # list comprehension
    vowel_dict = {vowel: string.count(vowel) for vowel in vowels}

    # return
    return vowel_dict

# tester
print(count_vowels("sample_text.txt"))
