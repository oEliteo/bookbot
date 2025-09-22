def main():
    count_words(get_book_text("./books/frankenstein.txt"))
    return


def get_book_text(relative_path):
    with open(relative_path) as f:
        return f.read()


def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    print(f"{count} words found in the document")


main()
