"""

"""
import timeit
import numpy as np
from scipy import integrate as it
import matplotlib.pyplot as plt
import analytique
import trapeze_method as trapz_meth

if __name__ == '__main__':

    print('Bienvenue dans votre integrateur de fonction, I = INT(f(x)dx entre a et b \n')
    print('La fonction est de la forme f(x) = p1 + p2x + p3x² + p3x^3 \n')
    print('L intégrale est de la forme F(x) = p1x + p2x²/2 + p3x^3/3 + p4x^4/4 \n')

    while 1:
        try:
            borne_a = int(input('Que vaut la borne a ? '))
            borne_b = int(input('Que vaut la borne b ? '))
            p1 = int(input('Que vaut p1 ? '))
            p2 = int(input('Que vaut p2 ? '))
            p3 = int(input('Que vaut p3 ? '))
            p4 = int(input('Que vaut p4 ? '))
            n = int(input('Combien de points ? '))
            break
        except ValueError:
            print('Ce n\'est pas une valeur correcte, veuillez réessayer.')

    def f(x):
        return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

    print(np.linspace(borne_a, borne_b + (borne_b - borne_a) / (n + 1), n))
    print(analytique.custom_linspace(borne_a, borne_b, n))

    def test_trapz(number):
        y = np.linspace(borne_a, borne_b, int(number))
        poly = p1 + p2 * y + p3 * y ** 2 + p4 * y ** 3
        return y, poly

    poly, y = test_trapz(n)

    # RECTANGLES
    print('EXACT = ', analytique.integrate(borne_a, borne_b, p1, p2, p3, p4))
    print('RECTANGLE = ', analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, n))
    print('RECTANGLE NUMPY = ', analytique.integrate_rectangle_numpy(borne_a, borne_b, p1, p2, p3, p4, n))
    print('TRAPEZE = ', abs(np.trapz(poly, y)))
    print('SIMPSON SCIPY= ', it.simpson(y, poly))
    print('SIMPSON PYTHON = ', analytique.simpson(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, n)))
    print(timeit.timeit('integrate_rectangle(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000))
    print(timeit.timeit('integrate_rectangle_numpy(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000))

    # TRAPEZES
    print(f'trapeze numpy = {trapz_meth.integration_trapeze_numpy(-2, 3, 1, 2, 3, 4, 1000)}')
    print(f'trapeze python = {trapz_meth.integration_trapeze_pyhton(-2, 3, 1, 2, 3, 4, 1000)}')
    print(timeit.timeit('trapz_meth.integration_trapeze_numpy(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000))
    print(timeit.timeit('trapz_meth.integration_trapeze_pyhton(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000))

    n_tab = np.linspace(2, 501, 500)
    valeurs_rectangle_python = []
    valeurs_rectangle_numpy = []
    valeurs_trapeze_reel = []
    for k in range(len(n_tab)):
        valeurs_rectangle_python.append(analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, n_tab[k]))
        valeurs_rectangle_numpy.append(analytique.integrate_rectangle_numpy(borne_a, borne_b, p1, p2, p3, p4, n_tab[k]))
        y, poly = test_trapz(n_tab[k])
        valeurs_trapeze_reel.append(np.trapz(poly, y))

    plt.plot(n_tab, valeurs_rectangle_python, label='PYTHON')
    plt.plot(n_tab, valeurs_rectangle_numpy, label='NUMPY')
    plt.plot(n_tab, valeurs_trapeze_reel, label='TRAPZ')
    plt.xlabel('nb points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()

