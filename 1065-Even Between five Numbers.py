list=[]
for i in range(5):
    num=int(input())
    if num %2==0:
        list.append(num)
print("{} valores pares".format(len(list)))