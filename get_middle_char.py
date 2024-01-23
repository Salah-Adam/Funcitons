def get_middle_char(text):
    length = len(text)
    if length % 2 == 1:
        middle_char = text[length // 2]
        return middle_char

    else:
        middle_chars = text[length // 2 - 1 : length // 2 + 1]
        return middle_chars


print(get_middle_char("hello"))
print(get_middle_char("good"))
