def text_reverse(text):
    reversed_text = ""

    for k in text:
        reversed_text = k + reversed_text
    return reversed_text

print(text_reverse("Python"))