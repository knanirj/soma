#coding: utf-8
import math

def Eq2grau(a, b, c): 
    # Calcul de Delta (discriminant)
    Delta = math.pow(b, 2) - 4 * a * c
    if Delta > 0: 
        # Il y a deux racines réelles distinctes
        x1 = (-b - math.sqrt(Delta)) / (2 * a)
        x2 = (-b + math.sqrt(Delta)) / (2 * a)
        return x1, x2
    elif Delta == 0:
        # Il y a une racine réelle unique
        x = -b / (2 * a)
        return x, x  # On retourne deux fois la même racine
    else:
        # Il n'y a pas de racines réelles
        return None

if __name__ == "__main__": 
    # Appel de la fonction avec les coefficients a, b, c
    result = Eq2grau(1, 4, 4)
    
    if result:
        x1, x2 = result
        print(f"As raízes são {x1} e {x2}")
    else:
        print("Não há raízes reais")
