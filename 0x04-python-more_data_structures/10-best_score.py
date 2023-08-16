#!/usr/bin/python3
def best_score(a_dictionary):
    '''
    Returns a key with the biggest integer value

    >>> my_dict = {'a': 10, 'b': 20, 'c': 5}
    >>> largest = best_score(my_dict)
    >>> if largest:
            print(f"The key with the largest value is '{largest_key}'")
        else:
            print("The dictionary is empty")

    The key with the largest value is 'b'
    '''
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
