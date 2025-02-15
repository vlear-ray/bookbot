def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    character_counts = count_characters(file_contents.lower())
    #print(f"{num_words} found in the document.")
    print_report(character_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text_string):
    counts = {}
    for character in text_string:
        if character in counts:
            counts[character]+=1
        else:
            counts[character] = 1
    return counts

def sort_on(item):
    return item["num"]

def print_report(counts):
    list_counts = [{'char': k, 'num': v} for k, v in counts.items() if k.isalpha()]
    list_counts.sort(reverse=True, key=sort_on)
    for item in list_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")
    return None

if __name__ == "__main__":
    main()