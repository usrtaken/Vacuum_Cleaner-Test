# Vacuum_Cleaner-Test
Test technique pour le stage de développeur Full Stack

La société “Fruition Sciences” a décidé de développer un aspirateur automatique.

L’aspirateur doit pouvoir parcourir l'intégralité d’une pièce donnée, sa position est représentée par ses coordonnées (x,y) et d'une lettre indiquant l'orientation selon la notation cardinale anglaise (N,E,W,S). Une pièce est modélisée par une grille rectangulaire.

Par exemple, l’aspirateur peut se trouver dans la position « 0, 0, N », ce qui signifie qu’il se situe dans le coin inférieur gauche de la pièce, et orientée vers le Nord.

Pour contrôler l’aspirateur, une séquence de commandes symbolisée par une suite de lettres lui est envoyée. Les commandes possibles sont « D », « G » et « A ». « D » et « G » font pivoter l’aspirateur de 90° à droite ou à gauche respectivement, sans la déplacer. « A » signifie que l'on avance d'une case dans la direction à laquelle elle fait face, et sans modifier son orientation.

On définit que la case directement au Nord de la position (x, y) a pour coordonnées (x, y+1).

Pour programmer l’aspirateur, on lui fournit un fichier d'entrée formaté ainsi :

La première ligne donne les dimensions de la grille à savoir le nombre de carrés sur l’axe x puis y séparé d’un espace.
Les deux lignes suivantes permettent de commander l’aspirateur :
la première donne sa position initiale, ainsi que son orientation. La position et l'orientation sont fournies sous la forme de 2 chiffres et une lettre, séparés par un espace ;
la seconde est une série d'instructions que l’aspirateur exécutera. Les instructions sont une suite de caractères sans espaces.

Lorsque l’aspirateur achève une série d'instruction, il communique sa position et son orientation.

OBJECTIF
Concevoir et écrire un programme dans le langage de votre choix afin de faire passer le test suivant.
TEST
Le fichier suivant est fourni en entrée :
10 10
5 5 N
DADADADAA

On attend le résultat suivant : 5 6 N
