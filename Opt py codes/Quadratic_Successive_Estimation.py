from math import sin, cos, tan, degrees

def f(x):
    return eval(equ_function)

def Successive_Quad_Estimation_iteration(x1, d, iterations):
    i = 0
    f1 = f(x1)
    x2 = x1 + d
    f2 = f(x2)
    if f1 >= f2:
        x3 = x1 + (2 * d)
    else:
        x3 = x1 - d
    for i in range(1, iterations + 1):
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        print('\n ## Iteration no. :',i)
        Fmin = min(f1, f2, f3)

        if Fmin == f1:
            xmin = x1
        elif Fmin == f2:
            xmin = x2
        else:
            xmin = x3

        print('x1,x2,x3 values are:',x1,x2,x3)
        print('f1,f2,f3 values are:',f1,f2,f3)
        print('Fmin value is: ',Fmin)
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * (((f3 - f1) / (x3 - x1)) - a1)

        # print(type(a1), type(a2))
        print('a1,a2 values:',a1,a2)
        x_a = ((x1 + x2) / 2) - (a1 / (2 * a2))

        print('x bar value is:',x_a)
        print('f(x bar) value:',f(x_a))

        val = list((x1, x2, x3, x_a))
        val.sort()
        (_, x1, x2, x3) = val
    print('minimum after',i,'iterations is at',x_a)


def Successive_Quad_Estimation_terminate(x1, d, E):
    i = 0
    f1 = f(x1)
    x2 = x1 + d
    f2 = f(x2)
    if f1 >= f2:
        x3 = x1 + (2 * d)
    else:
        x3 = x1 - d
    while (True):
        i += 1
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        print('\niteration no.:',i)
        Fmin = min(f1, f2, f3)
        print('Fmin value:',Fmin)
        if Fmin == f1:
            xmin = x1
        elif Fmin == f2:
            xmin = x2
        else:
            xmin = x3

        print('x1,x2,x3 values:',x1,x2,x3)
        print('f1,f2,f3 values:',f1,f2,f3)

        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * (((f3 - f1) / (x3 - x1)) - a1)

        # print(type(a1), type(a2))
        print('a1,a2 values :',a1,a2)
        xbar = ((x1 + x2) / 2) - (a1 / (2 * a2))

        print('xbar value:',xbar)

        fxbar = f(xbar)
        print('f(xbar) value:',fxbar)

        diff_Fmin_fxbar = abs(Fmin - fxbar)
        diff_xmin_xbar = abs(xmin - xbar)

        if (diff_Fmin_fxbar < E and diff_xmin_xbar < E):
            print('x=',xmin,'is the minimum point')
            break
        else:
            val = list((x1, x2, x3, xbar))
            val.sort()
            (_, x1, x2, x3) = val
            # print(val)
            print('The Best 3 points are:',x1,x2,x3)


equ_function = str(input("enter the function: "))
x1 = float(input('enter the value of x1'))
d = float(input('enter value of delta'))
choose = int(input('choose any 1 option \n1) result after n iterations \n2) continue till termination'))
if choose == 1:
    iterations = int(input('enter no. of iterations'))
    Successive_Quad_Estimation_iteration(x1=x1, d=d, iterations=iterations)

elif choose == 2:
    termparameter = float(input('enter the termination parameter'))
    Successive_Quad_Estimation_terminate(x1=x1, d=d, E=termparameter)

else:
    print('Invalid')
