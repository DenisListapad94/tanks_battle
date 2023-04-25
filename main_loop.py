import pygame
import mainmenu

pygame.init()
# pygame.display.set_caption('Tanks')
#
# pygame.mixer.music.load('Tankshoot.mp3')
# pygame.mixer.music.play()
sound1 = pygame.mixer.Sound('tank_shot.mp3')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

W, H = 1000, 600
sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60


class Tank_34:
    def __init__(self, picture, start_x, start_y, tank_shoot):
        self.Tank_surf = pygame.image.load(picture)
        self.Tank_surf = pygame.transform.scale(self.Tank_surf,
                                                (self.Tank_surf.get_width() // 2,
                                                 self.Tank_surf.get_height() // 2)
                                                )
        self.Tank_rect = pygame.math.Vector2(start_x, start_y)
        self.direction = pygame.math.Vector2(5, 0)
        self.live_tank = 10
        self.tank_shoot = tank_shoot

    def move(self, ml, mr, mu, md):
        key = pygame.key.get_pressed()
        if key[md]:
            self.Tank_rect -= self.direction
            if ignore_wall() == 1:
                self.Tank_rect += self.direction
        elif key[mu]:
            self.Tank_rect += self.direction
            if ignore_wall() == 1:
                self.Tank_rect -= self.direction
        elif key[mr]:
            self.direction.rotate_ip(3)
            if ignore_wall() == 1:
                self.direction.rotate_ip(-3)
        elif key[ml]:
            self.direction.rotate_ip(-3)
            if ignore_wall() == 1:
                self.direction.rotate_ip(3)

    def rotate_t(self):
        self.angle = self.direction.angle_to((0, 0))
        self.rotate_tank = pygame.transform.rotate(self.Tank_surf, self.angle)
        sc.blit(self.rotate_tank, self.rotate_tank.get_rect(center=(round(self.Tank_rect.x), round(self.Tank_rect.y))))


class Bullet:
    def __init__(self, picture, start_x, start_y, direction, key_shoot):
        self.direction = direction
        self.Bullet_surf = pygame.image.load(picture)
        self.Bullet_surf = pygame.transform.scale(self.Bullet_surf, (
            self.Bullet_surf.get_width() // 6, self.Bullet_surf.get_height() // 6))
        self.Bullet_rect = pygame.math.Vector2(start_x, start_y)
        self.direction_bullet = pygame.math.Vector2(self.direction, 0)
        self.flshoot = False
        self.key_shoot = key_shoot

    def shoot(self, direction, Tank):
        key = pygame.key.get_pressed()
        if key[self.key_shoot] and not self.flshoot:
            sound1.play()
            self.direction_bullet = pygame.math.Vector2(direction, 0)
            self.Bullet_rect.x = Tank.x
            self.Bullet_rect.y = Tank.y
            self.flshoot = True
        if self.flshoot:
            self.Bullet_rect += self.direction_bullet
            sc.blit(self.Bullet_surf, self.Bullet_rect)
            if self.Bullet_rect.x < 50 or self.Bullet_rect.x > 900 or self.Bullet_rect.y < 50 or self.Bullet_rect.y > 500:
                self.flshoot = False
                sound1.stop()


direction = pygame.math.Vector2(5, 0)


def main_area():
    pygame.draw.rect(sc, BLACK, [50, 50, 900, 500], 5)
    pygame.draw.rect(sc, BLACK, [350, 5, 300, 35])

    button_exit = pygame.font.SysFont('arial', 30)
    live1 = pygame.font.SysFont('arial', 30)
    live2 = pygame.font.SysFont('arial', 30)

    button_menu = button_exit.render(f"EXIT TO MENU", False, WHITE)
    text_live_1 = live1.render(f"live first tank: {Tank1.live_tank}", False, BLACK)
    text_live_2 = live2.render(f"live second tank: {Tank2.live_tank}", False, BLACK)
    sc.blit(button_menu, (420, 5))
    sc.blit(text_live_1, (50, 10))
    sc.blit(text_live_2, (735, 10))


def rules():
    rule1 = pygame.font.SysFont('arial', 30)
    text1 = rule1.render('Победа будет легендарной', False, BLACK)
    text2 = rule1.render('Если не ты победишь то враг', False, BLACK)
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLACK, [300, 100, 400, 370], 5)
    pygame.draw.rect(sc, BLACK, [350, 5, 300, 35])

    button_exit = pygame.font.SysFont('arial', 30)
    button_menu = button_exit.render(f"EXIT TO MENU", False, WHITE)
    sc.blit(button_menu, (420, 5))

    sc.blit(text1, (320, 120))
    sc.blit(text2, (320, 160))
    pygame.display.update()


wall1_1_surf = pygame.image.load('images\wall_1_1.jpg')
wall1_1_surf = pygame.transform.scale(wall1_1_surf, (wall1_1_surf.get_width(), wall1_1_surf.get_height()))
wall_2_surf = pygame.image.load('images\wall_2_1.jpg')
wall_2_surf = pygame.transform.scale(wall_2_surf, (wall_2_surf.get_width() // 4, wall_2_surf.get_height() // 4))
wall_2_rect = wall_2_surf.get_rect(center=(300, 300))
wall1_1_rect = wall1_1_surf.get_rect(center=(500, 400))


def walls():
    sc.blit(wall1_1_surf, wall1_1_rect)
    sc.blit(wall_2_surf, wall_2_rect)
    if wall1_1_rect.collidepoint(Bullet1.Bullet_rect.x, Bullet1.Bullet_rect.y) or wall_2_rect.collidepoint(
            Bullet1.Bullet_rect.x, Bullet1.Bullet_rect.y):
        Bullet1.flshoot = False


def ignore_wall():
    X = int(Tank1.Tank_rect.x)
    Y = int(Tank1.Tank_rect.y)
    for i in range(X - 20, X + 20):
        for j in range(Y - 20, Y + 20):
            if wall1_1_rect.collidepoint(i, j):
                return True
    return False


Tank1 = Tank_34("images/tank_1.jpg", 100, 100, pygame.K_SPACE)
Bullet1 = Bullet('images/bullet.jpg', 100, 100, direction, pygame.K_SPACE)
Tank2 = Tank_34('images/tank_2.jpg', 800, 100, pygame.K_e)
Bullet2 = Bullet('images/bullet.JPG', 800, 100, direction, pygame.K_e)


def control_area(flagmenu,flaggame,flagrules):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and \
                350 <= event.pos[0] <= 650 and 380 <= event.pos[1] <= 430 and \
                flagmenu:
            if event.button == 1:
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN and (flaggame or flagrules) and \
                350 <= event.pos[0] <= 650 and 5 <= event.pos[1] <= 40:
            if event.button == 1:
                flagmenu = True
                flagrules = False
                flaggame = False
        if event.type == pygame.MOUSEBUTTONDOWN and flagmenu and\
                350 <= event.pos[0] <= 650 and 140 <= event.pos[1] <= 190:
            if event.button == 1:
                flagmenu = False
                flaggame = True
        if event.type == pygame.MOUSEBUTTONDOWN and flagmenu and\
            350 <= event.pos[0] <= 650 and 300 <= event.pos[1] <= 350:
            if event.button == 1:
                flagrules = True
                flagmenu = False
    return flagmenu, flaggame, flagrules

flagrules = False
flagmenu = True
flaggame = False
while True:

    flagmenu, flaggame, flagrules = control_area(flagmenu, flaggame, flagrules)

    if flagmenu:
        mainmenu.Drawmenu(sc, FPS)
    elif flagrules:
        rules()
    else:
        sc.fill(WHITE)

        Tank1.move(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        Tank1.rotate_t()
        Tank2.move(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        Tank2.rotate_t()
        main_area()
        Bullet1.shoot(Tank1.direction, Tank1.Tank_rect)
        Bullet2.shoot(Tank2.direction, Tank2.Tank_rect)
        walls()

        pygame.display.update()
        clock.tick(FPS)
