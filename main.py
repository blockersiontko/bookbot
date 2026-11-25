import sys
from stats import get_num_words, get_letter_count, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def print_report(file_path: str, word_count: str, sorted_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")

    for letter, count in sorted_list:
        
        if letter.isalpha():
            print(f'{letter}: {count}')

    print("============= END ===============")

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

FILE_PATH = sys.argv[1]

book_text = get_book_text(FILE_PATH)
num_words = get_num_words(book_text)
let_count = get_letter_count(book_text)
sor_list = chars_dict_to_sorted_list(let_count)

print_report(FILE_PATH, num_words, sor_list)