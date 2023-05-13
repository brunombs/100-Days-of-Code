from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

operations = {
    "*": multiply,
    "+": add,
    "/": divide,
    "-": subtract
}
def calculator():
    print(logo)
    n1 = float(input("What is the first number?: "))
    continue_awnser = True
    while continue_awnser == True:
        for operator in operations:
            print(operator)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        awnser = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {awnser}")

        continuar = input(f"Type 'y' to continue calculating with {awnser}, or type 'n' to start over: ")
        if continuar == 'y':
            n1 = awnser
        elif continuar == 'n':
            continue_awnser = False
            calculator()
        else:
            print("Invalid option.")
            break

calculator()