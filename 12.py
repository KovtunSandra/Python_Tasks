def count_vowels(word):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    return sum(1 for i in word if i in vowels)

def sorting_words(words):
    return sorted(words, key=lambda word: count_vowels(word))

words = input("Введіть ваші слова: ").split()

sorted_words = sorting_words(words)
print("Слова за к-тю голосних букв:")
print(sorted_words)