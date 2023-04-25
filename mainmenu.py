import pygame
pygame.init()

def Drawmenu(screen,FPS):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    SILVER = (192, 192, 192)
    clock = pygame.time.Clock()


    f1 = pygame.font.SysFont('arial', 50)
    text1 = f1.render("NEW GAME", False, WHITE)
    f2 = pygame.font.SysFont('arial', 50)
    text2 = f1.render("CONTINUE", False, WHITE)
    f3 = pygame.font.SysFont('arial', 50)
    text3 = f1.render("RULES", False, WHITE)
    f4 = pygame.font.SysFont('arial', 50)
    text4 = f1.render("EXIT", False, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(WHITE)

        pygame.draw.rect(screen, SILVER, [300, 100, 400, 370])
        pygame.draw.rect(screen, BLACK, [350, 140, 300, 50])
        pygame.draw.rect(screen, BLACK, [350, 220, 300, 50])
        pygame.draw.rect(screen, BLACK, [350, 300, 300, 50])
        pygame.draw.rect(screen, BLACK, [350, 380, 300, 50])

        screen.blit(text1, (390, 135))
        screen.blit(text2, (395, 215))
        screen.blit(text3, (435, 295))
        screen.blit(text4, (460, 375))


        pygame.display.update()
        clock.tick(FPS)
        return screen

