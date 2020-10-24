from math import sin, cos, tan, degrees 

  

#Input: 

  

f_equation = str(input("enter the function")) 

lower = int(input('lower')) 

upper = int(input('upper')) 

E = float(input('enter the minimum accuracy value')) 

  

def f(x): 

    if ('sin' or 'cos' or 'tan') in f_equation: 

        print("hi",x) 

        x = degrees(x) 

        print(x) 

    return (eval(f_equation)) 

  

def Interval_halving_method(lower, upper): 

    L = (upper-lower) 

    x1 = lower + L/4 

    x2 = upper - L/4 

    x_m = (lower + upper)/2 

     

    f_x1 = f(x1) 

    f_x2 = f(x2) 

    f_xm = f(x_m) 

    print("values of x1,x2,x(m) currently:"+str(x1)+","+str(x2)+","+str(x_m)) 

    print("values of f(x1),f(x2),f(x(m)) currently:"+str(f_x1)+","+str(f_x2)+","+str(f_xm)) 

     

    verification(x1, x2, x_m, f_x1, f_x2, f_xm, lower, upper) 

     

def verification(x1, x2, x_m, f_x1, f_x2, f_xm, lower, upper): 

    if(f_x1 < f_xm): 

        p = lower 

        q = x_m 

    elif(f_x2 < f_xm): 

        p = x_m 

        q = upper 

    else: 

        p = x1 

        q = x2 

    L = q - p 

    if(abs(L) < E): 

        print("nominimum exists in ("+str(p)+","+str(q)+")") 

    else: 

        Interval_halving_method(p, q) 

  

Interval_halving_method(lower, upper)     

 