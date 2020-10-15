#arithmetic operations
first_number = input("Enter the first number:")
second_number = input("Enter the second number:")
operation = input("Please enter + , - , * or / :")

if operation == "+":
    print(int(first_number) + int(second_number))
elif operation == "-":
    print(int(first_number) - int(second_number))
elif operation == "*":
    print(int(first_number) * int(second_number))
elif operation == "/":
    print(int(first_number) / int(second_number))
