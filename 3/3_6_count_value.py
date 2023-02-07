'''

Count the total number of digits in a number

'''

def count_value(n):                                 # defining function
    n = str(n)                                      # convert int into string
    return len(n)                                   # calculate len of string

c1 = count_value(100)                               # calling function
print(c1)