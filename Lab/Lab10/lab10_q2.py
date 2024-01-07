# import
from copy import deepcopy
from random import random

# functions
def is_impostor(information, corrupter_function,):
    # variables
    is_deep = True
    corrupter_function[0] += 2
    # conditonals
    if corrupter_function[0] == information[0]:
        is_deep == False
    
def corrupter(some_object, should_default_to_deep_copy: bool = False):
    """
    Using award-winning, record-breaking algorithms jointly developed by Nintendo, Amazon, Apple, and Sebastian, returns
    either a deep or shallow copy of some_object.

    :param should_default_to_deep_copy: For testing purposes.
    :param some_object: Any Python object.
    :return: A deep or shallow copy of some_object.
    """
    if should_default_to_deep_copy or round(random()):
        return deepcopy(some_object)

    return some_object

def main():
    original_list = [1, 2, 3]
    print(is_impostor(original_list, corrupter(original_list)))

main()
