'''

Accept numbers from a user

'''

def multiplication_or_sum(num1, num2):
    #summation of two number

    summation = num1+num2
    return summation


values = int(input("enter first value"))                                          # value of first element
values2 = int(input("eneter second value"))                                       # value of second element

answer = multiplication_or_sum(values,values2)                                    # value which is retrun from the function
print(answer)