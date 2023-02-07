'''

Write a program to display all prime numbers within a range

'''
def prime_num(start,end):
    for num in range(start, end + 1):
        if num > 1:                                                     # if number is less than or equal to 1, it is not prime
            for i in range(2, num):
                if (num % i) == 0:                                      # not a prime number so break inner loop
                    break
            else:
                print(num)

start = 2
end = 100
c1 = prime_num(start,end)                                               # calling function
