def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count


def seperate_character_dictionaries(character_counts):
    dictionary_list = []
    for key in character_counts:
        if key.isalpha():
            dictionary_list.append({"char": key, "num": character_counts[key]})
        else:
            pass
    return dictionary_list


def count_characters(text):
    text = text.lower()
    character_dictionary = {}

    for char in text:
        if char not in character_dictionary:
            character_dictionary[char] = 1
        else:
            character_dictionary[char] += 1

    return character_dictionary


def sort_helper(char_dict):
    return char_dict["num"]
