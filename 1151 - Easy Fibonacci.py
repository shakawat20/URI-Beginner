num =int(input())
i = 0
toe=[]
while i < num:
    if i == 0 or i == 1:
        toe.append(i)
    if i > 1:
        a = toe[i-2] +toe[i-1]
        toe.append(a)
    i = i + 1
for k in range(0, num):
    toe[k] =str(toe[k])
  
toe = ' '.join(toe)
print(toe)