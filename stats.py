def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characters_dict = {}
    for character in text.lower():
        if not character in characters_dict:
            characters_dict[character] = 0
        if character in characters_dict:
            characters_dict[character] += 1
    return characters_dict


def count_alphabet(text):
    characters_dict = count_characters(text)
    print(characters_dict.items())