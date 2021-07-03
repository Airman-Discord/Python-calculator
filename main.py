print("Python Calculator")

first_num = float(input("Enter your first number: "))

operation = input("Enter your operation: ")

second_num = float(input("Enter your second number: "))

if operation == "+":
    print(first_num + second_num)

elif operation == "-":
    print(first_num - second_num)

elif operation == "*":
    print(first_num * second_num)

elif operation == "/":
    print(first_num / second_num)

else:
    print("invalid")


