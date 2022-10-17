pls = []
min = []
div = []
mul = []

while True:
    a = float(input())
    b = float(input())
    operation = input()

    if operation == "+":
        print(f"{a} {operation} {b} = {a + b}")
        pls.append(f"{a} {operation} {b} = {a + b}")

    elif operation == "-":
        print(f"{a} {operation} {b} = {a - b}")
        min.append(f"{a} {operation} {b} = {a - b}")

    elif operation == "/":
        print(f"{a} {operation} {b} = {a / b}")
        div.append(f"{a} {operation} {b} = {a / b}")

    elif operation == "*":
        print((f"{a} {operation} {b} = {a * b}"))
        mul.append((f"{a} {operation} {b} = {a * b}"))

    else:
        print("введена неверная операция!")

    print("+", pls)
    print("-", min)
    print("/", div)
    print("*", mul)
    print()