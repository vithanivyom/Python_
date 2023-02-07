'''

Create a string made of the middle three characters

'''

def middle_three_character(n):                  # define function               
    middle = int(len(n)/2)                      # find value of middle index
    print(n[middle-1:middle+2])                 # print middle three character

c1 = middle_three_character("JhonDipPeta")      # calling function