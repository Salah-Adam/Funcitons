def count_latters_digits_symbols(text):
    char = ""
    digits = ""
    symbol = ""
    for t in text:
        if t.isalpha():
            char += t
        elif t.isdigit():
            digits += t
        else:
            symbol += t
    return f"Chars = {len(char)}, Digits = {len(digits)}, Symbols = {len(symbol)}"


print(count_latters_digits_symbols("1A@2B#3"))