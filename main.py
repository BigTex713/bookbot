from stats import word_count, char_count, dict_list, sort_on

def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(book_contents)
        
def main():
    book = "books/frankenstein.txt"
    
    
    print(word_count(book))
    return dict_list((char_count(book)))
    

if __name__ == "__main__":
    main()