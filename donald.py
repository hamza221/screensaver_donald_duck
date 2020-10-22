import sys, pygame
pygame.init()

size = width, height = 1920, 1080
speed = [2,2]
white = 255, 255, 255

screen = pygame.display.set_mode(size)
colors =[	(255,0,0),(255,99,71),	(255,127,80),(205,92,92),(0,255,255),(0,128,128)]

ball=pygame.image.load("donald.png")
ballrect = ball.get_rect()
i =0
while 1:
    if i==6:
        i=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        white=colors[i]
        i=i+1
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        white=colors[i]
        i=i+1
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()