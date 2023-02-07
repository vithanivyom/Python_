'''

Print the sum of the current number and the previous number

'''
def sum_of_n_number(n):
    for i in range(0,n+1):     # range of for loop is 0 to n
        summation = 0          #initally value of summation is 0
        if i == 0:             # if value of n is 0, return 0
            print(" Sum of previous value {} is {}".format(i,i))
        else:
            summation = i+(i-1)   # else summation between current value and previous value
            print(" Sum of current value {} and previous value {} is {}".format(i,i-1,summation))


c1 = sum_of_n_number(9)   # calling function
