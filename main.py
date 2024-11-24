def count(text):
    text_array = text.split()
    return len(text_array)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number = count(file_contents)
        print(number)


main()
