from stats import count_words


def main():
    count_words(get_book_text("./books/frankenstein.txt"))
    return


def get_book_text(relative_path):
    with open(relative_path) as f:
        return f.read()


main()
