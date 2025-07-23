def calculator():
    while True:
        print("\nSelect operation: +, -, *, / or 'q' to quit")
        op = input("Enter operator: ")

        if op == 'q':
            print("Exiting calculator.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operator")

calculator()