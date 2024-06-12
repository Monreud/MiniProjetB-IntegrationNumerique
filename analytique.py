"""

"""
import numpy as np


def integrate(a, b, p1, p2, p3, p4):

    def f_primitive(x):
        return p1 * x + p2 * x ** 2 / 2 + p3 * x ** 3 / 3 + p4 * x ** 4 / 4

    i_exact = f_primitive(b) - f_primitive(a)

    return i_exact


def custom_linspace(a, b, n):
    real_b = b + (b - a) / (n + 1)
    step = (real_b - a) / (n - 1)
    result = [a + i * step for i in range(n)]
    return result


"""def integrate_rectangle(a, b, p1, p2, p3, p4, n):
    bornes_n = custom_linspace(a, b, n)
    i_rectangle = 0

    def f_primitive(x):
        return p1 * x + p2 * x ** 2 / 2 + p3 * x ** 3 / 3 + p4 * x ** 4 / 4

    for i in range(n-1):
        i_rectangle += f_primitive(bornes_n[i+1]) - f_primitive(bornes_n[i])

    return i_rectangle """


def integrate_rectangle(a, b, p1, p2, p3, p4, n):
    largeur_rectangle = (b - a) / n
    i_rectangle = 0

    def f(x):
        return p1 + p2 * x + p3 * x**2 + p4 * x**3

    for i in range(int(n)-1):
        x = a + i * largeur_rectangle
        i_rectangle += f(x) * largeur_rectangle

    return i_rectangle


def integrate_rectangle_numpy(a, b, p1, p2, p3, p4, n):
    bornes_n = np.linspace(a, b + (b - a) / (int(n) + 1), int(n))
    largeur_rectangle = (b - a) / int(n)

    def f(x):
        return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

    # Calculer les hauteurs des rectangles
    hauteur_rectangle = f(bornes_n)

    # Calculer l'aire totale
    i_rectangle_numpy = np.sum(hauteur_rectangle * largeur_rectangle)

    # i_rectangle_numpy = np.sum(np.diff(f(bornes_n)))

    return i_rectangle_numpy


def calcul_erreur(exact, methode):
    return methode - exact


def simpson(a, b, p1, p2, p3, p4, n):
    bornes_n = custom_linspace(a, b, n)
    i_simpson = 0

    def f_simpson(x):
        return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

    for i in range(int(n)-1):
        i_simpson += (bornes_n[i+1] - bornes_n[i]) / 6 * (f_simpson(bornes_n[i]) + 4 * f_simpson((bornes_n[i] + bornes_n[i+1]) / 2) + f_simpson(bornes_n[i+1]))

    return i_simpson


