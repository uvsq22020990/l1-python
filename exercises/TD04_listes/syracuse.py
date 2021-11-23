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

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1,n_max+1)]

print(tempsVolListe(100))

#Partie 2 question 6

sort.tempsVolListe(10000)