num = int(input())
num2 = int(input())
tem = num
sum = 0
if(num > num2):
    num = num2
    num2 = tem
while(num <= num2):
    if(num%13 != 0):
        sum += num
    num += 1
print(sum)