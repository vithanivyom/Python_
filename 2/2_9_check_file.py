'''

Check file is empty or not

'''

import os
os.stat
size = os.stat("/Users/vyomvithani/Documents/Pynative/2/test.txt").st_size          # reading file
if size == 0:                                                                       # if file is empty, print 'file is empty'
    print('file is empty')

