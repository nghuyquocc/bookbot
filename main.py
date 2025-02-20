def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words(file_contents)} words found in the document")

    char_list = [{"char": char, "count": count} for char,count in isalpha(char_count(file_contents)).items()]
    for char_data in char_list.sort(reverse=True, key=get_values):
        print(f"The character '{char_data["char"]}' was found {char_data["count"]} times")
    print("--- End report ---") 

def number_of_words(string):
    return len(string.split())

def isalpha(dict):
    new_dict = {}
    for key,value in dict.items():
        if key.isalpha():
            new_dict[key] = value
    return new_dict

def char_count(string):
    char_dict = {}
    for char in string.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_values(d):
    return d["count"]

main()