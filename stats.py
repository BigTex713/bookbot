def word_count(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(f"{len(book_contents.split())} words found in the document")