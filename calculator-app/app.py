
from calc_func import do_addition, do_substraction

def main():
    print('Welcome to the calculator app')
    print("""\nselect the function from the given options:
          1. Add
          2. Substract""")

    user_input = input ('Select the Function: ')

    a = int(input('Enter the value of A: '))
    b = int(input('Enter the value of B: '))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_substraction(a,b)

    print("Result: ", result)

if __name__ == "__main__":
    main()