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