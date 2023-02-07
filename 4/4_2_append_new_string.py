'''

Append new string in the middle of a given string

'''

def Append(n,m):
    string1 = n
    string2 = m
    x = ''
    middle = int(len(string1)/2)
    x = string1[:middle:]
    x +=string2
    x +=string1[middle:]


    return x

c1 = Append('vyom','abc')
print(c1)