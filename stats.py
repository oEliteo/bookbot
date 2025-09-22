def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    print(f"{count} words found in the document")
