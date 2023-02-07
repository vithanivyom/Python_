'''

Write a program to print multiplication table of a given number

'''


def sum_of_n_number(n):
    multiplication = 1              # initally value of summation is 1
    for i in range(1,n+1):          # range of for loop is 0 to n
        multiplication *=i          # multiplication between current value and previous values
    return multiplication


c1 = sum_of_n_number(5)             # calling function
print(c1)