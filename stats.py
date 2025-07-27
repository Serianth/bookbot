#word_count splits the book into words and then counts the length of the words
def word_count(file_contents):
    words = file_contents.split()
    return len(words)
def character_count(file_contents):
    letters ={}
    for letter in file_contents:
        stored_letters = letter.lower()
        if stored_letters in letters:
            letters[stored_letters] += 1
        else:
            letters[stored_letters] = 1
    return letters
def sort_on(items):
    return items["num"]
    
def sort_characters(character_count):
    characters = []
    for char_name, num_count in character_count.items():
        char_dict = {"char": char_name, "num": num_count}
        characters.append(char_dict)
    characters.sort(reverse=True, key=sort_on)
    return characters