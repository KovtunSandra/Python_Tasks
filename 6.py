def make_acronym(phrase):
    ignoring_words = {"a", "an", "the", "and", "but", "or", "for", "yet", "so", "in", "on", "at", "by", "near", "with", "to", "of"}
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words if word.lower() not in ignoring_words)
    return acronym

my_phrase = input("Введіть фразу для створення акроніму: ")
acronym = make_acronym(my_phrase)

print(f"Акронім: {acronym}")