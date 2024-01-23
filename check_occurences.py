def count_occurrence(text, t):
    txt = text.lower()
    chars = t.lower()
    if txt.count(chars) == 1:
        return f"'{t}' appeared once"
    elif txt.count(chars) == 2:
        return f"'{t}' appeared twice"
    else:
        return f"'{t}' appeared {txt.count(chars)} times"


print(count_occurrence("Hello, hello, hell Hello, hello, hell", "llo"))
print(count_occurrence("Python is greate, python is powerful", "Python"))
print(count_occurrence("1231236123123", "6"))
print(count_occurrence("The quick brown fox jumps over the lazy dog", "The"))
