def count_word(text):
    text_array = text.split()
    return len(text_array)


def sort_by_num(dict):
    return dict['count']


def dict_to_list(dict):
    new_list = []
    for item in dict:
        temp_dict = {}
        temp_dict['char'] = item
        temp_dict['count'] = dict[item]
        new_list.append(temp_dict)
    new_list.sort(reverse=True, key=sort_by_num)
    return new_list


def count_char(text):
    char_dict = {}
    for char in text:
        low_char = char.lower()
        if low_char.isalpha():
            if low_char in char_dict:
                char_dict[low_char] = (char_dict[low_char] + 1)
            else:
                char_dict[low_char] = 1
    return dict_to_list(char_dict)


def print_report(num, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num} words found in the document")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_num = count_word(file_contents)
        char_list = count_char(file_contents)
        print_report(word_num, char_list)

main()

