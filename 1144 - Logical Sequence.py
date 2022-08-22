num=int(input())
for i in range(1,num+1):
    x=i*i
    y=i*i*i
    print("{} {} {}".format(i,x,y))
    print("{} {} {}".format(i,x+1,y+1))