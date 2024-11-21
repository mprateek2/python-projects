
from calc_func import do_addition, do_substraction, do_division
from multiply import do_multiplication

def main():
    print('Welcome to the calculator app')
    print("""\nselect the function from the given options:
          1. Add
          2. Substract
          3. Multiply
          4. division """)

    user_input = input ('Select the Function: ')

    a = int(input('Enter the value of A: '))
    b = int(input('Enter the value of B: '))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_substraction(a,b)
    elif user_input == '3':
        result = do_multiplication(a,b)
    elif user_input == '4':
            result = do_division(a,b)
    print("Result: ", result)

if __name__ == "__main__":
    main()