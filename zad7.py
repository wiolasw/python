#y=ax^2+bx+c
import math
import sys

print("Skrypt oblicza pierwiastki równania kwadratowego")
a = float(input("Podaj wartość a: \n"))
b = float(input("Podaj wartość b: \n"))
c = float(input("Podaj wartość c: \n"))

delta = (b*b) -(4*a*c)
if delta <0:
    print ("Funkcja nie ma pierwistków")
elif delta == 0:
    x0 = -(b/(2*a))
    print("Funckja ma dokładnie jedno miejsce zerowe x0 = {}".format(x0))
else:
    pierw_delt = math.sqrt(delta)
    x1=(-b + pierw_delt)/(2*a)
    x2=(-b + pierw_delt)/(2*a)
    print("Funkcja ma dwa pierwiastki kwadratowe x1 = {} i x2 = {}".format(x1,x2))
