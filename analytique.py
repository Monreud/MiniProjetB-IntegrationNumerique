"""

"""

import numpy as np


def integrate(b, a, p1, p2, p3, p4):

    def f_primitive(x):
        return p1 * x + p2 * x ** 2 / 2 + p3 * x ** 3 / 3 + p4 * x ** 4 / 4

    i_exact = f_primitive(b) - f_primitive(a)

    return i_exact


def integrate_rectangle(b, a, p1, p2, p3, p4, n):
    bornes_n = np.linspace(a, b + (b-a) / (n+1), n)

    i_rectangle = 0

    def f_primitive(x):
        return p1 * x + p2 * x ** 2 / 2 + p3 * x ** 3 / 3 + p4 * x ** 4 / 4

    for i in range(n-1):
        i_rectangle += f_primitive(bornes_n[i+1]) - f_primitive(bornes_n[i])

    return i_rectangle


def calcul_erreur(exact, rectangle):
    return rectangle - exact


if __name__ == '__main__':
    print('Bienvenue dans votre integrateur de fonction, I = INT(f(x)dx entre a et b \n')
    print('La fonction est de la forme f(x) = p1 + p2x + p3x² + p3x^3 \n')
    print('L intégrale est de la forme F(x) = p1x + p2x²/2 + p3x^3/3 + p4x^4/4 \n')

    borne_a = int(input('Que vaut la borne a ? '))
    borne_b = int(input('Que vaut la borne b ? '))

    p1 = int(input('Que vaut p1 ? '))
    p2 = int(input('Que vaut p2 ? '))
    p3 = int(input('Que vaut p3 ? '))
    p4 = int(input('Que vaut p4 ? '))
    n = int(input('Combien de points ? '))

    y = np.linspace(borne_b, borne_a, n)
    poly = p1 + p2 * y + p3 * y ** 2 + p4 * y ** 3

    print('EXACT = ', integrate(borne_b, borne_a, p1, p2, p3, p4))
    print('RECTANGLE = ', integrate_rectangle(borne_b, borne_a, p1, p2, p3, p4, n))
    print('TRAPEZE = ', abs(np.trapz(poly, y)))
    print('ERREUR = ', calcul_erreur(integrate(borne_b, borne_a, p1, p2, p3, p4), integrate_rectangle(borne_b, borne_a, p1, p2, p3, p4, n)))
