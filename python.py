
"""
    Program testuje rychlost a efektivitu implementovaných funkcí

    Použité knihovny: Scipy, Pyroots, Rootfinging, numpy, Root-solver, Root-Calculator

    pip install pyroots
    pip install scipy
    pip install numpy
    pip install matplotlib
    pip install rootfinding
    pip install root-calculator

    Výsledek: formátovaný výpis časů potřebných k výpočtu

"""
import time as t
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as SP
import rootfinding as RF
import pyroots as PR
import root_solver as RS
# import  root_calculator - není implemontován,existuje pouze dokumentace
# rozsah funkce
wait_time=3
val=np.linspace(-10,10,109)
def linear(x): return 2*x+3 #Lineární funkce s 1 kořenem
def parabola(x): return 1-x**2 # Parabolická funkce s 2 kořeny
def oscilace(x): return np.sin(x)*np.cos(x) # Funkce periodická s opakujícím se kořenem násobkem kořenu
def odd_polynom(x): return ((2*(x**5))+((x**4)) -(x**3) -(2*(x**2)) -(3*x))# Lichý polynom 5stupně
def even_polynom(x): return (2*(x**4)+(x**3)-2*(x**2)-(x))# Sudý polynom 4.stupně
def unstable(x): return( (x/10)**3 + np.sin(5*x))# Kmitající funkce 

    # Kód určený pro visualizaci funkcí
    # Returns: plot.svg
#%%
plt.figure(0)
plt.plot(val,linear(val))
plt.figure(1)
plt.plot(val,parabola(val)) 
plt.figure(2) 
plt.plot(val,oscilace(val))
plt.figure(3)
plt.plot(val,odd_polynom(val))
plt.figure(4)
plt.plot(val,even_polynom(val))
plt.figure(5)
plt.plot(val,unstable(val))
#%%
#SCIPY METODY
def scipy_fsolve(fce):
    """
    Funkce z knivny scipy
    funguje na principu jacobiho iterace a derivace
    Nejsou zde omezení

    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny=SP.fsolve(fce,[-10,10])
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
def scipy_brentq(fce):
    """
    Funkce z knivny scipy
    funguje na principu kombinace bisekce secans metody
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen

    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny=SP.brentq(fce,-10,10)
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
def scipy_riderfce(fce):
    """
    Funkce z knivny scipy
    funguje na principu aproximace funkce exponencielou
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny=SP.ridder(fce,-10,10)
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
def scipy_newton(fce):
    """
    Funkce z knivny scipy
    funguje na principu derivace
    Omezení žádné není
    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny=SP.newton(fce,[-10,10])
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
def scipy_bisect(fce):
    """
    Funkce z knivny scipy
    funguje na principu aproximace funkce exponencielou
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen

    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny=SP.bisect(fce,-10,10)
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
#PYROOT METODY
def pyroot_brent(fce):
    """
    Funkce z knivny pyroot
    funguje jedá se o téměř stejnou implementaci jako ve knihovně scipy
    je samostatná => menší náročnost na paměť
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    start_time=t.time()
    t.sleep(wait_time)
    solver = PR.Brentq()
    try:
        koreny = solver(fce, -10, 10).x0
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
def pyroot_bisec(fce):
    """
    Funkce z knivny pyroot
    funguje jedá se o téměř stejnou implementaci jako ve knihovně scipy, ale je samostatná => menší náročnost na paměť
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    start_time=t.time()
    t.sleep(wait_time)
    solver = PR.Bisect()
    try:
        koreny = solver(fce, -10, 10).x0
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
def pyroot_ridder(fce):
    """
    Funkce z knivny pyroot
    funguje jedá se o téměř stejnou implementaci jako ve knihovně scipy, ale je samostatná => menší náročnost na paměť
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    start_time=t.time()
    t.sleep(wait_time)
    solver = PR.Ridder()
    try:
        koreny = solver(fce, -10, 10).x0
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False
#ROOTFINDING
def rootfinding_fce(fce):
    """
    Funkce z knivny rootfinding
    jedná se modifikovanou a optimalizovanou medodu bisekce
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen

    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny = RF.bisect(fce, [-10, 10])
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny.root)
        return (t.time()-start_time)-wait_time
    return False
#ROOT_SOLVE
def root_solve_cubic(koef):
    """
    Funkce z knivny root-solve
    jedná se modifikovanou iterační metodu pro polynom 3 stupně
    Omezením je že výpočte kořeny pouze polynomu a to jen do 3. stupně
    inputem fukce je array koeficientů nikoli funkce samotná

    """
    start_time=t.time()
    t.sleep(wait_time)
    try:
        koreny = RS.solve_cubic(koef[0],koef[1],koef[2],koef[3])
    except:
        koreny = "nelze vypočíst"
        print(koreny)
    else:
        print(koreny)
        return (t.time()-start_time)-wait_time
    return False

fce_in = linear
scipy_print_output ="scipy-library"+'\n'+ "bisekce: "+(str) (scipy_bisect(fce_in))+'\n'+ "solver: "+(str) (scipy_brentq(fce_in)) +'\n'+"newton: "+(str) (scipy_newton(fce_in)) +'\n'+"rider: "+(str) (scipy_riderfce(fce_in))+'\n'+"fsolve: "+(str)(scipy_fsolve(fce_in))
print(scipy_print_output)
pyroot_print_output = "pyroot-library"+'\n'+"bisekce: "+ (str)(pyroot_bisec(fce_in))+'\n'+"brent: "+(str)(pyroot_brent(fce_in))+'\n'+"ridder: "+(str)(pyroot_ridder(fce_in))
print(pyroot_print_output)
rootfinding_print_output = "rootfinding-library"+'\n'+ "bisec: "+(str)(rootfinding_fce(fce_in))
print(rootfinding_print_output)
root_solve_print_output = root_solve_cubic([3,-1,2,10])
print("root-solve-library"+'\n'+ "cubic: "+(str)(root_solve_print_output))
print("done")
