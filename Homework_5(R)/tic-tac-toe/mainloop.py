import pygame
import variables
import check

def run(screen):
    while variables.RUN:
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                variables.RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1]//variables.CELL_SIZE
                column = pos[0]//variables.CELL_SIZE
                if variables.FIELD[row][column] == '' and not variables.WON:
                    if variables.TURN % 2 == 0:
                        variables.FIELD[row][column] = 'x'
                        pygame.draw.line(screen,
                                         variables.RED,
                                         (0+variables.CELL_SIZE*column, 0+variables.CELL_SIZE*row),
                                         (variables.CELL_SIZE+variables.CELL_SIZE*column, variables.CELL_SIZE+variables.CELL_SIZE*row),
                                         variables.LINE_WIDTH)
                        pygame.draw.line(screen,
                                         variables.RED,
                                         (variables.CELL_SIZE+variables.CELL_SIZE*column, 0+variables.CELL_SIZE*row),
                                         (0+variables.CELL_SIZE*column, variables.CELL_SIZE+variables.CELL_SIZE*row),
                                         variables.LINE_WIDTH)
                        variables.WON = check.win('x')
                    else:
                        variables.FIELD[pos[1]//variables.CELL_SIZE][pos[0]//variables.CELL_SIZE] = 'o'
                        pygame.draw.circle(screen,
                                           variables.BLUE,
                                           (variables.CELL_SIZE//2+variables.CELL_SIZE*column, variables.CELL_SIZE//2+variables.CELL_SIZE*row),
                                           variables.CELL_SIZE//2,
                                           variables.LINE_WIDTH)
                        variables.WON = check.win('o')
                    variables.TURN += 1    
    pygame.quit()
