text = input("Введіть текст: ")

lower_letters = "аеєиіїоуюя"
upper_letters = "АЕЄИІЇОУЮЯ"

dragon_text = ""
for i in text:
    if i in lower_letters:
        dragon_text += 'а'
    elif i in upper_letters:
        dragon_text += 'А'
    else:
        dragon_text += i

print(dragon_text)