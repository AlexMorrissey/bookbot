def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    letters = {}
    for letter in text:
        if not letter.isalpha():
            continue
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters

def sort_on(dict):
    return dict["num"]

def letters_sorted(num_letters_dict):
    letters_list = []
    for let in num_letters_dict:
        letters_list.append({"letter": let, "num": num_letters_dict[let]})
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list