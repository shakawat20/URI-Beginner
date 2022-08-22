num=int(input())

for i in range(6):
    if num%2==0:
        num=num+1
    if num%2!=0:
        print(num)
        num=num+2