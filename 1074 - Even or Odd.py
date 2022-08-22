num = int(input())

for i in range(num):
    num1=int(input())
    if num1==0:
        print("NULL")
    elif num1 >0 and num1%2==0:
        print("EVEN POSITIVE")
    elif num1<0 and num1%2!=0:
        print("ODD NEGATIVE")
    elif num1>0 and num1%2!=0:
        print("ODD POSITIVE")
    elif num1 <0 and num1%2==0:
        print("EVEN NEGATIVE")    