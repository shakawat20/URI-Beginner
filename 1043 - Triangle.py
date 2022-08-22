x,y,z=list(map(float,input().split(" ")))

if(x<y+z and y<x+z and z<x+z):
    
     print("Perimetro = {:.1f}".format(x+y+z))
     
else:
    
     print("Area = {:.1f}".format((z*(x+y))/2))