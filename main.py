from stats import word_count, char_count, dict_list, sort_on

def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(book_contents)
        
def main():
    book = "books/frankenstein.txt"
    
    
    print(word_count(book))
    
    book_dict = char_count(book)
    book_dict_list = dict_list(book_dict)
    book_dict_list.sort(reverse=True, key=sort_on)
    
    for ltr_dict in book_dict_list:
        dict_access_key = 0 #will use this to set the position in the dictionay list
        print(f"{book_dict_list[dict_access_key]['char']}: {book_dict_list[dict_access_key]['num']}/n")
        dict_access_key +=1
    

if __name__ == "__main__":
    main()