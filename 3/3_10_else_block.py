'''

Use else block to display a message “Done” after successful execution of for loop


'''

def else_block(n):                              #Defining function
    for i in range(n+1):                        
        print(i)
    else:                                       #else block in for loop
        print("Done!")

c1 = else_block(10)                             # calling funtion