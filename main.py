from stats import get_num_words, char_count, sort_count, sort_on


def get_book_text(path):
    with open(path, 'r', encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

book_path = "books/frankenstein.txt"

def main():
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