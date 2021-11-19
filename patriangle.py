import sys

# import numpy as np
# import pandas as pd
# from sklearn import ...
temp = ''
outstrin = ''
def pascallmaker(n,r=[]):
    for i in range(n):
        l = len(r)
        r = [1 if j == 0 or j == l else r[j-1]+r[j] for j in range(l+1)]
        yield r
#print(list(pascallmaker(6)))
for line in sys.stdin:
    #print(list(pascallmaker(6)))
    pascaltri = list(pascallmaker(6))
    for i in range(len(pascaltri)):
        temp = temp+str(pascaltri[i])+' ' #the space is needed or the output is wrong every new term

#print(temp)
for i in temp: #why is this such a pain
    #print (i)
    if i == '[' or i == ']' or i == ',' :
        pass
    else:
        outstrin += i
print(outstrin)