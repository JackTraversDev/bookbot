import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import *





def main():
    get_num_words()
    letterCount = character_number()
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    for letter in letterCount:
        print(f"{letter}: {letterCount[letter]}")

main()