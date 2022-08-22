num = False
while not num:
    X,Y = input().split()
    Y = int(Y)
    X = int(X)
    if X == 0 or Y == 0:
        num = True
    if X>0 and Y > 0 and not num:
         print('primeiro')
    elif X> 0 and Y < 0 and not num:
         print('quarto')
    elif X < 0 and Y< 0 and not num:
         print('terceiro')
    else:
        if not num:
            print('segundo')