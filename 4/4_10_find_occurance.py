'''

Write a program to count occurrences of all characters within a string
input: 
str1 = "Apple"
output:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}

'''

from collections import Counter

def occurrence(str):
    dic = Counter(str)
    return dic


s1 = occurrence('vyommvyoqw')
print(s1)
s2 = 'ghg'