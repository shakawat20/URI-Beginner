num= int(input())
for i in range(num):
    num1=int(input())
    sum1=0

    for j in range(1,num1):
        if num1%j==0:

            sum1=sum1+j


    if sum1 == num1:
        print("{} eh perfeito".format(num1))
    else:
        print("{} nao eh perfeito".format(num1))
