import sys
from stats import count_words,count_characters,count_characters_ordered

def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    count = 0
    for x in sys.argv:
        count += 1
    if count == 2:
        print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
        count_characters_ordered(count_characters(get_book_text(sys.argv[1])))
    else:    
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
main()
