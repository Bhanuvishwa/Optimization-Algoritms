from math import sin, cos, tan, degrees 

  

#Input: 

f_equation = str(input("enter the function")) 

lower = int(input('lower')) 

upper = int(input('upper')) 

n = int(input('no of intrevals')) 

  

def f(x): 

    if ('sin' or 'cos' or 'tan') in f_equation: 

        print("hi",x) 

        x = degrees(x) 

        print(x) 

    return (eval(f_equation)) 

delta = (upper-lower)/n 

print(delta) 

x1 = 0 

x2 = 0 

x3 = 0 

  

def Exhaustive_search_method(lower, delta): 

    x1 = lower 

    x2 = x1 + delta 

    x3 = x2 + delta 

    compute(x1,x2,x3) 

     

def compute(x1,x2,x3): 

    f_x1 = f(x1) 

    f_x2 = f(x2) 

    f_x3 = f(x3) 

    print("values of x1,x2,x3 currently:"+str(x1)+","+str(x2)+","+str(x3)) 

    print("values of f(x1),f(x2),f(x3) currently:"+str(f_x1)+","+str(f_x2)+","+str(f_x3)) 

     

    verification(x1, x2, x3, f_x1, f_x2, f_x3, delta) 

     

def verification(x1, x2, x3, f_x1, f_x2, f_x3, delta): 

    if(f_x1 >= f_x2 <= f_x3): 

        print("minimum intreval found:" "("+ str(x1) +"," + str(x3) + ")") 

    else: 

        p=x2 

        q=x3 

        r=q+delta 

        if(r <= upper): 

            print("## Next Iterarion ##") 

            compute(p, q, r) 

        else: 

            print("nominimum exists in ("+str(a)+","+str(b)+")") 

 
Exhaustive_search_method(lower, delta)    

 