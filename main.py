from stats import word_count, char_count, dict_list, sort_on
import sys

def get_book_text(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        print(book_contents)
        
def main():
    #sys.argv is used to pull in the book value 
    args = sys.argv
    
    if len(args) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:
        book = args[1]       
        book_dict = char_count(book)
        book_dict_list = dict_list(book_dict)
        book_dict_list.sort(reverse=True, key=sort_on)
        dict_access_key = 0 #will use this to set the position in the dictionay list
    


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")  
        print(word_count(book))
        print("--------- Character Count -------")
        for ltr_dict in book_dict_list:
            print(f"{book_dict_list[dict_access_key]['char']}: {book_dict_list[dict_access_key]['num']}")
            dict_access_key +=1
        print("============= END ===============")

if __name__ == "__main__":
    main()