while 1:
    try:
        num1,num2=list(map(int,input().split()))
        if num2 == num1:
            break
        if num1 - num2 > 0:
            print("Decrescente")
        elif num1 - num2 < 0:
            print("Crescente")
    except EOFError:
        break
