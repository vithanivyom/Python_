def read_lines(n):
    with open(n,'r') as fp:                                                     # open file
        lines = fp.readline()                                                   # reading lines
        print(lines[4])                                                         # print 4th line

path = read_lines('/Users/vyomvithani/Documents/Pynative/2/test.txt')
