def remove_Emptystring(string):

    filtered_string = []

    for sentence in string:
       if sentence.strip() !="":
           filtered_string.append(sentence)
    return filtered_string

print(remove_Emptystring(["Hello", "", "World", "    ", "Python"]))