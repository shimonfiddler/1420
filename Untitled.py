print('i')
import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
outlist = []
temp = ''
for line in sys.stdin:
    line = int(line)
    for i in range (line):
        #print(11**i)
        outlist.append(11**i)
print(outlist)
for i in range (0,len(outlist)):
    temp = temp + str(outlist[i])
print(temp)

#print(*outlist,sep=' ')
yield