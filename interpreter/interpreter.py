def main():
    expr = input("Enter an arithmetic expression: ")
    result = calculate(expr)
    print(f"Result: {result:.1f}")


def calculate(expr):
    x, op, y = expr.split()
    x, y = float(x), float(y)
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y


if __name__ == "__main__":
    main()

