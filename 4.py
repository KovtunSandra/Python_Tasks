def pyramid(height, symbol):
    if height <= 0:
        print("Висота піраміди має бути додатнім числом.")
        return

    if not symbol:
        print("Символ не може бути порожнім.")
        return

    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        symbols = symbol * (2 * i - 1)
        print(spaces + symbols)


height = int(input("Введіть висоту піраміди: "))
symbol = input("Введіть символ для піраміди: ")

pyramid(height, symbol)
