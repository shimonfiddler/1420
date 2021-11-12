name = input('Enter name: ')
if name == 'shimon':
    print ('awesome')
    
import random
num1 = random.randint(1,9)
num2 = random.randint(1,9)
ans = num1+num2
print('What is',num1,'+',num2)
userans = eval(input(':'))
if userans == ans:
    print('correct')
else:
    print('Incorrect\n The answer is', ans)
    
print(1!=4)
print(4>4)
print(2>=2)
print(4/3!=5)
print(4%2!=12)
print(3!=3)
print(5**2==25)
print(4*5==2)
print(1==7)
print(2**0>4)

import random
value = 50
randnum=random.randint(0,100)
if randnum<value:
    print('Our number is bigger than the random')
elif randnum>value:
    print('Our value is a large number')
else:
    print('The numbers are equal')
print(randnum)

price = eval(input('Price is: '))
if price >= 300:
    price=price*.7
elif price >= 200:
    price=price*.8
elif price >= 100:
    price=price*.9
else:
    price=price*.95
print(price)

def celctofar():
    celc=eval(input('Enter the celsius to convert to farenhight: '))
    faren=(celc*(9/5)+32)
    print(faren)

def daytranslate():
    daynum=eval(input('Enter a number from 1-7: '))
    if daynum == 1:
        return('Monday')
    elif daynum == 2:
        return('Tuesday')
    elif daynum == 3:
        return('Wednesday')
    elif daynum == 4:
        return('Thusday')
    elif daynum == 5:
        return('Friday')
    elif daynum == 6:
        return('Sataday')
    elif daynum == 7:
        return('Sunday')

def cube(number):
    number=number**3
    return(number)

def divisibe_by_three(number):
    if number%3==0:
        cube(number)
        return(number)
    else:
        return(False)
    
def factorial(number):
    iters = 1
    result = 1
    while iters != number+1:
        result = result*iters
        iters+=1
    return(result)
number=5
number = factorial(number)
print(number)