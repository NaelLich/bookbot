from stats import get_num_words, get_chars_dict, count_alpha_characters
import sys

def main():
    if len(sys.argv) == 1:
        print("Please provide path to the book")
        sys.exit(1)
    book_path = "books/frankenstein.txt"
    text = open(sys.argv[1]).read()
    num_words = get_num_words(text)
    num_characters = get_chars_dict(text)
    alpha_characters = count_alpha_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in alpha_characters:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()  