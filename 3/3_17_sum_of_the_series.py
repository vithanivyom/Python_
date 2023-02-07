'''

 sum of the series

'''

def sum_of_series(n,start):             # defining the function
    dummy = start                       # base value
    sum = 0                             # total summation
    for i in range(0,n):                
        sum +=dummy                     # add value in sum variable
        dummy = (dummy*10)+start        # update base value
    return sum

c1 = sum_of_series(5,2)                 # calling function

print(c1)