# for i in range (6,19):
#     print(i,':00')
import random
num1 = random.randint(0,10)
num2 = random.randint(0,10)
answer = eval(input(f'what is {num1} + {num2} = '))
while answer != (num1+num2):
    answer = eval(input(f'Incorrect \nwhat is {num1} + {num2} = '))
print('correct')