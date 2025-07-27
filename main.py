import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
#get_book_text retrieves the book
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents
from stats import word_count
from stats import character_count
from stats import sort_characters
#main function - currently uses the above two functions in order to print out how many words are in the book.
def main():
    book_contents = get_book_text(sys.argv[1])
    num_words = word_count(book_contents)
    num_letters = character_count(book_contents)
    character_list = sort_characters(num_letters)
    print (f"============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print (f"----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print (f"--------- Character Count -------")
    for char in character_list:
        char_string = char["char"]
        char_num = char["num"]
        if char_string.isalpha():
            print (f"{char_string}: {char_num}")
    print (f"============= END ===============")
main()