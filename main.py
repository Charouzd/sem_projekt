import time as t
import numpy as np
import matplotlib.pyplot as plt
import myImplementations as MI
import pipColection as PC

def average_time_of_10(method,f,min,max,expected_result,tol):
    """
    funkce změří průměrný čas jedné analitické funkce na 10 měřeních

    Args:
        method (function): funkce na zjištění kořenu
        f (function): prohledávaná funkce
        min (float): dolní limit intervalu
        max (float): horní limit intervalu
        expected_result (float): očekávaný výsledek
        tol (int): tolerance výsledku

    Returns:
        _float_: _description_
    """
    t_total=0
    for i in range(10):
        t1=t.time()
        t.sleep(1)
        res=method(f,min,max)
        t2=t.time()
        if res<=expected_result+tol and res>expected_result-tol:
            t_total+= t2-t1-1
    return t_total/10  
## Funkce pro testovní
def linear(x): return 2*x+3 #Lineární funkce s 1 kořenem
def parabola(x): return 1-x**2 # Parabolická funkce s 2 kořeny
def oscilace(x): return np.sin(x)*np.cos(x) # Funkce periodická s opakujícím se kořenem násobkem kořenu
def odd_polynom(x): return ((2*(x**5))+((x**4)) -(x**3) -(2*(x**2)) -(3*x))# Lichý polynom 5stupně
def unstable(x): return( (x/10)**3 + np.sin(5*x))# Kmitající funkce 

## Hodnty pro plotování
# values_for_linear=np.linspace(-3,3,109)
# values_for_parabola=np.linspace(-3,3,109)
# values_for_oscilace=np.linspace(-0.5,4,109)
#values_for_odd_polynom=np.linspace(-1.5,1.5,109)
#values_for_unstable=np.linspace(-10,10,109)

##Lineární funkce
# plt.figure(0)
# plt.plot(values_for_linear,linear(values_for_linear))
# plt.axhline(y=0, color='r')
# plt.axvline(x=0, color='g')

## kvadratická funkce print
# plt.figure(2) 
# plt.plot(values_for_parabola,parabola(values_for_parabola))
# plt.axhline(y=0, color='r')  
# plt.axvline(x=0, color='g')

## Oscilující funkce 
# plt.figure(3) 
# plt.plot(values_for_oscilace,oscilace(values_for_oscilace))
# plt.axhline(y=0, color='r')  
# plt.axvline(x=0, color='g')

## Lichý polynom
# plt.figure(4)
# plt.plot(values_for_odd_polynom,odd_polynom(values_for_odd_polynom))
# plt.axhline(y=0, color='r')
# plt.axvline(x=0, color='g')

## Kmitají funkce
# plt.figure(5)
# plt.plot(values_for_unstable,unstable(values_for_unstable))
# plt.axhline(y=0, color='r')  
# plt.axvline(x=0, color='g')

#def fce_s_rychlym_prechodem(x):
#    if x < -1:
#        return -5
#    elif x > 1:
#        return 5
#    else:
#       return 5*np.sin(1.5*x)
#def exponencialni_funkce(x):
#    return(math.exp(x))
#def fce_konstantni(x):
#    return 1
## Displaying the plot
# plt.show()

## printing results
## Lineární funkce
# print((str)(PC.scipy_brentq(linear,-5,1)))
# print((str)(MI.brents(linear,-2,0.5,0.00001,10000)[0]))
# print((str)(PC.scipy_brentq(linear,-5,1)))
# print((str)(MI.brents(linear,-2,0.5,0.00001,10000)[0]))

## brentova metoda
min=-3
max=0.05
funkce=parabola
res1=PC.scipy_brentq(funkce,min,max)
res2=PC.pyroot_brent(funkce,min,max)
res3=MI.my_brents(funkce,min,max,0.00001,10000)
t1=average_time_of_10(PC.scipy_brentq,funkce,min,max,-1.0,1e-6)
t2=average_time_of_10(PC.pyroot_brent,funkce,min,max,-1.0,1e-6)
t3=average_time_of_10(MI.my_brents,funkce,min,max,-1.0,1e-6)
print("Výsledek scipy pomocí brentq(): "+(str)(res1)+" v čase "+(str)(t1))
print("Výsledek pyroot pomocí brent(): "+(str)(res2)+" v čase "+(str)(t2))
print("Výsledek vlastní implementace pomocí my_brents(): "+(str)(res3)+" v čase "+(str)(t3))

