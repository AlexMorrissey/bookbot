from stats import get_num_words, get_num_letters, letters_sorted
import sys
print(sys.argv)


for arg in sys.argv:
    if arg == "main.py":
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    book_path = sys.argv
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    letters_sorted_list = letters_sorted(num_letters)
    print_report(book_path, num_words, letters_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, letters_sorted_list):
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for item in letters_sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"{item["letter"]}: {item["num"]}")

    print("========== END ==========")


if __name__ == "__main__":
    main()