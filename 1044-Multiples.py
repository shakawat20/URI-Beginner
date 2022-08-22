num1,num2=list(map(int,input().split()))

if num2%num1==0 or num1%num2==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")