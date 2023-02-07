'''

Calculate the cube of all numbers from 1 to a given number

'''

def cube(n):                                                                    # defining function
    for i in range(n+1):                                                    
        print("number is {} and cube of {} is {}".format(i,i,i*i*i))            # print cube of number

c1 = cube(4)