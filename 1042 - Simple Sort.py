num=list(map(int,input().split(" ")))
num3=num.copy()

for i in range(len(num)):

    op=num.pop(num.index(min(num)))

    print(op)
print()    
for j in num3:
    print(j)
