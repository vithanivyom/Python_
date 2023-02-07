'''

Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
output:
Sum is: 38 Average is  6.333333333333333

'''

def find_string(s):                     # define function
    num = 0                             # store sum of int value
    for i in s:                         # access string
        if i.isdigit():                 # if i is digit than added in num
            dummy = int(i)
            num +=dummy
    avg = num
    avg = avg/2                         # find avg. of num
    print(num)
    print(avg)

c1 = find_string('abw123+45')
