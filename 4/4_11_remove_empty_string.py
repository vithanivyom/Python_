'''

Remove empty strings from a list of strings

input:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

output:
['Emma', 'Jon', 'Kelly', 'Eric']

'''

def remove_empty(s):
    string = []
    for i in s:
        if i :
            string.append(i)
    return string

s1 = remove_empty(['q','','er',' qr'])
print(s1)