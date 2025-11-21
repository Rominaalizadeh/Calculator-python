print("Calculator".center(40, "═"))

while True:
    try:
        a = float(input("\n Prime number: "))
        op = input ("Operator(+ - * /): ")
        b = float(input("Second number:"))

        if op == "+":   print("Result →", a + b)
        elif op == "-": print("Result →", a - b)
        elif op == "*": print("Result →", a * b)
        elif op == "/":
            if b == 0:
                print("Error: Division by zero!")
            else:
                print(" Result→", a / b)
        else:
            print("Wrong operator")

        if input(" Again?(y/n): ").lower() != "y":
            print("Goodbye")
            break

    except ValueError:
        print("Please enter only numbers.")