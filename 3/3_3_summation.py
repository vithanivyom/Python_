'''

Calculate the sum of all numbers from 1 to a given number


'''

def sum_of_n_number(n):
    summation = 0              # initally value of summation is 0
    for i in range(1,n+1):     # range of for loop is 0 to n
        summation +=i          # summation between current value and previous values
    return summation


c1 = sum_of_n_number(9)   # calling function
print(c1)