op=float(input())

if op <0:
    print("Fora de intervalo")
elif op<=25 and op>=0:
    print("Intervalo [0,25]")
elif op>25 and op <=50:
    print("Intervalo (25,50]")
elif op>50 and op <=75:
    print("Intervalo (50,75]")
elif op >75 and op<=100:
    print("Intervalo (75,100]")
elif op>100:
    print("Fora de intervalo")