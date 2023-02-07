'''

Create a string made of the first, middle and last character

'''

def access_string(n):                   # define function
    middle = int(len(n)/2)              # find value of middle index 
    print(n[0])                         # print fist value
    print(n[middle])                    # print middle value
    print(n[-1])                        # print last value


c1 = access_string('vyomq')