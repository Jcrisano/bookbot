def get_book_text(path):
    with open(path, 'r', encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

def count_words(book_content):
    word_list = book_content.split()
    return len(word_list)


def main():
    content = get_book_text("books/frankenstein.txt")
    word_count = count_words(content)
    print(f"{word_count} words found in the document")

main()