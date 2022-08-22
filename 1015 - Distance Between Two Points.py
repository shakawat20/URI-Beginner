import math
op =list(map(float,input().split(" ")))
op1=list(map(float,input().split(" ")))

result=((op1[0]-op[0])**2 +(op1[1]-op[1])**2)
print("{0:.4f}".format(math.sqrt(result)))