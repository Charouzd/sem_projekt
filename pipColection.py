
"""
    knihovna inbuild funkcí pro výpočet kořenů v pythonu
    Použité knihovny: Scipy, Pyroots, Rootfinging, numpy, Root-solver, Root-Calculator

    pip install pyroots
    pip install scipy
    pip install numpy
    pip install matplotlib
    pip install rootfinding
    pip install root-calculator

    Výsledek: kořen(y)

"""
import numpy as np
import scipy.optimize as SP
import rootfinding as RF
import pyroots as PR
import root_solver as RS
# import  root_calculator - není implemontován,existuje pouze dokumentace

#SCIPY METODY
def scipy_fsolve(fce,a,b):
    """
    Funkce z knivny scipy
    funguje na principu jacobiho iterace a derivace
    Nejsou zde omezení

    """
    try:
        koreny=SP.fsolve(fce,[a,b])
    except:
        koreny = "koreny nelze vypočíst"
        return (koreny)
    return koreny
def scipy_brentq(fce,a,b):
    """
    Funkce z knivny scipy
    funguje na principu kombinace bisekce secans metody
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen

    """
    try:
        koreny=SP.brentq(fce,a,b)
    except:
       return "koreny nelze vypočíst"
    return koreny

def scipy_riderfce(fce,a,b):
    """
    Funkce z knivny scipy
    funguje na principu aproximace funkce exponencielou
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    try:
        koreny=SP.ridder(fce,a,b)
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny
    return False
def scipy_newton(fce,a,b):
    """
    Funkce z knivny scipy
    funguje na principu derivace
    Omezení žádné není
    """
    try:
        koreny=SP.newton(fce,[a,b])
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny
def scipy_bisect(fce,a,b):
    """
    Funkce z knivny scipy
    funguje na principu aproximace funkce exponencielou
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen

    """
    try:
        koreny=SP.bisect(fce,a,b)
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny
#PYROOT METODY
def pyroot_brent(fce,a,b):
    """
    Funkce z knivny pyroot
    funguje jedá se o téměř stejnou implementaci jako ve knihovně scipy
    je samostatná => menší náročnost na paměť
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    solver = PR.Brentq()
    try:
        koreny = solver(fce, a, b).x0
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny
    return False
def pyroot_bisec(fce,a,b):
    """
    Funkce z knivny pyroot
    funguje jedá se o téměř stejnou implementaci jako ve knihovně scipy, ale je samostatná => menší náročnost na paměť
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    solver = PR.Bisect()
    try:
        koreny = solver(fce, a, b).x0
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny
def pyroot_ridder(fce,a,b):
    """
    Funkce z knivny pyroot
    funguje jedá se o téměř stejnou implementaci jako ve knihovně scipy, ale je samostatná => menší náročnost na paměť
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen a MUSÍ být spojiná

    """
    solver = PR.Ridder()
    try:
        koreny = solver(fce, a, b).x0
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny
#ROOTFINDING
def rootfinding_fce(fce,a,b):
    """
    Funkce z knivny rootfinding
    jedná se modifikovanou a optimalizovanou medodu bisekce
    Omezení na zvoleném intervalu se musí nacházet pouze jeden kořen

    """

    try:
        koreny = RF.bisect(fce, [a, b])
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny.root
#ROOT_SOLVE
def root_solve_cubic(koef):
    """
    Funkce z knivny root-solve
    jedná se modifikovanou iterační metodu pro polynom 3 stupně
    Omezením je že výpočte kořeny pouze polynomu a to jen do 3. stupně
    inputem fukce je array koeficientů nikoli funkce samotná

    """
    try:
        koreny = RS.solve_cubic(koef[0],koef[1],koef[2],koef[3])
    except:
        koreny = "nelze vypočíst"
    else:
        return koreny