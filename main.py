import sys
from stats import get_num_words, get_num_characters_dict, sort_dict_by_value


def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    char_dict = get_num_characters_dict(book_text)
    sorted_dict_list = sort_dict_by_value(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for dict in sorted_dict_list:
        if dict['char'].isalpha():
            print(f'{dict["char"]}: {dict["num"]}')
    print("============= END ===============")


if __name__ == '__main__':
    main()
