def add_ing_ly(text):
    if len(text) < 3:
        return text
    if text.endswith("ing"):
        return text + "ly"
    else:
        return text + "ing"

print(add_ing_ly("king"))
print(add_ing_ly("ok"))
print(add_ing_ly("try"))




