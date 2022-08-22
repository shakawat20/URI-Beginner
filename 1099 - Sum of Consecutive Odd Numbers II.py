num=int(input())
sum=0
while num>0:
    num1,num2=list(map(int,input().split()))
    for i in range (min(num1,num2)+1,max(num1,num2)):
        if i %2!=0:
            sum=sum +i
    print(sum)
    sum=0
    num=num-1