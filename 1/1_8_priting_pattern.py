'''

Print the following pattern

1
22
333
4444
55555
'''

def Pattern(x,y):                          # defining function
    for i in range(1,x+1):                 
        for j in range(1,y+1):
            if j<=i:                       # if value of j is less than or eual to i, print i
                print(i, end=' ')
            else:
                print(' ',end= ' ')        # else print space without creating new line
        print()                            # create new line

p1 = Pattern(5,5)                          # calling Pattern function