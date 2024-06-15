def calculate_sum(number):
    total = 0

    for num in number:
        total += num
        
    return total

print(calculate_sum([3, 3, 6, 73, 1]))