# Intégration avec méthode des trapèzes
import numpy as np
import timeit
def integration_trapeze_numpy (borne_inf, borne_sup, p1, p2, p3, p4, nombre_de_segments):

    x1 = np.linspace(borne_inf, borne_sup - (borne_sup - borne_inf)/(nombre_de_segments + 1), nombre_de_segments) # a
    x2 = np.linspace(borne_inf + (borne_sup - borne_inf)/(nombre_de_segments + 1), borne_sup, nombre_de_segments) # b

    y1 = p1 + p2*x1 + p3*x1**2 + p4*x1**3 # f(a)
    y2 = p1 + p2*x2 + p3*x2**2 + p4*x2**3 # f(b)

    t = (x2 - x1) * ((y2 + y1)/2) # integration avec la méthode des trapèzes
    trapeze = np.sum(t)

    return trapeze


# On créé l'équivalent de la fonction linspace de numpy
def custom_linspace(a, b, n):
    real_b = b + (b - a) / (n + 1) # la borne b doit faire un pas de plus pour faire b - a
    step = (real_b - a) / (n - 1) # On applique la formule du pas
    result = [a + i * step for i in range(n)] # On créé notre linspace
    return result

def integration_trapeze_pyhton (borne_inf, borne_sup, p1, p2, p3, p4, nombre_de_segments):

    sum_trapz = 0
    x = custom_linspace(borne_inf, borne_sup, nombre_de_segments)

    # On définit notre polynome avec une fonction
    # pour eviter de faire une boucle qui remplit chaque valeur de la liste y
    def function(x):
        y = p1 + p2 * x + p3 * x**2 + p4 * x**3
        return y

    for i in range(len(x) - 1):
        # On applique simplement la formule
        sum_trapz += (x[i + 1] - x[i]) * ((function(x[i]) + function(x[i + 1])) / 2)
    return sum_trapz

######## Comparaison de la précision de calcul et du temps d'exécution pour chacune des méthodes
print(f'trapeze numpy = {integration_trapeze_numpy(-2, 3, 1, 2, 3, 4, 1000)}')
print(f'trapeze python = {integration_trapeze_pyhton(-2,3, 1, 2, 3 ,4, 1000)}')

x = np.linspace(-2, 3,1000)
y = 1 + 2*x + 3*x**2 + 4*x**3
print(f'trapz = {np.trapz(y,x)}')

print(timeit.timeit('integration_trapeze_numpy(-2, 3, 1, 2, 3, 4, 1000)', globals=globals(), number = 1000))
print(timeit.timeit('integration_trapeze_pyhton(-2,3, 1, 2, 3, 4, 1000)', globals=globals(), number = 1000))
print(timeit.timeit('np.trapz(y,x)', globals=globals(), number = 1000))
