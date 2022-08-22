min=input().split(" ")
op=(int(min[2])*60+int(min[3]))-(int(min[0])*60+int(min[1]))
if op <=0:
    op+=60*24

koo=op//60
mino=op%60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(koo,mino))