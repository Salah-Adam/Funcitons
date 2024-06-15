def calculateAverage(nums):
    sum = 0
    count = 0

    for num in nums:
        sum += int(num)
        count += 1

    average = sum / count
    return '{:.2f}'.format(average)

print(calculateAverage([1, 43, 53, 3, 5, 2]))
