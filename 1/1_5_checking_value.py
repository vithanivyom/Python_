'''

Check if the first and last number of a list is the same

'''

def checking_number(l1):                      #defining function 
    if l1[0] == l1[-1]:                       # checking first and last value
        return True                           # returning True if correct
    
list = checking_number([10,20,30,10])         # calling function
print(list)