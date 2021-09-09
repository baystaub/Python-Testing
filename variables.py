import math

# Learning how to make a simply function and setting variables

x = 7
y = float(3.9)

print(x)
print(y)

x = str('This seems so much easier than javascript')

print(x)

# starting on functions now with know how to make variables in python
# testing these if else functions with code runner extention
x = 12
y = 12

if x < y :
    print('x is less than y')
elif y < x:
    print('y is less than x')
elif x == y:
    print('x and y are equal to each other')

# making set's and making it print sets using code runner extention

settest = {'ginger','ale','cola','soda'}

for x in settest:
    print(x)

settest.add('youtube')
settest.remove('cola')

for x in settest:
    print(x)

thisset = set(('orange','apples','bannanas'))

set3 = thisset.union(settest)

for x in set3:
    print('This is set3' + x)

# testing while loops using basic math with python

i = 0

while i < 20:
    i += 1
    if i == 10:
        continue
    print('still less than 20')

# Testing out import math features
# square rooting a number
x = math.sqrt(144)
print(x)
# ciel rounds up and floor rounds down
x = math.ceil(1.5)
y = math.floor(1.5)

print(x,y)


#python has a built in date and time function that you can import
import datetime

x = datetime.datetime.now()
print(x)

# using try and except variables in basic functions to print

try :
    print(z)
except:
    print('That variable is not defined try again')

# testing out inputs now

Fname = input("Whats your first name?")
Lname = input("Whats your last name?")

print("your name is" + Fname + Lname)


# trying to make a basic addition calculator


def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print ('select option:')
print('Add')
print('subtract')
print('Multiply')
print('Divide')

while True:
    choice = input("Enter your choice: 1, 2, 3, 4")

    if choice = ('1', '2', '3', '4')
        num1 = float(input('enter the first number'))
        num2 = float(input('enter the second number'))

        if choice == '1':
            print(num1, '+', num2, '=', add(num1,num2))
        elif choice == '2':
            print(num1, '-', num2, '=', sub(num1,num2))
        elif choice =='3':
            print(num1, '*', num2, '=', multiply(num1,num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1,num2))
        
        break
    else:
        print('invalid input, please try again')

#finished the calculator.