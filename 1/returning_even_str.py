'''
Print characters from a string that are present at an even index number
'''

def return_even_index(s):        # defining function
    string = ''                  # empty string
    for i in range(1,len(s),2):  # assessing all even values from given string using for loop
        string += s[i]           # concatenation in string
    return string                # return string
    

value = input("eneter string :")
string = return_even_index(value)    # calling return_even_index function
print(string)