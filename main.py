#get_book_text retrieves the book
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents
from stats import word_count
from stats import character_count
#main function - currently uses the above two functions in order to print out how many words are in the book.
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_contents)
    num_letters = character_count(book_contents)
    print (f"{num_words} words found in the document")
    print (num_letters)
main()