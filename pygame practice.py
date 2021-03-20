import pygame,sys,random

width = 800
height = 800
screen = pygame.display.set_mode ((width,height))
pygame.display.set_caption("minigame")

cyan=(0,255,255)
brown = (156,102,31)
Blue = (152,245,255)
white = (248,248,255)
brick = (210,105,30 )
gray =(128,138,135)
black = (0,0,0)
yellow=(255,246,143)
green=(69,139,0)
purple=(160,32,240)
red=(255,0,0)
orange = (255,100,10)
green = 0
red = 0
blue = 0
rectx = 400
rect_change_x = 0
recty = 400
rect_change_y = 0
right_down = False
left_down = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_change_x += 10
                right_down = True
            if right_down:
                print("hello")
                rect_change_x += 2
            if event.key == pygame.K_LEFT:
                rect_change_x = -2
                left_down = True
            if event.key == pygame.K_UP:
                rect_change_y = -1
            if event.key == pygame.K_DOWN:
                rect_change_y = 1
            if event.key == pygame.K_SPACE:
                red = random.randrange(0,255)
                blue = random.randrange(0, 255)
                green = random.randrange(0, 255)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_down = False


            """
            if not right_down and not left_down:
                rect_change_x = 0
            elif right_down and left_down and event.key == pygame.K_RIGHT:
                rect_change_x = -1
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
            """
            """
            if not right_down and not left_down:
                rect_change_x = 0
            elif left_down and right_down and event.key == pygame.K_LEFT:
                rect_change_x = 1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                rect_change_x = 0
            """
    rect_change_x *= 0.9
    print(rectx)
    rectx += rect_change_x
    recty += rect_change_y
    screen.fill(black)
    pygame.draw.rect(screen, (blue,green,red), (rectx, recty, 20, 20))
    pygame.display.update()