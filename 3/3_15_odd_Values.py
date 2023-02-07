'''

Use a loop to display elements from a given list present at odd index positions

'''

def odd_values(n):                          # defining the function
    for i in range(0,len(n),2):             # access odd index
        print(n[i])                         # access odd values

c1 = odd_values([10,20,30,40,50])