import unicodedata
import string

def palindrome(n):
    n = unicodedata.normalize('NFD', n)
    n = ''.join(i for i in n if i not in string.whitespace and i.isalnum())
    n = n.lower()
    return n == n[::-1]

my_text = input("Введіть текст для перевірки на паліндром: ")

if palindrome(my_text):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")