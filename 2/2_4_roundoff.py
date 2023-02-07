'''
Display float number with 2 decimal places using print()

'''

def Roundoff(n):                 # Defining function
    return ('%.2f' % n)          # Roundoff 

n = Roundoff(10.2345)            # Calling function
print(n)