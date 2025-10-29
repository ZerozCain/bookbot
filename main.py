from stats import get_book_text
from stats import char_count
from stats import char_count_sort


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(get_book_text('books/frankenstein.txt').split())} total words")
    print("-------- Character Count -------")
    for item in char_count_sort(char_count(get_book_text('books/frankenstein.txt'))):
        print(f"{item["char"]}: {item["num"]}")
    

main()