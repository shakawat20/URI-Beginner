def sum (a,b):
    if int(a)-int(b)<0:
        return -1*(int(a)-int(b))
    elif int(a)-int(b)>=0:

        return int(a)-int(b)
valor = input().split(" ")
a, b, c = valor
op =sum(int(a),int(b))
k=(int(a)+int(b)+op)/2
lp=sum(k,int(c))
result= (k +int(c)+lp)/2
print("{} eh o maior".format(int(result)))