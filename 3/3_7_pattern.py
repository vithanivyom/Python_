'''

Print the following pattern
4 3 2 1 
3 2 1 
2 1 
1 

'''

def pattern (n):
    k = n                                   # use to print reverse value
    for i in range(1,n+1):                  # x axis
        for j in range(k-i,0,-1):           # y axis
            if j <= 5-i:                    # printing value using this condition
                print(j,end=" ")
            else:
                print(' ',end=" ")
        print()

c1 = pattern(5)