"""

"""
import numpy as np


def integrate(a, b, p1, p2, p3, p4):

    def f_primitive(x):
        return p1 * x + p2 * x ** 2 / 2 + p3 * x ** 3 / 3 + p4 * x ** 4 / 4

    i_exact = f_primitive(b) - f_primitive(a)

    return i_exact


# Linspace en python par compréhension de liste.
def custom_linspace(a, b, n):
    real_b = b + (b - a) / (n + 1)
    step = (real_b - a) / (n - 1)
    result = [a + i * step for i in range(n)]
    return result


# Les deux version avec et sans numpy
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

    return i_rectangle_numpy


def calcul_erreur(exact, methode):
    return methode - exact



