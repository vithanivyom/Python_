'''

Accept a list of 5 float numbers as an input from the user


'''

def creating_list(n):                                       # define list
    list = []
    for i in range(0, n):
        print("Enter number at location", i, ":")
        item = float(input())                               # convert string intp float
        list.append(item)                                   # add it to the list
    return list

n = int(input("enter length of list"))
c1 = creating_list(n)
print(c1)
