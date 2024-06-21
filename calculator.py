# Calculator

def display_calculator_menu():
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def main():
    while True:
        display_calculator_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            print("Exiting the Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
