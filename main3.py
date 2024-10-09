#coding: utf-8
import math

def Eq2grau(a, b, c):
    # Calcul de Delta (discriminant)
    Delta = math.pow(b, 2) - 4 * a * c
    x1 = None
    x2 = None
    if Delta > 0:
        # Il y a deux racines réelles distinctes
        x1 = (-b - pow(Delta, 0,5)) / (2 * a)
        x2 = (-b + pow(Delta, 0,5)) / (2 * a)
        
    elif Delta == 0:
        print (" ha rize unica, Delta", Delta)
        # Il y a une racine réelle unique
        
    else:
        print (" rizes complexes, Delta", Delta)
        # Il n'y a pas de racines réelles
        return x1, x2, Delta
    

def Eq2grauCapivara(a, b, c):
    Delta = math.pow(b, 2) - 4 * a * c

if Delta > 0:
        print("ha duas raizes reais distinct")
        # Il y a deux racines réelles distinctes
        x1 = (-b - pow(Delta, 0,5)) / (2 * a)
        x2 = (-b + pow(Delta, 0,5)) / (2 * a)
        
    elif Delta == 0:
        print (" ha rize unica, Delta", Delta)
        x= -b / (2*a)
        return x, Delta
        
    else:
        print (" rizes complexes, Delta", Delta)
        # Il n'y a pas de racines réelles
        return  Delta