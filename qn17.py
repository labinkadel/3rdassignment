num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
ope = input("Enter the operator: ")


def fun(ope):
    if ope == '+':
        return num1 + num2
    elif ope == '-':
        return num1 - num2
    elif ope == '*':
        return num1 * num2
    else:
        try:
            return num1/num2
        except ZeroDivisionError:
            return f"Divide by 0 error"


print(fun(ope))