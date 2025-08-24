def count_words(words):
    list = words.split();
    return len(list); 

def count_characters(text):
    characters_list = []
    count_characters = {}
    text = text.lower()

    for character in text:
        characters_list.append(character)
    
    for character in characters_list:
        if(character in count_characters):
            count_characters[character] += 1
        else:
            count_characters[character] = 1
    return count_characters

def sort_on(items):
    return items["num"];

def sort_list(dictionary):
    sorted_list = []
    for character in dictionary:
        char_dictionary = {}
        char_dictionary["char"] = character
        char_dictionary["num"] = dictionary[character]
        sorted_list.append(char_dictionary)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
