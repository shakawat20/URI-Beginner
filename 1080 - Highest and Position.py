list=[]
for i in range(100):
    number=int(input())
    list.append(number)
number2=max(list)
print(number2)
print((list.index(number2))+1)
