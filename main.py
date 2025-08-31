from stats import get_word_count, character_stats, sort_character_stats

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    #Header
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------")
    #print number of words
    num_words = get_word_count(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print character dictionary
    for item in sort_character_stats(character_stats(book)):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()