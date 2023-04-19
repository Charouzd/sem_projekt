import numpy as np

def my_brents(f, a, b, tolerance=1e-6, maxiter=1000):
    """
    brentova metoda pro hledání kořene na intervalu [a,b]
    Parametry:
    f: (function) Vstupní funkce jejíž kořeny hledáme
    a: (double) levé ohraničení intervalu
    b: (double) pravé ohraničení intervalu
    tol: (double) tolerovaná přestost řešení
    maxiter: (int) maximální počet iterací
    Return:
    Return (tuple)(double,int) kořen funkce a počet iterací potřebných k nalezení řešení
    """
    fx0 = f(a)
    fx1 = f(b)

    
    if abs(fx0) < abs(fx1):
        a, b = b, a
        fx0, fx1 = fx1, fx0

    x2, fx2 = a, fx0
    d=x2
    mflag = True
    step = 0
    ttol=abs(b-a)
    while step < maxiter and abs(b-a) > tolerance:
        fx0 = f(a)
        fx1 = f(b)
        fx2 = f(x2)

        if fx0 != fx2 and fx1 != fx2:
            L0 = (a * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
            L1 = (b * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
            L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
            new = L0 + L1 + L2
        else:
            new = b - ( (fx1 * (b - a)) / (fx1 - fx0) )

        if ((new < ((3 * a + b) / 4) or new > b) or
            (mflag == True and (abs(new - b)) >= (abs(b - x2) / 2)) or
            (mflag == False and (abs(new - b)) >= (abs(x2 - d) / 2)) or
            (mflag == True and (abs(b - x2)) < tolerance) or
            (mflag == False and (abs(x2 - d)) < tolerance)):
            new = (a + b) / 2
            mflag = True
        else:
            mflag = False

        fnew = f(new)
        d, x2 = x2, b

        if (fx0 * fnew) < 0:
            b = new
        else:
            a = new

        if abs(fx0) < abs(fx1):
            a, b = b, a

        step += 1
        ttol=abs(b-a)
    # if step>=maxiter:
    #     raise()
    return b
def my_ridder(f, a, b, tol=1e-6, maxiter=1000):
    """
    Reidderova metoda pro hledání kořene na intervalu [a,b]
    Parametry:
    f: (function) Vstupní funkce jejíž kořeny hledáme
    a: (double) levé ohraničení intervalu
    b: (double) pravé ohraničení intervalu
    tol: (double) tolerovaná přestost řešení
    maxiter: (int) maximální počet iterací
    Return:
    Return (tuple)(double,int) kořen funkce a počet iterací potřebných k nalezení řešení
    """
    #funčí hodnota v krajíních bodech intervalu
    fa = f(a) 
    fb = f(b)
    # if fa*fb >= 0:# kořen není v intervalu nebo interval je příliš velký
    #     raise ValueError("vybraný interval je příliš rozsáhlý")
    x = np.nan
    for i in range(maxiter):# za počet iterací
        #půlení intervalu
        c = (a + b)/2
        fc = f(c)#funkční hodnota cetrálního bodu
        if fc <0+tol and fc>0-tol:
            return c, i+1
        #interpolační část
        
        s = np.sqrt(abs(fc**2 - fa*fb))
        if s == 0:
            return x, i+1
        dx = (c - a)*fc/s
        if (fa - fb) < 0:
            dx = -dx
        u = c + dx
        fu = f(u)#nová hraniční hodnota
        # pzůžení intervalu
        if (fu*fc) > 0:
            a, fa = c, fc
            b, fb = u, fu
        elif (fu*fa) > 0:
            b, fb = u, fu
        elif (fu*fb) > 0:
            a, fa = u, fu
        else:
            x = u
            return x, i+1
        if abs(b-a) < tol*(abs(b)+abs(a)):
            x = (a + b)/2
            return x
    #raise RuntimeError("překročen počet iterací")

def my_bisection(f, a, b, tol=1000):
    """
    Bisekční metoda pro hledání kořene na intervalu [a,b]
    Parametry:
    f: (function) Vstupní funkce jejíž kořeny hledáme
    a: (double) levé ohraničení intervalu
    b: (double) pravé ohraničení intervalu
    tol: (double) tolerovaná přestost řešení
    Return:
    Return (double) kořen funkce v intervalu
    """
    while abs(f(a + (b - a) / 2)) > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
## testovací a ladící příklady
# def f1(x):
#     return 3*x-1
# def f2(x):
#     return x**2
# def f3(x):
#     return x**2-1
# val=np.linspace(-5,5,110)
#print(my_bisection(f1,-3,3,0.001))
# print(my_bisection(f2,-3,3,0.001))
# print(my_bisection(f3,-3,0,0.001))
# print(my_bisection(f3,0,3,0.001))
# print("result= " + (str)(my_ridder(f1,-5,5,0.0001,10000)))
# print("result= " + (str)(my_ridder(f1,-225,1,0.0001,10000)))
# print("result= " + (str)(my_ridder(f2,-23,998,0.0001,10000)))
#print((str)(brents(f1,-1,1,0.001,100)))
# pic=plt.plot(val,f3(val))
# plt.axhline(y=0, color='b')
# plt.axvline(x=0, color='b')
# plt.show()
#print((str)(brents(f2,-5,1,0.001,10000)))
#print((str)(brents(f3,-2,0,0.00001,10000)))
# print((str)(brents(f3,0.5,2,0.00001,10000)))