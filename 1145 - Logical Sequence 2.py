num1,num2 = list(map(int,input().split()))
cont = 1
for i in range(1,(int((num2/num1))+1)):
    op = ""
    for y in range(num1):
        op += str(cont) + " "
        cont += 1
    print(op[:-1])