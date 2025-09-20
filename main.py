def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(book_contents)

def word_count(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(f"{len(book_contents.split())} words found in the document")


        
def main():
    book = "books/frankenstein.txt"
    return word_count(book)
    

if __name__ == "__main__":
    main()