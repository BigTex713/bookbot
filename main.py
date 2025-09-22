from stats import word_count, char_count

def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(book_contents)
        
def main():
    book = "books/frankenstein.txt"
    print(word_count(book) )
    print(char_count(book))
    

if __name__ == "__main__":
    main()