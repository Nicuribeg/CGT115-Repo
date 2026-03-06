import pygame
import pymunk

#this initializes pygame and pymunk
pygame.init()
screen = pygame.display.set_mode((800, 600))
space = pymunk.Space()
space.gravity= (0,0.01)

body = pymunk.body.Body(1,1)
ball = pymunk.Circle(body, 10, (0, 0))
body.position = (250, 100)
space.add(body, ball)

# This creates the ramp
line1Body = pymunk.Body(body_type=pymunk.Body.STATIC)
line1 = pymunk.Segment(line1Body, (200, 200), (300, 300), 2)
space.add(line1,line1Body)

#this creates the second ramp
line2Body = pymunk.Body(body_type=pymunk.Body.STATIC)
line2 = pymunk.Segment(line2Body, (310, 400), (375, 275), 2)
space.add(line2,line2Body)

#this creates the third line
line3Body = pymunk.Body(body_type=pymunk.Body.STATIC)
line3 = pymunk.Segment(line3Body, (175, 400), (375, 500), 2)
space.add(line3,line3Body)

#This is the game loop
done = False
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
    screen.fill((0, 0, 0))
    space.step(1/10.0)
    pygame.draw.circle(screen, (255, 255, 255), body.position, 10)
    # this draws the three ramps
    pygame.draw.line(screen,(255, 255, 255), line1.a, line1.b, 2)
    pygame.draw.line(screen,(255, 255, 255), line2.a, line2.b, 2)
    pygame.draw.line(screen,(255, 255, 255), line3.a, line3.b, 2)
    pygame.display.update()
