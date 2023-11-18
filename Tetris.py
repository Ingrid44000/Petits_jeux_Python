import pygame
import random

square = 40

colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]

figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

class Case:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def afficher(self, surface):
        pygame.draw.rect(surface, self.couleur, pygame.Rect(self.x*40, self.y*40, 40, 40), 2)
        pygame.display.flip()
        
class Grille():
    def __init__(self, hauteur, largeur):
        self.grille = [[Case(x,y, couleur = (255,255,255)) for x in range(largeur)] for y in range(hauteur)]
        self.hauteur = hauteur
        self.largeur = largeur
        
          
        
    def affichergrille(self, surface):
        for sousliste in self.grille:
            for case in sousliste:
                case.afficher(surface)
                
        
        
class Figure:
    
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(colors) # You can choose different colors for each shape
        self.rotation = 0
    
    
    
    def new_piece(self):
        # Choose a random shape
        figure = random.choice(figures)
        # Return a new Tetromino object
        return Figure(4, 0, figure)

def main():
    pygame.init()
    surface = pygame.display.set_mode((650,750))
    
    
    grille = Grille(18, 10)
    grille.affichergrille(surface)
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("haut")
                if event.key == pygame.K_DOWN:
                    print("bas")
                if event.key == pygame.K_LEFT:
                    print("gauche")
                if event.key == pygame.K_RIGHT:
                    print("droite")




main()