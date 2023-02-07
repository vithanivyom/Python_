'''

Display three string “Name”, “Is”, “James” as “Name**Is**James”

'''

def Print_string(str):                     # defining function
    string = str.split(' ')                # split the string
    for i in string:                       # print '**' for every new word
        print(i,"**",end=" ")

c1 = Print_string("my name is vyom")