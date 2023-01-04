def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

print("""
Calculator

1 - Add
2 - Subtract
3 - Multiply
4 - Divide

""")


while True:
    choice = input(">>> ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print('result: ', add(num1, num2))
        if choice == '2':
            print('result: ', sub(num1, num2))
        if choice == '3':
            print('result: ', mul(num1, num2))
        if choice == '4':
            print('result: ', div(num1, num2))
    
    
