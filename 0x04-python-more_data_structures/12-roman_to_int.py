#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) != str):
        return
    number = 0
    i = 0
    len_string = len(roman_string)
    while (i < len_string):
        if (roman_string[i] == 'I'):
            if (i + 1 < len_string):
                if (roman_string[i + 1] == 'V'):
                    number += 4
                    i += 1
                elif (roman_string[i + 1] == 'X'):
                    number += 9
                    i += 1
                else:
                    number += 1
            else:
                number += 1
        elif (roman_string[i] == 'V'):
            number += 5
        elif (roman_string[i] == 'X'):
            if (i + 1 < len_string):
                if (roman_string[i + 1] == 'L'):
                    number += 40
                    i += 1
                elif (roman_string[i + 1] == 'C'):
                    number += 90
                    i += 1
                else:
                    number += 10
            else:
                number += 10
        elif (roman_string[i] == 'L'):
            number += 50
        elif (roman_string[i] == 'C'):
            if (i + 1 < len_string):
                if (roman_string[i + 1] == 'D'):
                    number += 400
                    i += 1
                elif (roman_string[i + 1] == 'M'):
                    number += 900
                    i += 1
                else:
                    number += 100
            else:
                number += 100
        elif (roman_string[i] == 'D'):
            number += 500
        i += 1
    return (number)
