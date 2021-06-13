#import of Modules
import pygame
import random
import math

#initialize all imported pygame modules
pygame.init()

#Display
screen = pygame.display.set_mode((800, 600))

#CAPTION
pygame.display.set_caption("Sprzedaj Futro")

#ICON
icon = pygame.image.load('leather.png')
pygame.display.set_icon(icon)

#PlayerIMG 
playerIMG = pygame.image.load('dwarf.png')

#Starting positon of player 
playerX = 370
playerY = 480

#position variable used in motion
playerX_change = 0

#score var
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
def show_score(x,y):
    score_ren = font.render("wynik :"+ str(score),True, (255,255,255))
    screen.blit(score_ren, (x, y))

#Displays the player on the screen in the correct coordinates
def player(x,y):

    screen.blit(playerIMG, (x, y))

#EnemyIMG
enemyIMG = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change =[]
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('merchant.png'))
    #Starting positon of enemy
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 51))
    #initial speed (then changes when it hits walls) X axis
    enemyX_change.append(0.3)
    #change of position in the Y axis
    enemyY_change.append(30)

#displaying the opponent on the given coordinates
def enemy(x,y, i):

    screen.blit(enemyIMG[i], (x, y))

#BulletIMG
attacIMG = pygame.image.load('skora.png.png')
#projectile coordinates
bulletX = 0
BulletY = 480

#speed of the bullet 
BulletY_change = 0.3 

#ENG =("bullet status") 
#rdy = bullet is redy to get display 
#fire = bullet is alredy on te screen we cant shot the another one
 
status_bullet = "rdy"  

#ENG =("Projectile shot displayed")
def Fire_bullet(x,y):

    global status_bullet
    status_bullet = "fire"
    screen.blit(attacIMG,(x+16,y+10))

def IsCollision(enemyX,enemyY,bulletX,BulletY):

    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-BulletY,2)))

    if distance <27:
        return True
    else:
        return False

#mechanizm zamykania oraz gry
done = False
while not done:
        #RGB 0-255
    screen.fill((30,100,20))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        # jeśli klawisz jest wciśnięty sprawdza czy to jest prawa lub lewa
        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_a: #wciskamy A i zmieniemy wartość poruszania sie gracza 
                playerX_change = -0.2

            if event.key == pygame.K_d: #wciskamy D i zmieniemy wartość poruszania sie gracza
                playerX_change = 0.2

            if event.key == pygame.K_SPACE:

                if status_bullet is "rdy":
                    #właściwe kordynaty
                    bulletX = playerX
                    Fire_bullet(bulletX,BulletY)

        if event.type == pygame.KEYUP: #odklikujemy przycisk i tymsamym zmieniamy wartość poruszania się gracza na 0 

            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    #obiekt gracza
    playerX += playerX_change 
    player(playerX, playerY)

    if playerX<=0:
        playerX = 0

    elif playerX >=736:
        playerX = 736

    #enemy
    
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0:
            enemyX[i] = 0
            enemyX_change[i] = random.uniform(0.15, 0.2)
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX[i] = 736
            enemyX_change[i] = random.uniform(-0.2, -0.15)
            enemyY[i] += enemyY_change[i]

        Collision = IsCollision(enemyX[i], enemyY[i], bulletX, BulletY)
        if Collision:

            BulletY = 480
            status_bullet = "rdy"
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 51)

        enemy(enemyX[i], enemyY[i], i)

    #strzal przemieszczaniesie 
    if BulletY <=0:
        BulletY=480
        status_bullet="rdy"

    if status_bullet is "fire":

        Fire_bullet(bulletX, BulletY)
        BulletY -= BulletY_change

    #Collision



    #Update portions of the screen for software displays 
    show_score(textX, textY)
    pygame.display.update() 