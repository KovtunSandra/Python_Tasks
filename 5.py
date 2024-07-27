import string

def pangram(text):
    text = text.lower()
    alphabet = set(string.ascii_lowercase)
    letters_in_text = set(i for i in text if i in alphabet)
    return letters_in_text == alphabet

my_text = input("Введіть текст для перевірки на панграму: ")

if pangram(my_text):
    print("Текст є панграмою.")
else:
    print("Текст не є панграмою.")