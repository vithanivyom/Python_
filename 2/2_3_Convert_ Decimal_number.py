'''

Convert Decimal number to octal using print() output formatting

'''
def convert(n):              # defining the function
    out = oct(n)             # convert int to octal
    return (out[2:])         # return octal value

n = convert(8)               # calling function
print(n)