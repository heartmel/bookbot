from stats import count_words, count_characters, sort_list
import sys 

def get_book_text(path):

    with open(path) as f:
        file_contents = f.read();
    return file_contents;

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1);
    filepath = sys.argv[1];
    content = get_book_text(filepath);
    result_words = count_words(content);
    result_character = count_characters(content);
    sorted_list = sort_list(result_character)
    #print(f"{resultwords} words found in the document")
    #print (resultcharacter)
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {filepath}\n"
          "----------- Word Count ----------\n"
          f"Found {result_words} total words\n"
          "--------- Character Count -------")
    for character in sorted_list:
        if(character["char"].isalpha()):
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main();