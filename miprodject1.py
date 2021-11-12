##Shimon Fiddler
#import os
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
def screenclr(userscreen): #should not be necessary implemented to try fix array persisting betweek functions NOT WORKING
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
    #print(userscreen)#shows screen should be clear
    return(userscreen)

# def arrow():
#     userscreen = []
#     current = []
#     for i in range(0,5):
#         current.append('*')
#         userscreen += current
#         userscreen.append('\n')
#     for i in range(0,4):
#         current.pop(0)
#         userscreen += current
#         userscreen.append('\n')
#     print(*userscreen,sep='')
# #arrow()
def screenprint(whattoshow):
    #os.system('cls||clear') #clears teminal output
    for i in range(0,len(whattoshow)):
            print(*whattoshow[i],sep=' ')
            
def arrow(userscreen,offset):
    #print(userscreen)
    for i in range(0,5):
        userscreen[i][i+offset]='*'
    for i in range(0,4):
        userscreen[5+i][3-i+offset]='*'
    screenprint(userscreen)
    #screenclr(userscreen)#without the screen persists NOT FIXED

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
#print(userscreen) #demonstrates the screen persist bug
userscreen=[['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','','']]#This works to fix the issue
#pyramid(userscreen)
arrow(userscreen,1)
screenclr(userscreen)#This dosent
arrow(userscreen,3)
