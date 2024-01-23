# 1st way
def remove_first_last_char(text):
    if len(text) <= 2:
        return text
    new_text = ""
    for char in range(1, len(text) - 1):
        new_text += text[char]

    return new_text


print(remove_first_last_char("hello"))



# 2nd way
def remove_first_last_char(text):
    if len(text) <= 2:
        return text
    else:
        return text[1 : -1]


print(remove_first_last_char("morning"))
