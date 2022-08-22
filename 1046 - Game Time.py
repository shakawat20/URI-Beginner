num1,num2=list(map(int,input().split(" ")))
if num1>12:
   num3=24-num1+num2
 
if num1<12:
    num3=num2-num1

if num1==num2:
    num3=num1-num2+24
print("O JOGO DUROU {} HORA(S)".format(num3))