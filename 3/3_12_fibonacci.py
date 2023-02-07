'''

 Display Fibonacci series up to 10 terms

'''

def fibonacci(n):
    num1, num2 = 0, 1                       # init fist 2 value of fibonacci series
    for i in range(n+1):
        print(num1, end="  ")
        res = num1 + num2                   # summation of previous 2 values   
        num1 = num2                         # changing the values for num1 and num2
        num2 = res

c1 = fibonacci(10)