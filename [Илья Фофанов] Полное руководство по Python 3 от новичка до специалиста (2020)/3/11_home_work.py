import random

sum = random.randint(1, 50)
x = 0
while x < 6:
    x += 1
    num1 = int(input('enter the number'))
    if num1 == sum:
        print(f"success! value {num1} is equal sum")
        break
    if num1 < sum:
        print(f"value {num1} is less than sum")
    else:
        print(f"value {num1} is more than sum")
