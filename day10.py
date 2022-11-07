# 2022/02/10
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mutiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
operations = {
    '+' : add,
    '-' : subtract,
    '*' : mutiply,
    '/' : divide,

}
def calculator():
    num1 = float(input('What\'s the first number?: '))
    for symbol in operations:
        print(symbol)
    over = False

    while not over :
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: ')) 
        answer = operations[operation_symbol](num1,num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ') == 'y':
            num1 = answer
        else:
            over = True
            calculator()
calculator()