def factorial_pos_num(num):
    count = 1
    if str(num).isalpha():
        return "Enter an enteger"
    elif int(num) < 0:
        return  "enter a positive number"
    elif int(num) == 0:
        return count
    else:
        for i in range(int(num), 0, -1):
            count *= i
        return count
    
    
print(factorial_pos_num(5))