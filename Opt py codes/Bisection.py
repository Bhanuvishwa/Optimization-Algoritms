from scipy.misc import derivative
from math import sin, cos, tan, degrees,e


def f(x):
    return eval(equ_function)


def Bisection_Method_termination(upper, lower, E):
    (a, b) = (lower, upper)
    f_upper = derivative(f, b, dx=1e-6)  # dx is infinitesimal
    f_lower = derivative(f, a, dx=1e-6)
    if (f_upper > 0 and f_lower < 0):
        i = 1
        while (True):
            print('\n ### Iteration no. : ###',i)
            i += 1
            z = (a + b) / 2
            fz = derivative(f, z, dx=1e-6)
            print('value of z is: ',z)
            print('value of f`(z) is:',fz)
            if (abs(fz) < E):
                print('minimum is at: ',z)
                break
            elif (fz < 0):
                a = z
            elif (fz > 0):
                b = z
            print('minimum lies between (',a,b,')')
    else:
        print('Not possible')


def Bisection_Method_iteration(upper, lower, iterations):
    (a, b) = (lower, upper)
    f_upper = derivative(f, b, dx=1e-6)  
    f_lower = derivative(f, a, dx=1e-6)
    if (f_upper > 0 and f_lower < 0):
        for i in range(1, iterations + 1):
            print('\n ### Iteration no. : ###',i)
            z = (a + b) / 2
            fz = derivative(f, z, dx=1e-6)
            print('value of z is: ',z)
            print('value of f`(z) is:',fz)
            if (fz < 0):
                a = z
            elif (fz > 0):
                b = z
            print('minimum lies between (',a,b,')')
        print('After',i,'iterations the minimum lies at',(a+b)/2)
    else:
        print('Not possible')


equ_function = str(input("enter the function "))
lower = float(input('enter lower limit value'))
upper = float(input('enter upper limit value'))
choose = int(input('choose 1 option \n1) iterations method \n2) termination parameter'))
if choose == 1:
    iterations = int(input('enter the number of iterations'))
    Bisection_Method_iteration(lower=lower, upper=upper, iterations=iterations)
elif choose == 2:
    terminationparameter = float(input('enter the value of termination parameter'))
    Bisection_Method_termination(upper=upper, lower=lower, E=terminationparameter)
else:
    print('Invalid')