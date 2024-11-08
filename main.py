def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(book_path)
    print(count)
    
    
    #gets the text from the book
def get_book_text(path):
    with open(path) as f:
        return f.read()
     
        
    #gets the word count from the book
def get_word_count(path):
    with open(path) as f:
        words = f.read()
        words_split = words.split()
        word_count = 0
        for word in range(len(words_split)):
            word_count += 1
    return word_count
            
    
main()