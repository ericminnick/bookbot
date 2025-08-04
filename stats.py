def count_words(document):
    word_contents = document.split()
    print(f"Found {len(word_contents)} total words")


def character_count(document):
    characters = {}

    for ch in document:

        characters[ch.lower()] = characters.get(ch.lower(), 0) + 1
    return characters


def sort_ch_counts(ch_dict):

    sort_list = []

    for char in ch_dict:
        if char.isalpha():
            char_sort = {}
            char_sort["char"] = char
            char_sort["num"] = ch_dict[char]
        
            sort_list.append(char_sort)

    return sorted(sort_list, key=lambda num: num["num"], reverse=True)
