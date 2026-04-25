import pymunk
import time
import pygame
import random
import threading

#Python yells at me if I don't put anything in the functions so this is a placeholder if needed
TestDud = "REPLACE ME"

#constants and globals
score1=0
score2=0
playermove = 0.075
done = False

#timers
def gametimer(seconds):
    TestDud


#collisions
COLLTYPE_LEFT = 1
COLLTYPE_RIGHT = 2
COLLTYPE_BULLET = 3
COLLTYPE_PLAYER = 4
COLLTYPE_OBSTACLE = 5
# PLAYER FUNCTIONS

#Player 1 Mover
def MovePlayer1(body, shape, left, right, up, down):
    deltaX = 0
    deltaY = 0
    pos = body.position
    if left:
        deltaX = deltaX - playermove
    if right:
        deltaX = deltaX + playermove
    if up:
        deltaY = deltaY + playermove
    if down:
        deltaY = deltaY - playermove
    bounds = shape.bb
    width = bounds.right - bounds.left
    height = bounds.bottom - bounds.top
    newX = pos.x+deltaX
#    newX = max(newX, width/2+20)
#    newX = min(newX, 780-width/2)
    newY = pos.y + deltaY
#    newY = max(newY, height/2+20)
#    newY = min(newY, 780-height/2)
    body.position = (newX, newY)

def MovePlayer2(body, shape, left, right, up, down):
    deltaX = 0
    deltaY = 0
    pos = body.position
    if left:
        deltaX = deltaX - playermove
    if right:
        deltaX = deltaX + playermove
    if up:
        deltaY = deltaY + playermove
    if down:
        deltaY = deltaY - playermove
    bounds = shape.bb
    width = bounds.right - bounds.left
    height = bounds.bottom - bounds.top
    newX = pos.x+deltaX
#    newX = max(newX, width/2+20)
#    newX = min(newX, 780-width/2)
    newY = pos.y + deltaY
#    newY = max(newY, height/2+20)
#    newY = min(newY, 780-height/2)
    body.position = (newX, newY)



# round structuring

#initializing the game
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
space = pymunk.Space()
space.gravity = (0, 0)
# load font
font = pygame.font.SysFont('Arial', 30)

#player creation
circleBody1 = pymunk.Body( 1, 100)
circleBody1.position = (100, 300)
circleShape1 = pymunk.Circle(circleBody1, 10)
circleShape1.filter = pymunk.ShapeFilter(group=1)
space.add(circleBody1, circleShape1)


circleBody2 = pymunk.Body( 1, 100)
circleBody2.position = (500, 300)
circleShape2 = pymunk.Circle(circleBody2, 10)
circleShape2.filter = pymunk.ShapeFilter(group=2)
space.add(circleBody2, circleShape2)

#bullet creations
def fireLeftBullet(gameSpace,player_body):
    bulletSpawnX = player_body.position.x + 35
    bulletSpawnY = player_body.position.y
    bulletMass = 1
    bulletMoment = pymunk.moment_for_circle(bulletMass,0,5)
    bulletBody = pymunk.Body(bulletMass, bulletMoment)
    spawnDistance = 35
    bulletBody.position = (bulletSpawnX + spawnDistance, bulletSpawnY)
    bulletShape = pymunk.Circle(bulletBody, 5)
    bulletShape.friction = 0
    bulletShape.filter = (pymunk.ShapeFilter(group=1))

    gameSpace.add(bulletBody, bulletShape)
    bulletBody.velocity = (5, 0)

    return bulletBody

def fireRightBullet(gameSpace,player_body):
    bulletSpawnX = player_body.position.x - 35
    bulletSpawnY = player_body.position.y
    bulletMass = 1
    bulletMoment = pymunk.moment_for_circle(bulletMass,0,5)
    bulletBody = pymunk.Body(bulletMass, bulletMoment)
    spawnDistance = 35
    bulletBody.position = (bulletSpawnX + spawnDistance, bulletSpawnY)
    bulletShape = pymunk.Circle(bulletBody, 5)
    bulletShape.friction = 0
    bulletShape.filter = (pymunk.ShapeFilter(group=2))


    gameSpace.add(bulletBody, bulletShape)
    bulletBody.velocity = (-5, 0)

    return bulletBody

bullets1 = []
bullets2 = []
#Game Loop
leftArrowDown = False
rightArrowDown = False
upArrowDown = False
downArrowDown = False
AKeyDown = False
DKeyDown = False
WKeyDown = False
SKeyDown = False
#LeftShiftDown = False
RightShiftDown = False

roundActive = False
ammo1 = 6
ammo2 = 6

out_of_ammo1 = False
out_of_ammo2 = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftArrowDown = True
            if event.key == pygame.K_a:
                AKeyDown = True
            if event.key == pygame.K_RIGHT:
                rightArrowDown = True
            if event.key == pygame.K_d:
                DKeyDown = True
            if event.key == pygame.K_UP:
                upArrowDown = True
            if event.key == pygame.K_w:
                WKeyDown = True
            if event.key == pygame.K_DOWN:
                downArrowDown = True
            if event.key == pygame.K_s:
                SKeyDown = True
            if event.key == pygame.K_LSHIFT:
                if out_of_ammo1 == False:
                    newBullet = fireLeftBullet(space, circleBody1)
                    bullets1.append(newBullet)
                    ammo1 = ammo1 - 1
            if event.key == pygame.K_RSHIFT:
                if out_of_ammo2 == False:
                    newBullet = fireRightBullet(space, circleBody2)
                    bullets2.append(newBullet)
                    ammo2 = ammo2 - 1
            if event.key == pygame.K_RSHIFT:
                RightShiftDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftArrowDown = False
            if event.key == pygame.K_a:
                AKeyDown = False
            if event.key == pygame.K_RIGHT:
                rightArrowDown = False
            if event.key == pygame.K_d:
                DKeyDown = False
            if event.key == pygame.K_UP:
                upArrowDown = False
            if event.key == pygame.K_w:
                WKeyDown = False
            if event.key == pygame.K_DOWN:
                downArrowDown = False
            if event.key == pygame.K_s:
                SKeyDown = False



    MovePlayer1(circleBody1, circleShape1, leftArrowDown, rightArrowDown, downArrowDown, upArrowDown)
    space.step(1 / 60.0)
    screen.fill((0, 0, 0))
    circle1X = int(circleBody1.position.x)
    circle1Y = int(circleBody1.position.y)
    pygame.draw.circle(screen, (255, 255, 255), (circle1X, circle1Y), 10)
    MovePlayer2(circleBody2, circleShape2, AKeyDown, DKeyDown, SKeyDown, WKeyDown)
    circle2X = int(circleBody2.position.x)
    circle2Y = int(circleBody2.position.y)
    pygame.draw.circle(screen, (255, 255, 255), (circle2X, circle2Y), 10)

    for bullet in bullets1:
        pos = bullet.position
        pygame.draw.circle(screen, (255, 0, 0), (int(pos.x), int(pos.y)), 10)
    for bullet in bullets2:
        pos = bullet.position
        pygame.draw.circle(screen, (255, 0, 0), (int(pos.x), int(pos.y)), 10)
    pygame.display.update()

    if ammo1 <= 0:
        out_of_ammo1 = True
    if ammo2 <= 0:
        out_of_ammo2 = True

