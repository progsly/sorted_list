import sys


def is_digit(n):
    return n.lstrip("-").isdigit()


def process(input_list=None):

    if not input_list:
        return ""

    numbers = []
    words = []
    indexes = []
    for value in input_list:
        if is_digit(value):
            numbers.append(value)
            indexes.append(True)
        else:
            words.append(value)
            indexes.append(False)

    numbers.sort(key=int)
    words.sort()

    result = []
    for index in indexes:
        if index is True:
            result.append(numbers.pop(0))
        else:
            result.append(words.pop(0))

    return " ".join(result)

if __name__ == "__main__":
    input_list = sys.argv[1:]
    print process(input_list)
