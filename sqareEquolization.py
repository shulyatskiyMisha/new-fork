import math
while True:
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    c = int(input('enter c:'))
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b+math.sqrt(D))/(2*a)
        x2 = (-b-math.sqrt(D))/(2*a)
        print('x1 =',x1)
        print('x2 =',x2)
        print(D)
        print(x1+x2)
        print(x1*x2)
    else:
        print('D < 0')
