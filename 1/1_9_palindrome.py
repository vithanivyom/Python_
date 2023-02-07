'''

Check Palindrome Number

'''

def Palindrome(n1):                    #defining function
    if n1 == n1[::-1]:                 # revercing the string
        return True                    
    
input = input("enter Number :")        # taking number as string
c1 = Palindrome(input)                 # calling function
print(c1)