from math import sin, cos, tan, degrees, e


def f(x):
    if ('sin' or 'cos' or 'tan') in equ_function:
        x = degrees(x)
    return (eval(equ_function))


def fx(w):
    x = w * (upper - lower) + lower
    return f(x)


def Golden_Section_Search(lower, upper, i):
    aw = (lower - lower) / (upper - lower)
    bw = (upper - lower) / (upper - lower)
    for iteration in range(i):
        print('\n \nIteration no:',iteration + 1,'\n')
        lw = bw - aw
        w1 = aw + (0.618) * lw
        w2 = bw - (0.618) * lw
        print('value of w1 and w2:',w1,w2)
        a = fx(w1)
        b = fx(w2)
        print('value of f(w1) and f(w2):',a,b)
        if a < b:
            (aw, bw) = (w2, bw)
        else:
            (aw, bw) = (aw, w1)
        print('The new interval is (',aw,bw,')')
        print('\n---------------------------------------------------')
        ax = (aw) * (upper - lower) + lower
        bx = (bw) * (upper - lower) + lower
        print('Minimum of the given function lies in',ax,bx)


equ_function = str(input('Enter the function '))
lower = float(input('lower '))
upper = float(input('upper '))

i = 0
while (True):
    s = (0.618 ** i) * (upper - lower)
    if s < 1:
        break
    i = i + 1
ans = input('Do you wand custom iterations?, \nDefault is i,type Y/N' )
if (ans == 'N' or ans == 'n'):
    i = int(input('Enter the number of iterations'))
Golden_Section_Search(lower=lower, upper=upper, i=i)