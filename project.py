import numpy as np


def brent(f, a, b, tol=1e-10, maxiter=1000):
    """
    Brent's method for finding a root of a function f(x) between a and b.
    Returns the estimated root x and the number of iterations used.
    """
    # funkční hodnoty krajních bodů intervalu a středu
    fa = f(a)
    fb = f(b)
    c = a
    fc = fa
    d = np.nan
    s = np.nan
    mflag = True # boolovská hodnota, která mi řekne co jsem dělal naposled, true =secant bylo použito
    for i in range(maxiter):# za každou iteraci
        #interpolace k získání odhadovaného kořene "s"
        if fa != fc and fb != fc:
            s = (a*fb*fc)/((fa - fb)*(fa - fc)) + (b*fa*fc)/((fb - fa)*(fb - fc)) + (c*fa*fb)/((fc - fa)*(fc - fb))
        elif fb==fc:
            s=b-tol
        else:
            s = b - fb*(b - a)/(fb - fa)
        fs=f(s)
        if fs>0-tol and fs<0+tol:
            return s,i
        # podle zdálenosti odhadu od krajních bodu omezím interval 
        if ((s - b)*(s - c) > 0) or (abs(s - b) >= abs(c - b)/2):
            s = (a + b)/2
            mflag = True
        else:
            mflag = False
        fs = f(s)
        d = c
        c = b
        fc = fb
        if fa*fs < 0: # pokud je kořen blíž k té nižší hranici změníme b na s
            b=s
            fb=fs
        else: # pokud je kořen blíž k vyšší hranici změníme a na s
            a=s
            fa=fs
        if abs(fa) < abs(fb):
            a = b
            b = a
            fa= fb
            fb = fa
        if abs(fb) < tol:# pokud jsem v toleranci vrátím
            return b, i+1
        if mflag:
            continue
        # inversní kvadratická interpolace.
        if abs(b - c) > abs(c - d):
            s = (a + b)/2
        elif fb==fc:
            s=b-tol
        else:
            s = (b - fb*(b - c)/(fb - fc) or b)
            fs=f(s)
        if fs>0-tol and fs<0+tol:
            return s,i
        if ((s - b)*(s - c) > 0) or (abs(s - b) >= 0.5*abs(c - b)):
            s = (a + b)/2
        fs = f(s)
        d = c
        c = b
        fc = fb
        if fa*fs < 0:
            b, fb = s, fs
        else:
            a, fa = s, fs
        if abs(fb) < tol:
            return b, i+1
    raise RuntimeError("Prekrocen max pocet iteraci")

def my_ridder(f, a, b, tol=1e-10, maxiter=100):
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
    Errory:
    ValueError: v případě, že interval obsahuje více než jeden kořen
    RunntimeError: v případě že byl překročen maximální počet iterací
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
            return x, i+1
    raise RuntimeError("překročen počet iterací")

def my_bisection(f, a, b, tol):
    """
    Bisekční metoda pro hledání kořene na intervalu [a,b]
    Parametry:
    f: (function) Vstupní funkce jejíž kořeny hledáme
    a: (double) levé ohraničení intervalu
    b: (double) pravé ohraničení intervalu
    tol: (double) tolerovaná přestost řešení
    Return:
    Return (double) kořen funkce v intervalu
    Errory:
    ValueError: v případě, že interval obsahuje více než jeden kořen
    RunntimeError: v případě že byl překročen maximální počet iterací
    """
    while abs(f(a + (b - a) / 2)) > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def f1(x):
    return 3*x-1
def f2(x):
    return x**2
def f3(x):
    return x**2-1

#print(my_bisection(f1,-3,3,0.001))
# print(my_bisection(f2,-3,3,0.001))
# print(my_bisection(f3,-3,0,0.001))
# print(my_bisection(f3,0,3,0.001))
# print("result= " + (str)(my_ridder(f1,-5,5,0.0001,10000)))
# print("result= " + (str)(my_ridder(f1,-225,1,0.0001,10000)))
# print("result= " + (str)(my_ridder(f2,-23,998,0.0001,10000)))
print((str)(brent(f1,-1,1,0.001,100)))
print((str)(brent(f2,5,1,0.1,10000)))
print((str)(brent(f3,-2,0,0.00001,10000)))
