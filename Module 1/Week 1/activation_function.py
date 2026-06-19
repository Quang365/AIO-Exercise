import math

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def interactive_activation_function():
    x = input("Input x: ")
    input_function = input("Input Activation Function (sigmoid|relu|elu): ")

    if not is_number(x):
        print("x must be a number.")
        return
    
    x = float(x)
    if input_function == "sigmoid":
        result = 1 / (1 + math.exp(-x))
    elif input_function == "relu":
        result = max(0, x)
    elif input_function == "elu":
        result = x if x > 0 else 0.01 * (math.exp(x) - 1)
    else:
        print(f"{input_function} is not supported.")
        return
    
    print(f"{input_function}: f({x}) = {result}")
    
interactive_activation_function()
