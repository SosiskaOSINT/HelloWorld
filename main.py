def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ділення на нуль неможливе!"

# Зчитуємо операцію та числа від користувача
operation = input("Виберіть операцію (+, -, *, /): ")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Виконуємо обрану операцію
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Невідома операція"

print(f"Результат: {result}")
