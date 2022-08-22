num1=int(input())
sum=0
for i  in range(num1):
    num2,num3=list(map(int,input().split(" ")))
    if num2%2==0:
        num2=num2+1
    for j in range(num3):
        sum=sum +num2
        num2 = num2 + 2
    print(sum)
    sum=0