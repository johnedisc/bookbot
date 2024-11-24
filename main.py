def count_word(text):
    text_array = text.split()
    return len(text_array)


def count_char(text):
    char_dict = {}
    for char in text:
        low_char = char.lower()
        if low_char.isalpha():
            if low_char in char_dict:
                char_dict[low_char] = (char_dict[low_char] + 1)
            else:
                char_dict[low_char] = 1
    return char_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_num = count_word(file_contents)
        char_num = count_char(file_contents)
        print(word_num)
        print(char_num)


main()
