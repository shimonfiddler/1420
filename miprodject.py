import os
userscreen=[['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','','']]
clearuserscreen=[['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','','']]
clearuserscreen = tuple(clearuserscreen)
def arrow(): #sob 100
    userscreen = []
    current = []
    for i in range(0,5):
        current.append('*')
        userscreen += current
        userscreen.append('\n')
    for i in range(0,4):
        current.pop(0)
        userscreen += current
        userscreen.append('\n')
    print(*userscreen,sep='')
#arrow()
def screenprint(whattoshow):
    #os.system('cls||clear')
    for i in range(0,len(whattoshow)):
            print(*whattoshow[i],sep=' ')
            
def arrow(userscreen,offset):  #sob101
    for i in range(0,5):
        userscreen[i][i+offset]='*'
    for i in range(0,4):
        userscreen[5+i][3-i+offset]='*'
    screenprint(userscreen)

def pyramid(userscreen): #breaks after screen higher than 8, draws extra wrong
    layer = 0
    for i in range(0,len(userscreen)):
        offset = 0
        for i in range(0,layer+1):
            offset+=1
            userscreen[layer][int((len(userscreen[layer])/2)-layer+offset)] ='*'            
        layer += 1
    screenprint(userscreen)  
    
arrow(userscreen,0)
#pyramid(userscreen)
userscreen = clearuserscreen
arrow(userscreen,1)
#print(clearuserscreen)
userscreen = clearuserscreen
arrow(userscreen,3)
 
#pyramid(userscreen)
#still have mutability bug