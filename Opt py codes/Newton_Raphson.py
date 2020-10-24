from scipy.misc import derivative
from math import sin, cos, tan, degrees, e


def f(x):
    return eval(equ_function)


def Newton_Raphson_Method(x0, tp):
    i = 0
    while (True):
        i += 1
        if (x0 < -0.01 or x0 > 0.01):
            dx = 0.01
        elif (-0.01 < x0 < 0.01):
            dx = 0.0001
        print('###', i ,'###')
        f_d1 = derivative(f, x0, dx=dx)
        f_d2 = derivative(f, x0, dx=dx, n=2)
        print('f`=',f_d1,'f``=',f_d2)
        x0 = x0 - (f_d1 / f_d2)
        f_d1 = derivative(f, x0, dx=dx)
        print('f`(x(',i,')) =', f_d1)
        if (abs(f_d1) > tp):
            pass
        else:
            break
    print('minimum lies at:',x0)


equ_function = str(input("enter the function: "))
x0 = float(input('enter the value of x0'))
tp = float(input('enter the termination parameter'))
Newton_Raphson_Method(x0, tp)