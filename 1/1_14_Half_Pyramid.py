'''
Print downward Half-Pyramid Pattern with Star (asterisk)

'''
def Half_pyramid(n):                      # defining function
    for i in range(1,n):                  # x- axis
        for j in range(1,n):              # y- axis
            if j <=n-i:                   # condition for print 
                print("*", end=" ")
            else:                         # else print space ' ' downward Half-Pyramid Pattern
                print(' ',end=" ")
        print()



c1 = Half_pyramid(5)                      # calling function