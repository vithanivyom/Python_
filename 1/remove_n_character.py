'''
Remove first n characters from a string

'''

def remove_character(s,n):     # defining function
    string = ''               # empty string
    string += s[n:]            # removing first n characters from given string
    return string              # retrun final string

string = input("enter the string :")    # take string from user
n = int(input("enter value n :"))       # taking n and removing n element from given string

output = remove_character(string,n)     # calling function 
print(output)


