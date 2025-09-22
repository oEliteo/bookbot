import sys

from stats import (
    count_characters,
    count_words,
    seperate_character_dictionaries,
    sort_helper,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    char_dict_list = seperate_character_dictionaries(char_count)
    char_dict_list.sort(key=sort_helper, reverse=True)

    head = f"""============ BOOKBOT ============
            Analyzing book found at {book_path}...
            ----------- Word Count ----------
            Found {word_count} total words
            --------- Character Count -------"""

    tail = """============= END ==============="""
    head = head.split("\n")
    for line in head:
        print(line.lstrip())
    print_char_dict_list_lines(char_dict_list)
    print(tail)

    return


def print_char_dict_list_lines(dict_list):
    for item in dict_list:
        print(f"{item["char"]}: {item["num"]}")


def get_book_text(relative_path):
    with open(relative_path) as f:
        return f.read()


main()
