import numpy as np


def integration_simson_numpy(borne_inf, borne_sup, p1, p2, p3, p4, nombre_de_segments):

    x1 = np.linspace(borne_inf, borne_sup - (borne_sup - borne_inf) / (nombre_de_segments + 1), nombre_de_segments)  # a
    x2 = np.linspace(borne_inf + (borne_sup - borne_inf) / (nombre_de_segments + 1), borne_sup, nombre_de_segments)  # b

    y1 = p1 + p2 * x1 + p3 * x1 ** 2 + p4 * x1 ** 3  # f(a)
    y2 = p1 + p2 * x2 + p3 * x2 ** 2 + p4 * x2 ** 3  # f(b)
    y_simson = p1 + ((x1 + x2)/2) * p2 + ((x1 + x2)/2) ** 2 * p3 + ((x1 + x2)/2) ** 3 * p4  # f( (a+b)/2 )

    simson = ((x2 - x1) / 6) * (y1 + 4 * y_simson + y2)
    simson_somme = np.sum(simson)

    return simson_somme

# On créé l'équivalent de la fonction linspace de numpy


def custom_linspace(a, b, n):
    real_b = b + (b - a) / (n + 1)  # la borne b doit faire un pas de plus pour faire b - a
    step = (real_b - a) / (n - 1)  # On apllique la formule du pas
    result = [a + i * step for i in range(n)]  # On créé notre linspace
    return result


def integration_simson_python(borne_inf, borne_sup, p1, p2, p3, p4, nombre_de_segments):

    simson_py = 0
    x = custom_linspace(borne_inf, borne_sup, nombre_de_segments)

    def function(x_function):
        # f(a) ou f(b) en fonction de si x1 ou x2 est passé en paramètre
        y = p1 + p2 * x_function + p3 * x_function**2 + p4 * x_function**3
        return y

    def function_simson(x1, x2):
        y_simson = p1 + ((x1 + x2) / 2) * p2 + ((x1 + x2) / 2) ** 2 * p3 + ((x1 + x2) / 2) ** 3 * p4  # f( (a+b)/2 )
        return y_simson

    for i in range(len(x) - 1):
        # formule de simson
        simson_py += ((x[i+1] - x[i])/6) * (function(x[i]) + function(x[i+1]) + 4 * function_simson(x[i], x[i+1]))

    return simson_py

