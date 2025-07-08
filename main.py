from stats import get_num_words, char_count, sort_count, sort_on
import sys

def get_book_text(path):
    with open(path, 'r', encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

def main():
    # check to see if there are at least 2 arguments provided when program called
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        # if less than 2 arguments provided, program will terminate using sys.exit(1) indicating misc. error
        sys.exit(1)
        
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    word_count = get_num_words(content)
    character_count = char_count(content)
    sort_key = sort_count(content)
    sort_key.sort(key=sort_on, reverse=True)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_key:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    





main()