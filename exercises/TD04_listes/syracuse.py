#Partie 2 question 1 et 2

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    L1=[3]
    while n != 1:
        if n % 2 == 0:
            n=n//2
            L1.append(n)
        else:
            n=n*3 + 1
            L1.append(n)
    return L1

print(syracuse(3))

#Partie 2 question 3

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    a=syracuse(n_max)
    if a[-1]==1:  #dernière élément de la liste renvoyé par syracuse = 1 alors la conjecture est vraie
        return True
    else:
        return False


print(testeConjecture(10000))

#Partie 2 question 4

def tempsVol(n):
    """ Retourne le temps de vol de n """
    a=syracuse(n)
    return (len(a)-1)

print("Le temps de vol de", 3, "est", tempsVol(3))

#Partie 2 question 5

def tempsVolListe(n_max):
    """Retourne la liste de tous les temps de vol de 1 à n_max"""
    L=[]
    for i in range (1,n_max+1):
        a=tempsVol(i)
        L.append(a)
    return L
    

print(tempsVolListe(100))

#en compréhension de liste :

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1,n_max+1)] # L= [expr for x in t]

print(tempsVolListe(100))

#Partie 2 question 6

"""Déterminer quel entier entre 1 et 10000 a le plus grand temps de vol (réponse 6171 qui a le temps de vol 261)."""
liste_triee = sorted(tempsVolListe(10000))
print(liste_triee[-1]) #dernière valeur de la liste triéé, donc temps de vol max
print(tempsVolListe(10000).index(261)+1) #donne l'indice de l'élément ayant comme valeur 261, or le premier indice de la liste est 0 donc 261 + 1

#Partie 2 question 7

"""L’altitude maximale de l'entier `n` est la plus grande valeur par laquelle passe `n` au cours de son vol. 
Déterminer quel entier entre 1 et 10000 a la plus grande altitude maximale (réponse 27114424, atteint par l'entier 9663). 
Ne pas hésiter à écrire de nouvelles fonctions pour cela."""
liste=[]
for i in range(1,10001):
    liste.append(max(syracuse(i))) #ajoute le maximum de chaque liste donné par syracus pour les n de e1 à 10000 dans une liste vide

liste_copie=list(liste) #on fait une copie de la liste

liste.sort() #trie la liste avec les valeurs max de chaque liste allant de 1 à 10000

print(liste[-1]) #donne le max de la liste (triée) ayant les valeurs max de chaque liste allat de 1 à 10000

print(liste_copie.index(27114424)+1) #donne la position i-1 de la valeur 27114424 dans la liste des valeurs max des listes de syracus
                                     # pour les n allant de 1 à 10000 (d'où le +1)


