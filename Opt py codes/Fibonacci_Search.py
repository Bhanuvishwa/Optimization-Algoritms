from math import sin, cos, tan, degrees


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def f(x):
    if ('sin' or 'cos' or 'tan') in equ_function:
        x = degrees(x)
    return (eval(equ_function))


def Fibonacci_Search_Method(lower, upper, m, k=2):
    L = upper - lower
    F = Fibonacci
    for i in range(m - 1):
        print('\n Iteration no:',i + 1,'-----------------------')
        k += 1
        lk = (F(m - k + 2 + 2) / F(m + 1 + 2)) * L

        x1 = lower + lk
        x2 = upper - lk
        print('values of x1,x2 are :',x1,x2)
        print('values of f(x1),f(x2) are:',f(x1) ,f(x2))
        if f(x1) > f(x2):
            lower = x1
            print('new intreval is: (',lower,upper,')')
        else:
            upper = x2
            print('new intreval is: (',lower,upper,')')
    print('---------------------------------')

equ_function = str(input("enter the function"))
lower = int(input('enter value of lower limit'))
upper = int(input('enter the value of upper limit'))
m = int(input('enter no. of function evaluations'))
Fibonacci_Search_Method(lower=lower, upper=upper, m=m)