import math

def SolveAxPlusB(a,b):
    print("x = -",b,"/",a)
    x = -b / a
    print("x =",x)

def SolveHypotenuse(a,b):
    print("c = sqrt(",a,"^2 + ",b,"^2)")
    x = math.hypot(a,b)
    print("c =",x)

