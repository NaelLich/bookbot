def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    characters_dict = {}
    for character in text.lower():
        if not character in characters_dict:
            characters_dict[character] = 1
        else:
            characters_dict[character] += 1
    return characters_dict

def sort_on(dict):
    return dict["num"]


def count_alpha_characters(text):
    characters_dict = get_chars_dict(text)
    characters_list = []
    for char, count in characters_dict.items():
        if char.isalpha():
            temps_dic = {"char": char, "num": count}
            characters_list.append(temps_dic)
    characters_list.sort(reverse = True, key=sort_on)
    return characters_list


