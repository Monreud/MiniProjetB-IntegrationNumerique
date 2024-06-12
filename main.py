"""
Ce code exécute l'ensemble des modules analytique; qui contient la méthode des rectangles et exacte; simpson et trapèzes.
Il vous demande d'entrer les bornes a et b, les paramètres p1 à p4 ainsi qu'un nombre de points.
Ce nombre de points est utilisé pour voux afficher en console des résultats (résultat de l'intégrale, erreur de la méthode et temps de calcul).
Ce script exécute aussi l'affichage des courbes.
!!!!!!!!!! IMPORTANT !!!!!!!!!! : METTEZ EN COMMENTAIRES LES TIMEIT NON DÉSIRÉS AFIN D'AMÉLIORER LE TEMPS DE COMPILATION. ILS SONT INDIQUÉS ET SE TROUVE DANS LA BOUCLE FOR.
"""
import timeit
import numpy as np
from scipy import integrate as it
import matplotlib.pyplot as plt
import analytique
import trapeze_method as trapz_meth
import simson_method as sim_meth

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
        x = np.linspace(borne_a, borne_b, int(number))
        poly = p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3
        return x, poly

    poly, x = test_trapz(n)

    # RECTANGLES
    print('EXACT = ', analytique.integrate(borne_a, borne_b, p1, p2, p3, p4))
    print('RECTANGLE = ', analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, n))
    erreur_rectangle_python = analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', erreur_rectangle_python)

    print('RECTANGLE NUMPY = ', analytique.integrate_rectangle_numpy(borne_a, borne_b, p1, p2, p3, p4, n))
    erreur_rectangle_numpy = analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                analytique.integrate_rectangle_numpy(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', erreur_rectangle_numpy)

    print('TRAPEZE = ', abs(np.trapz(poly, x)))

    duree_rect_python = timeit.timeit('analytique.integrate_rectangle(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000)
    print('Temps de compute rectangles python : ', duree_rect_python)
    duree_rect_numpy = timeit.timeit('analytique.integrate_rectangle_numpy(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000)
    print('Temps de compute rectangles numpy : ', duree_rect_numpy)


    # TRAPEZES
    print(f'trapeze numpy = {trapz_meth.integration_trapeze_numpy(borne_a, borne_b, p1, p2, p3, p4, 1000)}')
    erreur_trapeze_numpy = analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                trapz_meth.integration_trapeze_numpy(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', erreur_trapeze_numpy)

    print(f'trapeze python = {trapz_meth.integration_trapeze_pyhton(borne_a, borne_b, p1, p2, p3, p4, 1000)}')
    erreur_trapeze_python = analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                trapz_meth.integration_trapeze_pyhton(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', erreur_trapeze_python)

    duree_trapz_numpy = timeit.timeit('trapz_meth.integration_trapeze_numpy(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000)
    print('Temps de compute trapèze numpy : ', duree_trapz_numpy)
    duree_trapz_python = timeit.timeit('trapz_meth.integration_trapeze_pyhton(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000)
    print('Temps de compute trapèzes python : ', duree_trapz_python)


    # SIMPSON
    print(f'simson numpy = {sim_meth.integration_simson_numpy(borne_a, borne_b, p1, p2, p3, p4, 1000)}')
    erreur_simpson_numpy = analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                sim_meth.integration_simson_numpy(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', erreur_simpson_numpy)
    print(f'simson python = {sim_meth.integration_simson_python(borne_a, borne_b, p1, p2, p3, p4, 1000)}')

    erreur_simpson_python = analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                sim_meth.integration_simson_python(borne_a, borne_b, p1, p2, p3, p4, n))
    print('ERREUR = ', erreur_simpson_python)

    duree_simpson_numpy = timeit.timeit('sim_meth.integration_simson_numpy(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000)
    print('Temps de compute Simpson numpy : ', duree_simpson_numpy)
    duree_simpson_python = timeit.timeit('sim_meth.integration_simson_python(borne_a,borne_b,p1,p2,p3,p3,n)', globals=globals(), number=1000)
    print('Temps de compute Simpson python : ', duree_simpson_python)

    # SET UP DE PLOT
    n_tab = np.linspace(10, 509, 500)

    valeurs_rectangle_python = []
    valeurs_rectangle_numpy = []
    erreur_rectangle_python = []
    erreur_rectangle_numpy = []
    duree_rect_python = []
    duree_rect_numpy = []

    valeurs_trapeze_python = []
    valeurs_trapeze_numpy = []
    erreur_trapeze_python = []
    erreur_trapeze_numpy = []
    duree_trapz_python = []
    duree_trapz_numpy = []

    valeurs_simpson_python = []
    valeurs_simpson_numpy = []
    erreur_simpson_python = []
    erreur_simpson_numpy = []
    duree_simpson_python = []
    duree_simpson_numpy = []

    valeurs_simpson_reel = []
    valeurs_trapeze_reel = []
    duree_simpson_reel = []
    duree_trapeze_reel = []

    """ ICI COMMENTER JUSQUA LA FIN SI GRAPHES PAS VOULUS"""

    for k in range(len(n_tab)):
        valeurs_rectangle_python.append(analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k])))
        valeurs_rectangle_numpy.append(analytique.integrate_rectangle_numpy(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k])))
        erreur_rectangle_python.append(analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                analytique.integrate_rectangle(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k]))))
        erreur_rectangle_numpy.append(analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                analytique.integrate_rectangle_numpy(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k]))))
        """ !!!!! ICI TIMEIT !!!!! """
        # duree_rect_python.append(timeit.timeit('analytique.integrate_rectangle(borne_a,borne_b,p1,p2,p3,p3,int(n_tab[k]))', globals=globals(), number=1000))
        # duree_rect_numpy.append(timeit.timeit('analytique.integrate_rectangle_numpy(borne_a,borne_b,p1,p2,p3,p3,int(n_tab[k]))', globals=globals(), number=1000))

        valeurs_trapeze_python.append(trapz_meth.integration_trapeze_pyhton(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k])))
        valeurs_trapeze_numpy.append(trapz_meth.integration_trapeze_numpy(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k])))
        erreur_trapeze_python.append(analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                trapz_meth.integration_trapeze_pyhton(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k]))))
        erreur_trapeze_numpy.append(analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                trapz_meth.integration_trapeze_numpy(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k]))))
        """ !!!!! ICI TIMEIT !!!!! """
        # duree_trapz_python.append(timeit.timeit('trapz_meth.integration_trapeze_pyhton(borne_a,borne_b,p1,p2,p3,p3,int(n_tab[k]))', globals=globals(), number=1000))
        # duree_trapz_numpy.append(timeit.timeit('trapz_meth.integration_trapeze_numpy(borne_a,borne_b,p1,p2,p3,p3,int(n_tab[k]))', globals=globals(), number=1000))

        valeurs_simpson_python.append(sim_meth.integration_simson_python(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k])))
        valeurs_simpson_numpy.append(sim_meth.integration_simson_numpy(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k])))
        erreur_simpson_python.append(analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                sim_meth.integration_simson_python(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k]))))
        erreur_simpson_numpy.append(analytique.calcul_erreur(analytique.integrate(borne_a, borne_b, p1, p2, p3, p4),
                                                sim_meth.integration_simson_numpy(borne_a, borne_b, p1, p2, p3, p4, int(n_tab[k]))))
        """ !!!!! ICI TIMEIT !!!!! """
        # duree_simpson_python.append(timeit.timeit('sim_meth.integration_simson_python(borne_a,borne_b,p1,p2,p3,p3,int(n_tab[k]))', globals=globals(), number=1000))
        # duree_simpson_numpy.append(timeit.timeit('sim_meth.integration_simson_numpy(borne_a,borne_b,p1,p2,p3,p3,int(n_tab[k]))', globals=globals(), number=1000))

        x, poly = test_trapz(int(n_tab[k]))
        valeurs_trapeze_reel.append(np.trapz(y=poly, x=x))
        """ !!!!! ICI TIMEIT !!!!! """
        # duree_trapeze_reel.append(timeit.timeit('np.trapz(y=poly, x=x)', globals=globals(), number=1000))
        valeurs_simpson_reel.append(it.simpson(y=poly, x=x))
        """ !!!!! ICI TIMEIT !!!!! """
        # duree_simpson_reel.append(timeit.timeit('it.simpson(y=poly, x=x)',globals=globals(), number=1000))

    """plt.plot(n_tab, valeurs_rectangle_python, label='PYTHON')
    plt.plot(n_tab, valeurs_rectangle_numpy, label='NUMPY')
    plt.title('Méthode des rectangles - Évolution des valeurs selon le nombre de segments')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.plot(n_tab, erreur_rectangle_python, label='PYTHON')
    plt.plot(n_tab, erreur_rectangle_numpy, label='NUMPY')
    plt.title('Méthode des rectangles - Évolution de l\'erreur selon le nombre de segments')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show() 
    plt.plot(n_tab, duree_rect_python, label='PYTHON')
    plt.plot(n_tab, duree_rect_numpy, label='NUMPY')
    plt.title('Méthode des rectangles - Évolution du temps de calcul selon le nombre de segments (pour number=1000)')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(n_tab, valeurs_trapeze_python, label='PYTHON')
    plt.plot(n_tab, valeurs_trapeze_numpy, label='NUMPY')
    plt.plot(n_tab, valeurs_trapeze_reel, label='PRE-PROG')
    plt.title('Méthode des trapèzes - Évolution des valeurs selon le nombre de segments')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show() 
    plt.plot(n_tab, erreur_trapeze_python, label='PYTHON')
    plt.plot(n_tab, erreur_trapeze_numpy, label='NUMPY')
    plt.title('Méthode des trapèzes - Évolution de l\'erreur selon le nombre de segments')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.plot(n_tab, duree_trapz_python, label='PYTHON')
    plt.plot(n_tab, duree_trapz_numpy, label='NUMPY')
    plt.plot(n_tab, duree_trapeze_reel, label='PRE-PROG')
    plt.title('Méthode des trapèzes - Évolution du temps de calcul selon le nombre de segments (pour number=1000)')
    plt.xlabel('nb points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(n_tab, valeurs_simpson_python, label='PYTHON')
    plt.plot(n_tab, valeurs_simpson_numpy, label='NUMPY')
    plt.plot(n_tab, valeurs_simpson_reel, label='PRE-PROG')
    plt.title('Méthode de Simpson - Évolution des valeurs selon le nombre de segments')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.plot(n_tab, erreur_simpson_python, label='PYTHON')
    plt.plot(n_tab, erreur_simpson_numpy, label='NUMPY')
    plt.title('Méthode de Simpson - Évolution de l\'erreur selon le nombre de segments')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.plot(n_tab, duree_simpson_python, label='PYTHON')
    plt.plot(n_tab, duree_simpson_numpy, label='NUMPY')
    plt.plot(n_tab, duree_simpson_reel, label='NUMPY')
    plt.title('Méthode de Simpson - Évolution du temps de calcul selon le nombre de segments (pour number=1000)')
    plt.xlabel('Nombre de points')
    plt.ylabel('Valeur méthode')
    plt.legend()
    plt.grid(True)
    plt.show() """

