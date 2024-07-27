import math


def simple_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


number = int(input("Введіть число для перевірки на просте: "))

if simple_number(number):
    print(f"{number} є простим числом.")
else:
    print(f"{number} не є простим числом.")