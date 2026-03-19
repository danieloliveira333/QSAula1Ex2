import math

def formulaResolvente(a, b, c):
    if a == 0:
        raise ValueError("Coeficiente 'a' não pode ser zero")
    delta = b**2 - 4*a*c
    if delta <= 0:
        return None  # sem raízes reais
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2