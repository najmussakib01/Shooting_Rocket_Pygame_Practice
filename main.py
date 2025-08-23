import pygame

pygame.init()
pygame.display.set_caption("Shooting Rocket")
pygame.display.set_icon(pygame.image.load("rocket.png"))
screen_size = pygame.display.set_mode((800, 800))

player_image = pygame.image.load("rocket.png")
playerX = 368
playerY = 736

def player_draw():
    screen_size.blit(player_image, (playerX, playerY))

is_running = True
while True:
    screen_size.fill((60, 70, 110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    player_draw()
    pygame.display.update()