'''
Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5


'''


def Pattern(x,y):                          # defining function
    for i in range(1,x+1):                 
        for j in range(1,y+1):
            if j<=i:                       # if value of j is less than or eual to i, print i
                print(j, end=' ')
            else:
                print(' ',end= ' ')        # else print space without creating new line
        print()                            # create new line

p1 = Pattern(5,5)                          # calling Pattern function