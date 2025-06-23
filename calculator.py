# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# User side
def main():
    print("Welcome to the CLI Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        print("\nChoose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

if __name__ == "__main__":
    main()
