#mathematical_operations
def opoperation_sum(num1, num2):
    return num1 + num2

def operation_subtraction(num1, num2):
    return num1 - num2

def operation_multiply(num1, num2):
    return num1 * num2

def operation_divide(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir entre 0"
    elif num1 == 0:
        return "El resultado es 0 porque el dividendo es 0"
    else:
        return num1 / num2