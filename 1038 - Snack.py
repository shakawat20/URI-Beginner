op=[4.00,4.50,5.00,2.00,1.50]
var1,var2=list(map(int,input().split()))
print("Total: R$ {:.2f}".format(op[var1-1]*var2))
