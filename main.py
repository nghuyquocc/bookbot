from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    for pathfile in sys.argv[1:]:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {pathfile}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words(get_book_text(pathfile))} total words")
        print("--------- Character Count -------")
        sort_on(get_book_text(pathfile))
        print("============= END ===============")

    
main()