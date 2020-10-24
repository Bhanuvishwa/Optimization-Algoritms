from math import sin, cos, tan, degrees 

  

#Input 

  

f_equation = str(input("enter the function")) 

x = int(input("enter the intial value")) 

d = float(input("enter the value of delta")) 

  

def f(x): 

    if ('sin' or 'cos' or 'tan') in f_equation: 

        print("hi",x) 

        x = degrees(x) 

        print(x) 

    return (eval(f_equation)) 

     

def Bounding_phase(x,d): 

    l1=[] 

    a = f(x - abs(d)) 

    b = f(x) 

    c = f(x + abs(d)) 

     

    if(a >= b >= c): 

        d= abs(d) 

    elif(a <= b <= c): 

        d= -1*d 

    else: 

        print("minimum lies in :",x-abs(d),x+abs(s)) 

    print(d) 

    i=0 

    l1.append(x) 

    while(True): 

        x = x 

        x1 = x + pow(2,i)*d 

        print("x1 is:"+str(x1)) 

        l1.append(x1) 

        if(f(x1) < f(x)): 

            x = x1 

        elif(f(x1) > f(x)): 

            k = x1 

            j = l1[i-1] 

            print("minimum lies in:"+str(j)+","+str(k)) 

            break 

        i+=1 

         

Bounding_phase(x,d) 