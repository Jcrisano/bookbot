"""
- Puts each word in from the text into a list (using .split() which will automatically use any whitespace as a delimeter)

- returns the length/count of the list
"""


def get_num_words(book_content):
    word_list = book_content.split()
    return len(word_list)