def trois_meme(element_un, element_deux, element_trois): #input de type string
    """Renvoie True si les trois éléments sont les même et différents du caractère '_'."""
    return element_un == element_deux == element_trois and element_un != '_'
        

def ligne(grille):
    for num_ligne in range(3): # parcours les 3 lignes de haut en bas
        if trois_meme(grille[num_ligne][0], grille[num_ligne][1], grille[num_ligne][2]):
            return True
    return False
    
def colonne(grille):
    for num_col in range(3):
        if trois_meme(grille[0][num_col], grille[1][num_col], grille[2][num_col]):
            return True
    return False
        
def diago(grille):
    if trois_meme(grille[0][0], grille[1][1], grille[2][2]):
        return True
    elif trois_meme(grille[2][0], grille[1][1], grille[0][2]):
        return True
    else : 
        return False

def victoire(grille):
    return ligne(grille) or colonne(grille) or diago(grille)
            
            
def creation_grille():
    grille = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]
    return grille
    
    
def afficher_grille(grille):
    for sous_liste in grille:
        print(sous_liste)
    

def jouer(grille):
    symbole = input("Quel symbole joues-tu ? ")
    
    ligne = int(input("Sur quelle ligne ? "))
    
    colonne = int(input("Sur quelle colonne ? "))
    
    grille[ligne][colonne] = symbole


def main():
    notre_grille = creation_grille()
    afficher_grille(notre_grille)
    
    
    while not victoire(notre_grille):
        jouer(notre_grille)
        afficher_grille(notre_grille)
    
    print("Bravo, fin de partie !!")
        
    
    
main()

    