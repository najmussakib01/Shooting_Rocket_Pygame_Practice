import random
import pygame
import math

pygame.init()
default_screen_size = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Rocket Shooter")
pygame.display.set_icon(pygame.image.load("rocket.png"))
background_img = pygame.image.load("ultra-detailed-nebul..._imresizer.png")
###
player_image = pygame.image.load("rocket.png")
playerX = 368
playerY = 700
playerX_change = 0

enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6


for i in range(number_of_enemies):
    enemy_image.append(pygame.image.load("rocket.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(0.5)
    enemyY_change.append(50)

bullet_image = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 3
visible_bullet = False


score = 0
my_font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

def showscore(x, y):
    score_value = my_font.render("Score: " + str(score), True, (255, 255, 255))
    default_screen_size.blit(score_value, (x, y))

def player_draw(x,y):
    default_screen_size.blit(player_image, (x, y))

def enemy_draw(x,y, en):
    default_screen_size.blit(enemy_image[en], (x, y))

def fire_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    default_screen_size.blit(bullet_image, (x +16 , y + 10))


def there_is_collision(eX, eY, bX, bY):
    coll_distance = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    if coll_distance < 27:
        return True
    else:
        return False

def final_score():
    my_final_font = my_font.render("GAME OVER", True, (255, 255, 255))
    default_screen_size.blit(my_final_font, (200, 200))


is_running = True
while True:
    default_screen_size.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 1
            if event.key == pygame.K_RIGHT:
                playerX_change += 1
            if event.key == pygame.K_SPACE:
                if not visible_bullet:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            '''
            if event.key == pygame.K_UP:
                playerY_change -= 0.1
            if event.key == pygame.K_DOWN:
                playerY_change += 0.1
            '''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX += 0


    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #enemyX += enemyX_change
    for enem in range(number_of_enemies):
        if enemyY[enem] > 500:
            for k in range(number_of_enemies):
                enemyY[k] = 1000
            final_score()
            break

        if enemyY[enem] > 500:
            for j in range(number_of_enemies):
                enemyY[j] = 1000
            break
        enemyX[enem] += enemyX_change[enem]
        if enemyX[enem] <= 0:
            enemyX_change [enem]= 1
            enemyY[enem] += enemyY_change[enem]
        elif enemyX[enem] >= 736:
            enemyX_change[enem] = -1
            enemyY[enem] += enemyY_change[enem]


        collision = there_is_collision(enemyX[enem], enemyY[enem], bulletX, bulletY)
        if collision:
            bulletY = 500
            visible_bullet = False
            score += 1
            print(score)
            enemyX[enem] = random.randint(0, 736)
            enemyY[enem] = random.randint(50, 200)

        enemy_draw(enemyX[enem], enemyY[enem], enem)



    if bulletY <= -64:
        bulletY = 500
        visible_bullet = False
    if visible_bullet:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player_draw(playerX, playerY)

    showscore( textX, textY)
    pygame.display.update()