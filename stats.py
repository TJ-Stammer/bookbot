def get_word_count(book):
    words = book.split()
    return len(words)

def character_stats(book):
    letter_dict = {}
    for char in book:
        if char.lower() in letter_dict:
            letter_dict[char.lower()] += 1
        else:
            letter_dict[char.lower()] = 1
    return letter_dict

def sort_on(items):
    return items["num"]

def sort_character_stats(letter_dict):
    dict_list = []
    for key, value in letter_dict.items():
        dict_list.append({"char":key,"num":value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
