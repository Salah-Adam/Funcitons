def vowel_count(text):

    vowels = "aeiou"
    count = 0

    for c in text:
        if c.lower() in vowels:
            count = count + 1
            
    return count

print(vowel_count("GOOD morning"))