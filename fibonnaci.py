def fibonacci(n):
    """ Generate and return fibonacci series till n terms """
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a+b
    return series

def main():
    """ Main function to take user input and display fibonacci series till n terms """
    try:
        num = int(input("Enter the number of fibonacci terms to display: "))
        if num <= 0:
            print("Please enter positive integer number as input")
        else:
            result = fibonacci(num)
            print("Fibonacci Series:", ", ".join(map(str,result)))
    except ValueError:
        print("Entered Invalid input, enter valid positive integer ")

if __name__ == "__main__":
    main()


