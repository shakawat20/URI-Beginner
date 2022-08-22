op =int(input())
num=op//3600
num1=op%3600
num2=num1//60
num3=num1%60
print("{}:{}:{}".format(num,num2,num3))