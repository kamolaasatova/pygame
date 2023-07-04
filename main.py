import pygame
class Sprite:
    def __init__(self, x, y, speed, img):
        self.image = pygame.image.load(img).convert_alpha()
        self.speed = speed
        self.x = x
        self.y = y
        self.imgR = self.image
        self.imgL = pygame.transform.flip(self.image, True, False)


    def cords(self):
        return tuple([self.x, self.y])

    def move(self, side):
        if side == 'right':
            self.image = self.imgR
            self.x +=self.speed
        elif side == 'left':
            self.image = self.imgL
            self.x -= self.speed
        elif side == 'up':
            self.y -= self.speed
        elif side.y == 'down':
            self.y += self.speed


w = pygame.display.set_mode((1270, 700))
Player = Sprite(100, 100, 1, 'ss.png')
game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Player.move('right')
    if keys[pygame.K_LEFT]:
        Player.move('left')
    w.fill((0, 0, 0))
    w.blit(Player.image, Player.cords())
    pygame.display.update()
pygame.quit()
