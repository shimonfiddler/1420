# def compare(num1,num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
    
# #print(compare(4,10))
# integerlist = []
# iters = 0
# while iters < 30:
#     integerlist.append(iters+1)
#     iters+=1
# print(integerlist)
# evenintslist = []
# evenintslist.append(integerlist[1::2])
# print(evenintslist)
# fiveevenslist = []
# fiveevenslist.append(integerlist[1:10:2])
# print(fiveevenslist)

# word = 'computing'
# print(word[3:6])

integerlist = [30, 21, 16, 66, 78, 109, 1, 4, 52]
nth_max = 2
nth_max -= 1
integerlist.sort(reverse=True)
print(integerlist[nth_max])

# def largestlistelement(inplist):
#     highest = 0
#     for i in inplist:
#         if i > highest:
#             highest = i
#     return(highest)

# Integers = [20, 9, 51, 81, 50, 42, 77]

# def listsorter(inplist):
#     high =[]
#     low = []
#     for i in inplist:
#         if i >= 50 or i%4 == 0:
#             high.append(i)
#         else:
#             low.append(i)
#     return(high,low)

# print(listsorter(Integers))