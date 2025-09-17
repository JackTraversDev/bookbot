import sys

def get_text():
    with open(sys.argv[1]) as f:
        return f.read()

def get_num_words():
    file_contents = get_text()
    split_contents = file_contents.split()
    return len(split_contents)

def character_number():
    letters = {}
    file_contents = get_text()
    letter_list = list(file_contents)
    for letter in letter_list:
        l = letter.lower()
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters
