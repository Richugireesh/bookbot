from stats import get_num_word,char_count,sort_char
import sys
def get_book_text(path):
    with open(path) as f:
       # f is a file object
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_word = get_num_word(text)
    dict_char = char_count(text)
    sorted_dict_char = sort_char(dict_char)
    #print(f"{sorted_dict_char}")
    print(f'''
        ============ BOOKBOT ============
        Analyzing book found at {sys.argv[1]}...
        ----------- Word Count ----------
        Found {num_word} total words
        --------- Character Count -------''')
    for i in sorted_dict_char:
        if i["char"].isalpha():
            print(f"        {i["char"]}: {i["num"]}")

    #print(f" words found in the document")
if __name__ == "__main__":
    main()
