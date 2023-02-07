'''

Count all letters, digits, and special symbols from a given string

'''

def counting(s):                                # define the function
    digit = []                                  # list, to store digit
    letters = []                                # list, to store letters
    special = []                                # list, to store special characters
    for i in s:
        if i.isdigit():                         # check that character is letter or digit or special character
            digit.append(i)
        elif i.islower() or i.isupper():
            letters.append(i)
        else:
            special.append(i)
    print(digit)
    print(letters)
    print(special)

c1 = counting('Vy1@')
