'''

Find all occurrences of a substring in a given string by ignoring the case

'''

def count_string(s1,s2):                                        # defining function
    count = 0                                                   # count the repetation of given string
    dummy = s1.split(" ")                                       # split the string by space
    for i in dummy:
        if (s2.upper() in i) or (s2.lower() in i):              # counting repeating string
            count +=1
    return count
    
c1 = count_string('vyom. vyom','vyom')
print(c1)