def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    while len(fib) < n:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)

    return fib


n = int(input("Введіть к-ть членів послідовності Фібоначчі: "))

fib_var = fibonacci(n)
print(f"Послідовність Фібоначчі до {n}-го члена: {fib_var}")