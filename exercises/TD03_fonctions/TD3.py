def pluriel(chaine,valeur):
    """Détermine si une valeur doit être écrite au pluriel ou non"""
    if valeur > 1:
        return str(valeur) + chaine+"s"
    elif valeur == 0:
        return ""
    else:
        return str(valeur)+ chaine
   
temps = (1,0,14,13) 
print(pluriel("jour", 0))

def afficheTemps(temps):
    """Affiche une phrase qui indique à quoi chaque valeur de mon tuples (la valeur de temps) correspond"""
    print("mon temps est:", pluriel("jour",temps[0]), pluriel("heure",temps[1]), pluriel("minute",temps[2]), pluriel("seconde",temps[3]))
    
afficheTemps((2,0,14,23))
