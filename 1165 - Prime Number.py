num1=int(input())
for i in range(num1):
    
    num=int(input())
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("{} nao eh primo".format(num))
                break
    
        else:   
             print("{} eh primo".format(num))
        
    else:
        print("{} nao eh primo".format(num))
       