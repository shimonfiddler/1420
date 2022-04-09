from collections import namedtuple
# def lightswithpeds(state,state1,state2,state3,state4,state5,state6,state7): #
#     state = [True,True,True,True,True,True,True,True]
#     return(state)

# def lightswithpeds(L1,L2):
#     state = [[True,False,False],[False,False,True]]
#     return(state)
TFL = namedtuple('anamedtuple','red amber green')
def lightswithpeds(TFL):#Red,Amber,Green
    state = [True,False,False]
    return(state)