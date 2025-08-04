from stats import count_words, sort_ch_counts
from stats import character_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        read_data = f.read()
        return read_data


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1] 
    document = get_book_text(filepath)
    character_counts = character_count(document)
    count_words(document)
    sorted_list = sort_ch_counts(character_counts)

    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

main()
