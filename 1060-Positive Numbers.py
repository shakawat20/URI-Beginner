num1=[ ]
for i in range(6):
    num=float(input())
    if num<=0:
        continue
    else:
        num1.append(num)



print(len(num1),"valores positivos")
