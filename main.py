from stats import get_book_text
from stats import char_count
from stats import char_count_sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {len(get_book_text(sys.argv[1]).split())} total words")
    print("-------- Character Count -------")
    for item in char_count_sort(char_count(get_book_text(sys.argv[1]))):
        print(f"{item["char"]}: {item["num"]}")
    

main()