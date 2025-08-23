import pygame

pygame.init()
pygame.display.set_caption("Shooting Rocket")
pygame.display.set_icon(pygame.image.load("rocket.png"))
screen_size = pygame.display.set_mode((800, 800))

player_image = pygame.image.load("rocket.png")
playerX = 368
playerY = 736
playerX_change = 0
#playerY_change = 0

enemy_image = pygame.image.load("rocket.png")
enemyX = 368
enemyY = 736
enemyX_change = 0

def player_draw(x,y):
    screen_size.blit(player_image, (x, y))

def enemy_draw(x,y):
    screen_size.blit(enemy_image, (x, y))

is_running = True
while True:
    screen_size.fill((60, 70, 110))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.1
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.1
            '''
            if event.key == pygame.K_UP:
                playerY_change -= 0.1
            if event.key == pygame.K_DOWN:
                playerY_change += 0.1
            '''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX += 0
            #if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #    playerY += 0
    playerX += playerX_change
    #playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player_draw(playerX, playerY)
    enemy_draw(enemyX, enemyY)
    pygame.display.update()