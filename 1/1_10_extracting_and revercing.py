'''

to extract each digit from an integer in the reverse order.

'''

def Extrecting(number):                       # defining function
    while number > 0:

        digit = number % 10                   # get last digit
        number = number // 10                 # remove the last digit and repeat the loop
        print(digit, end=" ")


number = 7536

c1 = Extrecting(number)                        # calling function