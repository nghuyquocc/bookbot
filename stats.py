def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(string):
    count = 0
    for item in string.split():
        count += 1

    return count

def count(string):
    from collections import Counter
    # dic = {}
    # for char in string.lower():
    #     dic[char] = dic.get(char, 0) + 1
    # return dic

    return dict(Counter(string.lower()))

def sort_on(string):
    sorted_dict = dict(sorted(count(string).items(), key=lambda item: item[1], reverse=True))
    for item in sorted_dict:
        if item.isalpha():
            print(f"{item}: {sorted_dict[item]}")
