from stats import get_num_words, char_count


def get_book_text(path):
    with open(path, 'r', encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

def main():
    content = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(content)
    character_count = char_count(content)
    print(f"{word_count} words found in the document")
    print(character_count)



main()