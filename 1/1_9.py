'''
Given a two list of numbers, write a program to create a new list 
such that the new list should contain odd numbers from the first list and even numbers from the second list.
'''

def Merge(l1,l2):                                      # defining function
    new_list = []                                      # defining new_list which is empty

    for i in l1:                                       # for first list, append all odd values in new_list
        if i%2!=0:
            new_list.append(i)
    
    for j in l2:                                       # for second list, append all even values in new_list
        if j%2==0:
            new_list.append(j)

    return new_list                                    # return new_list

c1 = Merge([10,20,30,15,17],[10,20,40,13,15,17])       # calling function
print(c1)
