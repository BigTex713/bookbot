def word_count(book_file):
    with open(book_file) as f:
        book_contents = f.read()
        return (f"Found {len(book_contents.split())} total words")
        
def char_count(book_file):
    ltr_cnt_dict = {}
    
    with open(book_file) as f:
        book_contents = f.read()
        
        for ltr in book_contents.lower():
            if ltr in ltr_cnt_dict:
                ltr_cnt_dict[ltr] += 1
            elif ltr.isalpha():
                ltr_cnt_dict[ltr] = 1
    return ltr_cnt_dict

def dict_list(char_dict):
    new_dict_list = []
    
    for ltr in char_dict:
        blnk_dict = {}
            
        blnk_dict["char"] = ltr
        blnk_dict["num"] = char_dict[ltr]
            
        new_dict_list.append(blnk_dict)
    
    return new_dict_list

def sort_on(items):
    return items["num"]    