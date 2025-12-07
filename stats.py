def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters_dict(text):
    # convert the text to lowecase, also include space and symbol in the counts
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_dict_by_value(d):
    dict_list = []
    for key in d:
        dict_list.append({'char': key, 'num': d[key]})

    def sort_helper(e):
        return e['num']
    dict_list.sort(key=sort_helper, reverse=True)
    return dict_list
