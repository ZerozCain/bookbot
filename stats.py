def get_book_text(file_path):
    with open(file_path) as book:
        content = book.read()
        return content

def char_count(text):
    text = text.lower()
    char = {}
    for c in text:
        if c not in char:
            char[c] = 1
        else:
            char[c] += 1
    return char

def char_count_sort(char):
    char_list = []
    for c in char:
        char_list.append({f"{c}", char[c]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def sort_on(items):
    return items["num"]
