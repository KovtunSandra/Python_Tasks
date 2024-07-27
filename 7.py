def roman_numbers(num):
    if not (1 <= num <= 3999):
        print("Число повинно бути від 1 до 3999")

    norm = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // norm[i]):
            roman_num += roman[i]
            num -= norm[i]
        i += 1
    return roman_num

number = int(input("Введіть число для перетворення від 1 до 3999: "))
print(f"Римський запис: {roman_numbers(number)}")