def factorial(n):
    if n < 0:
        raise ValueError("Помилка! Від'ємне число.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

try:
    number = int(input("Введіть число для обчислення факторіала: "))
    result = factorial(number)
    print(f"Факторіал числа {number} дорівнює {result}.")
except Exception as e:
    print(f"Помилка: {e}")