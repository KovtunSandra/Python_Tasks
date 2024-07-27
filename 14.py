def anagrams(words):
    anagram_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    anagram_groups = [group for group in anagram_dict.values() if len(group) > 1]
    return anagram_groups


words = input("Введіть ваші слова: ").split()
anagram_groups = anagrams(words)

if anagram_groups:
    print("Групи анаграм:")
    for group in anagram_groups:
        print(group)
else:
    print("Анаграм немає.")