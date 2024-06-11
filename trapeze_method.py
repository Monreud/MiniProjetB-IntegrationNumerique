# Intégration avec méthode des trapèzes
import numpy as np
def integration_trapeze_numpy (borne_inf, borne_sup, nombre_de_segments):

    p1 = 1
    p2 = 2
    p3 = 3
    p4 = 4
    integrale_trapeze = []
    #x1 = np.linspace(borne_inf, borne_sup - (borne_sup - borne_inf) / (nombre_de_segments), nombre_de_segments)
    #x2 = np.linspace(borne_inf + (borne_sup - borne_inf) / (nombre_de_segments), borne_sup + (borne_sup - borne_inf) / (nombre_de_segments), nombre_de_segments)
    x = np.linspace(borne_inf,borne_sup,nombre_de_segments)
    y = p1 + p2*x + p3*x**2 + p4*x**3

    x1 = np.linspace(borne_inf, borne_sup - (borne_sup - borne_inf)/(nombre_de_segments + 1), nombre_de_segments)
    x2 = np.linspace(borne_inf + (borne_sup - borne_inf)/(nombre_de_segments + 1), borne_sup, nombre_de_segments)

    y1 = p1 + p2*x1 + p3*x1**2 + p4*x1**3
    y2 = p1 + p2*x2 + p3*x2**2 + p4*x2**3

    t = (x2 - x1) * ((y2 + y1)/2)
    trapeze = np.sum(t)

    print(len(x1), len(x2))
    # print (f'x1 = {x1}\nx2 = {x2}')
    print(trapeze)
    print(np.trapz(y, x))
    return trapeze

integration_trapeze_numpy(-2, 3, 1000)

def custom_linspace(a, b, n):
    real_b = b + (b - a) / (n + 1)
    step = (real_b - a) / (n - 1)
    result = [a + i * step for i in range(n)]
    return result



def integration_trapeze_pyhton (borne_inf, borne_sup, nombre_de_segments):
    p1 = 1
    p2 = 2
    p3 = 3
    p4 = 4
    sum_trapz = 0



    x = custom_linspace(borne_inf, borne_sup, nombre_de_segments)

    def function(x):
        y = p1 + p2 * x + p3 * x**2 + p4 * x**3
        return y

    for i in range(len(x) - 1):
        sum_trapz += (x[i + 1] - x[i]) * ((function(x[i]) + function(x[i + 1])) / 2)
    return sum_trapz

print(integration_trapeze_pyhton(-2,3,1000))