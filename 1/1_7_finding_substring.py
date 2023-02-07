'''

Return the count of a given substring from a string

'''

def Substring(s1,s2):                           # defining Sugstringing function
    string = s1                                 
    substring = s2

    count = string.count(substring)            # finding substring into main string

    return count                               # returning total count of substring in main string

string = input("enter string")
substring = input ("eneter substring")

c1 = Substring(string,substring)               # calling function

print(c1)
