#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    Returns an integer value equivalent of input roman numeral.
    '''
    a = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for n in reversed(roman_string):
        if roman[n] < a:
            a -= roman[n]
        else:
            a += roman[n]
    return a
