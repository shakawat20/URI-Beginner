num1=int(input())
num2=int(input())
sum=0
for n in range((num2+1),num1):
    if (n%2!=0):
        sum+=n
print(sum)