'''

Replace each special symbol with # in the following string
input:
str1 = '/*Jon is @developer & musician!!'
output:
##Jon is #developer # musician##

'''
import string

def replace(str1):
    replace_char = '#'                                  # Replace punctuations with #

    for char in string.punctuation:                     # string.punctuation to get the list of all special symbols
        str1 = str1.replace(char, replace_char)

    print("The strings after replacement : ", str1)

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)