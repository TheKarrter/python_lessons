import pygame
import variables

def run():
    pygame.init()
    screen = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT))
    pygame.display.set_caption('Tic-tac-toe')
    screen.fill(variables.WHITE)
    pygame.draw.line(screen, 
                     variables.BLACK, 
                     (0,(variables.HEIGHT//3)*1),
                     (variables.WIDTH,(variables.HEIGHT//3)*1),
                     variables.LINE_WIDTH)
    pygame.draw.line(screen, 
                     variables.BLACK, 
                     (0,(variables.HEIGHT//3)*2),
                     (variables.WIDTH,
                      (variables.HEIGHT//3)*2),
                      variables.LINE_WIDTH)
    pygame.draw.line(screen, 
                     variables.BLACK, 
                     ((variables.WIDTH//3)*1,0),
                     ((variables.WIDTH//3)*1,variables.HEIGHT),
                     variables.LINE_WIDTH)
    pygame.draw.line(screen, 
                     variables.BLACK, 
                     ((variables.WIDTH//3)*2,0),
                     ((variables.WIDTH//3)*2,variables.HEIGHT),
                     variables.LINE_WIDTH)
    return screen