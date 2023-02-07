'''

Find words with both alphabets and numbers
input:
str1 = "Emma25 is Data scientist50 and AI Expert"
output:
Emma25
scientist50

'''
str1 = "avbf10 is Q23 gh "
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
