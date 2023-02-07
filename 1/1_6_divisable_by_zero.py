'''
Display numbers divisible by 5 from a list

'''

def divisable_five(n):                     # defining function
    final = []                             #assign empty list for storing output
    for i in n:
        if i%5 == 0:                      # if value is divisible by 5 than append into final list
            final.append(i)
    return final

input = divisable_five([5,10,20,13,45])    # calling function
print(input)