# Intégration numérique - Méthodes des rectangles, des trapèzes et de Simpson
## Utilisation - A noter
L'affichage des courbes ainsi que les timeit ne sont pas vectorisés. Afin d'éviter des temps de calcul trop longs voires difficiles selon votre machine, veuillez commenter au préalable les lignes indiquées dans le main (commentez tous les timeits ou ceux non désirés). Le programme n'affiche qu'une courbe à la fois, veuillez donc décommenter uniquement celle qui vous intéresse (idem pour les variables de la boucle for précédente).    
Selon le plot que vous désirez, vous devez décommenter les timeit correspondants (double clique sur les paramètres des plots pour les voir plus simplement).  
Cela ne concerne que les graphes des temps de calcul.
Le repository contient alors plusieurs modules :  
- main.py
- analytique.py : avec la méthode analytique et rectangles ainsi que la fonction de calcul d'erreur
- simson_method.py : avec la méthode de Simpson
- trapeze_method.py : avec la méthode des Trapèzes
Pour lancer le script, lancez simplement le main.
SI VOUS SOUHAITEZ SIMPLEMENT TESTER LE SCRIPT POUR UN NOMBRE DONNÉ DE POINTS, COMMENTEZ DEPUIS LE FOR DU MAIN JUSQU'A LA FIN.
A nouveau : cela ne concerne que les graphes des temps de calcul.
### Méthode des rectangles
La méthode a été programmée en se basant sur le modèle hauteur * largeur de l'aire d'un rectangle. 
### Méthode des trapèzes
Similaire à la méthode des rectangles, mais avec la forme des trapèzes. Pour la version python, besoin d'adapter linspace par de la compréhension de liste.
### Méthode de Simpson
Approxime une parabole sous la courbe et utilise également une compréhension de liste pour remplacer le linspace en python uniquement.
### Améliorations 
- Le main pourrait être séparé en plusieurs fonctions (notamment pour l'affichage des courbes et la gestion des attributions de variables).
- Le main manque de vectorisation (la boucle for mêlée aux timeit nécessite de commenter les timeit non nécessaires)
## Références
- Consignes projetB
- PyPI
- Scipy
