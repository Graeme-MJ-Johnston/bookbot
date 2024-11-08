def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    characters = characters_in_text(text)
    sorted_list = sort_character_number(characters)
    print(characters)
    
    
    #gets the text from the book
def get_book_text(path):
    with open(path) as f:
        return f.read()
     
        
    #gets the word count from the book
def get_word_count(text):
    words_split = text.split()
    return len(words_split)
            

def characters_in_text(text):
    character_number = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in character_number:
            character_number[lowered] += 1
        else:
            character_number[lowered] = 1
            
    return character_number
    
def sort_character_number(characters):
            
    
    
    return character_number
def report(book_path, count, characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print("")
    
    
main()