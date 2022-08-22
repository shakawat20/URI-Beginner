num=int(input())
for i in range(num):
    num1,num2=list(map(float,input().split()))
    if num2!=0:
        print("{}".format(num1 / num2))

    else:
        print("divisao impossivel")