import sys
from stats import get_num_words, count_chars, sorted_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = count_chars(text)
    chars_sorted = sorted_chars(text)
    for char, count in chars_sorted:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()