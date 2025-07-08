"""
- Puts each word in from the text into a list (using .split() which will automatically use any whitespace as a delimeter)

- returns the length/count of the list
"""
def get_num_words(book_content):
    word_list = book_content.split()
    return len(word_list)


"""
counts how many times each character is used in the text and returns dictionary
"""
def char_count(book_content):
    character_count_dict = {}
    word_list = book_content.lower().split()
    for word in word_list:
        for letter in word:
            if letter in character_count_dict:
                character_count_dict[letter] += 1
            else:
                character_count_dict[letter] = 1
    return character_count_dict

def sort_on(items):
    return items["num"]

def sort_count(book_content):
    items = []
    character_count_dict = char_count(book_content)
    for character in character_count_dict:
        items.append({"char": character, "num": character_count_dict[character]})
    return items


