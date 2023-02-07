'''

Reverse a given integer number

'''


def reverce(n):                 # defining the function 
    n = str(n)                  # convert int into string
    for i in n[::-1]:           # reverce the string
        print(i)

c1 = reverce(100)               # calling the function