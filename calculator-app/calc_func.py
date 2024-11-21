
# addition function
def do_addition(a:int, b:int):
    return a+b

# substraction function
def do_substraction(a,b):
    return a-b

# division function
def do_division(a,b):
    try: 
        return a/b
    except ZeroDivisionError as e:
        return "Cannot divide by zero"