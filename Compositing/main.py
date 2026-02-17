import pygame

# Initialize the game
pygame.init()

pygame.display.set_caption("Hello World")

img = pygame.image.load("images1/prague.png")
img2 = pygame.image.load("images1/characters/yoda.png")

width = img.get_width()
height = img.get_height()
screen = pygame.display.set_mode((width, height))
greenscreen = img2.get_at((0,0))
for y in range(0, height):
    for x in range(0, width):
        c1 = img.get_at((x, y))
        c2 = img2.get_at((x, y))
        if img2.get_at((x,y)) == greenscreen:
            img2.set_at((x, y,),c1)
        else:
            img2.set_at((x, y), c2)




screen.blit(img2, (0, 0) )

pygame.display.flip()

pygame.image.save(img2, "BW.png")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
