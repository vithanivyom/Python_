'''
Calculate the multiplication and sum of two numbers

'''

def multiplication_or_sum(n,num1, num2):
    if n==1:

        #multiplication of two number

        multiplication = num1 * num2
        return multiplication

    else:

        #summation of two number

        summation = num1+num2
        return summation

choice = int(input("please enter 1 for multiplication or 2 for summation"))       # enter choice. choice 1 for multiplication and 2 for summation
values = int(input("enter first value"))                                          # value of first element
values2 = int(input("eneter second value"))                                       # value of second element

answer = multiplication_or_sum(choice,values,values2)                             # value which is retrun from the function
print(answer)

