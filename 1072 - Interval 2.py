num = int(input())
count = 0
count2 = 0
while num > 0:
    num1 = int(input())
    if num1 >= 10 and num1 <= 20:
        count = count + 1

    elif num1 < 10 or num1 > 20:
        count2 = count2 + 1
    num = num - 1

print("{} in".format(count))
print("{} out".format(count2))