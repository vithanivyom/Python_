'''

Print the following pattern

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

rows = 5
for i in range(0, rows):            # for loop wroks from row 5
    for j in range(0, i + 1):
        print("*", end=' ')         # printing "*"
    print("\r")                     # printing new line

for i in range(rows, 0, -1):        # after row 5, this for loop works.
    for j in range(0, i - 1):       # printing "*"
        print("*", end=' ')         # printing new line
    print("\r")

