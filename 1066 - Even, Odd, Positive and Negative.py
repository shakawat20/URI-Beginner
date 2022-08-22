ev=0
od=0
pos=0
neg=0
for l in range(1,6):
    n = float(input())
    if(n % 2 == 0):
         ev = ev+1
    else:
        od=od+1
    if (n > 0):
        pos=pos+1
    elif (n < 0):
        neg=neg+1
print("{} valor(es) par(es)".format(ev))
print("{} valor(es) impar(es)".format(od))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))