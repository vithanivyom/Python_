'''

Arrange string characters such that lowercase letters should come first

'''

def lowercase(s):
    string1 = ''
    string2 = ''
    for i in s:
        if i.islower():
            string1 +=i
        else:
            string2 +=i
    return string1+string2
        

c1 = lowercase('vYoM')
print(c1)