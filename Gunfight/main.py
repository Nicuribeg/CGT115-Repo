import pymunk
import time
import pygame
import random


#constants and globals
score_1=0
score_2=0
playermove = 0.075
done = False
game_timer_duration = 60
start_position_p1 = (100,300)
start_position_p2 = (700,300)


timer_active = False
timer_end_time = 0
timer_started = False
timer_has_run = False

round_reset_pending = False
reset_delay = 0
reset_timer_start = 0

game_duration = 60
game_timer_start = 0
game_timer_active = False
game_over = False
winner_message = ""

#timers
def roundtimer():
    global timer_active
    global timer_start_time
    global timer_started
    global round_reset_pending
    global reset_timer_start

    if timer_started and timer_active:
        current_time = time.time()
        remaining = timer_start_time - current_time

        if remaining > 0:
            timer_text = font.render(f"{remaining:.1f}", True, (255, 0, 0))
            screen.blit(timer_text, (350, 250))
        else:
            timer_active = False
            timer_started = False

            round_reset_pending = True
            reset_timer_start = time.time()



#collisions
COLLTYPE_BULLET = 1
COLLTYPE_PLAYER = 2
COLLTYPE_OBSTACLE = 3

CAT_PLAYER = 0x0001
CAT_BULLET = 0x0002


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

    newX = pos.x + deltaX
    newY = pos.y + deltaY

    newX = max(newX, 10)
    newX = min(newX, 220)

    newY = max(newY, 10)
    newY = min(newY, 590)

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

    newX = pos.x + deltaX
    newY = pos.y + deltaY

    newX = max(newX, 580)
    newX = min(newX, 790)

    newY = max(newY, 10)
    newY = min(newY, 590)

    body.position = (newX, newY)


# obstacle creations
obstacles = []


def create_static_obstacles():
    global obstacles

    for body, shape in obstacles:
        space.remove(shape, body)
    obstacles = []

    for _ in range(3):
        x = random.randint(300, 450)
        y = random.randint(40, 740)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (x, y)

        shape = pymunk.Poly.create_box(body, (50, 50))
        shape.collision_type = COLLTYPE_OBSTACLE
        shape.filter = pymunk.ShapeFilter(categories=CAT_PLAYER, mask=CAT_BULLET)

        space.add(body, shape)
        obstacles.append((body, shape))

# round structuring

#initializing the game
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
space = pymunk.Space()
create_static_obstacles()
space.gravity = (0, 0)
# load font
font = pygame.font.SysFont('Arial', 30)
game_timer_start = time.time()
game_timer_active = True

#player creation
circle_body_1 = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
circle_body_1.position = (100, 300)
circle_shape_1 = pymunk.Circle(circle_body_1, 10)
circle_shape_1.collision_type = COLLTYPE_PLAYER
circle_shape_1.filter = pymunk.ShapeFilter(categories=CAT_PLAYER, mask=CAT_BULLET)
space.add(circle_body_1, circle_shape_1)


circle_body_2 = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
circle_body_2.position = (700, 300)
circle_shape_2 = pymunk.Circle(circle_body_2, 10)
circle_shape_2.collision_type = COLLTYPE_PLAYER
circle_shape_2.filter = pymunk.ShapeFilter(categories=CAT_PLAYER, mask=CAT_BULLET)
space.add(circle_body_2, circle_shape_2)




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
    bulletShape.collision_type = COLLTYPE_BULLET
    bulletShape.friction = 0
    bulletShape.filter = pymunk.ShapeFilter(categories=CAT_BULLET, mask=CAT_PLAYER)

    gameSpace.add(bulletBody, bulletShape)
    bulletBody.velocity = (25, 0)

    return bulletBody

def fireRightBullet(gameSpace,player_body):
    bulletSpawnX = player_body.position.x - 35
    bulletSpawnY = player_body.position.y
    bulletMass = 1
    bulletMoment = pymunk.moment_for_circle(bulletMass,0,5)
    bulletBody = pymunk.Body(bulletMass, bulletMoment)
    spawnDistance = 35
    bulletBody.position = (bulletSpawnX - spawnDistance, bulletSpawnY)
    bulletShape = pymunk.Circle(bulletBody, 5)
    bulletShape.collision_type = COLLTYPE_BULLET
    bulletShape.friction = 0
    bulletShape.filter = pymunk.ShapeFilter(categories=CAT_BULLET, mask=CAT_PLAYER)


    gameSpace.add(bulletBody, bulletShape)
    bulletBody.velocity = (-25, 0)

    return bulletBody

#Bullet Collisions


def remove_bullet(arbiter, space, data):
    bullet_shape = arbiter.shapes[0]
    player_shape = arbiter.shapes[1]
    bullet_body = bullet_shape.body
    shape_a, shape_b = arbiter.shapes

    if shape_a.collision_type == COLLTYPE_BULLET:
        bullet_shape = shape_a
        player_shape = shape_b
    else:
        bullet_shape = shape_b
        player_shape = shape_a


    space.remove(bullet_shape, bullet_shape.body)


    global score_1
    global score_2
    if player_shape.body == circle_body_1:
        score_1 += 1
    elif player_shape.body == circle_body_2:
        score_2 += 1
    if bullet_body in bullets_1:
        bullets_1.remove(bullet_body)
    elif bullet_body in bullets_2:
        bullets_2.remove(bullet_body)

    global round_reset_pending, reset_timer_start
    round_reset_pending = True
    reset_timer_start = time.time()

    return True

handler = space.add_collision_handler(COLLTYPE_BULLET, COLLTYPE_PLAYER)
handler.post_solve = remove_bullet

bullets_1 = []
bullets_2 = []

def remove_bullet_from_obstacle(arbiter, space, data):
    bullet_shape = None
    obstacle_shape = None

    for shape in arbiter.shapes:
        if shape.collision_type == COLLTYPE_BULLET:
            bullet_shape = shape
        elif shape.collision_type == COLLTYPE_OBSTACLE:
            obstacle_shape = shape

    if bullet_shape:
        bullet_body = bullet_shape.body
        space.remove(bullet_shape, bullet_body)

        if bullet_body in bullets_1:
            bullets_1.remove(bullet_body)
        elif bullet_body in bullets_2:
            bullets_2.remove(bullet_body)

    return True

obstacle_handler = space.add_collision_handler(COLLTYPE_BULLET, COLLTYPE_OBSTACLE)
obstacle_handler.post_solve = remove_bullet_from_obstacle

#Game Loop
leftArrowDown = False
rightArrowDown = False
upArrowDown = False
downArrowDown = False
AKeyDown = False
DKeyDown = False
WKeyDown = False
SKeyDown = False

roundActive = False
ammo_1 = 10
ammo_2 = 10

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
                    newBullet = fireLeftBullet(space, circle_body_1)
                    bullets_1.append(newBullet)
                    ammo_1 = ammo_1 - 1
            if event.key == pygame.K_RSHIFT:
                if out_of_ammo2 == False:
                    newBullet = fireRightBullet(space, circle_body_2)
                    bullets_2.append(newBullet)
                    ammo_2 = ammo_2 - 1
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



    #Initializes movement and draws players
    MovePlayer1(circle_body_1, circle_shape_1, AKeyDown, DKeyDown, SKeyDown, WKeyDown)
    space.step(1 / 60.0)
    screen.fill((0, 0, 0))
    circle1X = int(circle_body_1.position.x)
    circle1Y = int(circle_body_1.position.y)
    pygame.draw.circle(screen, (255, 255, 255), (circle1X, circle1Y), 10)
    MovePlayer2(circle_body_2, circle_shape_2, leftArrowDown, rightArrowDown, downArrowDown, upArrowDown)
    circle2X = int(circle_body_2.position.x)
    circle2Y = int(circle_body_2.position.y)
    pygame.draw.circle(screen, (255, 255, 255), (circle2X, circle2Y), 10)

    #Draws Obstacles
    for body, shape in obstacles:
        x = int(body.position.x)
        y = int(body.position.y)
        pygame.draw.rect(screen, (255,0,0) ,(x-25,y-25,50,50))

    #Draws bullets for each player
    for bullet in bullets_1:
        pos = bullet.position
        pygame.draw.circle(screen, (255, 0, 0), (int(pos.x), int(pos.y)), 10)
    for bullet in bullets_2:
        pos = bullet.position
        pygame.draw.circle(screen, (255, 0, 0), (int(pos.x), int(pos.y)), 10)
    ammo_text1 = font.render(f"P1 Ammo: {ammo_1}", True, (255, 255, 255))
    ammo_text2 = font.render(f"P2 Ammo: {ammo_2}", True, (255, 255, 255))
    score_text1 = font.render(f"{score_1}", True, (255, 255, 255))
    score_text2 = font.render(f"{score_2}", True, (255, 255, 255))
    screen.blit(ammo_text1, (10, 550))
    screen.blit(ammo_text2, (650, 550))
    screen.blit(score_text1, (50, 20))
    screen.blit(score_text2, (750, 20))

    roundtimer()

    #Starts round timer when either player runs out of ammo
    if (ammo_1 <= 0 or ammo_2 <= 0) and not timer_active and not timer_has_run:
        timer_active = True
        timer_started = True
        timer_start_time = time.time() + 10
        timer_has_run = True

    if ammo_1 <= 0:
        out_of_ammo1 = True
    if ammo_2 <= 0:
        out_of_ammo2 = True

    #Function that resets the round
    def reset_round():
        global round_reset_pending, score_1, score_2
        global bullets_1, bullets_2


        circle_body_1.position = start_position_p1
        circle_body_2.position = start_position_p2

        for shape in list(space.shapes):
            if shape.collision_type == COLLTYPE_BULLET:
                body = shape.body
                space.remove(shape, body)

        bullets_1.clear()
        bullets_2.clear()

        global ammo_1
        global ammo_2
        global out_of_ammo1
        global out_of_ammo2
        ammo_1 = 10
        ammo_2 = 10
        out_of_ammo1 = False
        out_of_ammo2 = False

        global timer_active
        global timer_started
        global timer_has_run
        timer_active = False
        timer_started = False
        timer_has_run = False

        create_static_obstacles()


    if round_reset_pending:
        current_time = time.time()
        if current_time - reset_timer_start >= reset_delay:
            reset_round()
            round_reset_pending = False

    if game_timer_active and not game_over:
        current_time = time.time()
        elapsed = current_time - game_timer_start
        remaining = game_duration - elapsed

        if remaining > 0:
            timer_text = font.render(f"{remaining:.1f}", True, (255, 255, 255))
            screen.blit(timer_text, (400, 10))  # Center top
        else:
            round_timer_active = False
            game_over = True
            if score_1 > score_2:
                winner_message = f"P1 Wins"
            elif score_2 > score_1:
                winner_message = f"P2 Wins"
            else:
                winner_message = f"It's a Draw"

            print("Game Over. " + winner_message)

        if game_over:
            overlay = pygame.Surface((800, 600))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            win_font = pygame.font.SysFont('Arial', 50, bold=True)
            win_text = win_font.render(winner_message, True, (255, 255, 0))
            text_rect = win_text.get_rect(center=(400, 300))
            screen.blit(win_text, text_rect)

            pygame.display.update()
            time.sleep(2)
            done == True

        pygame.display.update()