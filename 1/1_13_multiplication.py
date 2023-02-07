'''
Print multiplication table form 1 to 10

'''

def multiplication(n):                 # calling function
    for i in range(1, n):              # defining range from 1 to n for table
        for j in range(1, 11):          # defining range form 1 to 10 for multiplication
            print(i * j, end=" ")       # multiplication
        print("\t\t")

c1 = multiplication(20)
