'''

Create a new string made of the first, middle, and last characters of each input string

'''

def new_string(s1,s2):                          # define function
    string1 = s1
    string2 = s2
    x = ''                                      # empty strind
    middle1 = int(len(string1)/2)               # find middle index of string 1
    middle2 = int(len(string2)/2)               # find middle index of string 2
    x += string1[0]                             # concatination in empty string
    x +=string2[0]
    x +=string1[middle1]
    x +=string2[middle2]
    x +=string1[middle1]
    x +=string2[middle2]
    return x

c1 = new_string('abcer','qwert')                # calling function
print(c1)