import pygame
from drawfunctions import draw_surface, draw_rect, draw_circle, create_surface

pygame.init()

#Game info
name = "Doodle"
marginSize = 50
borderSize = 10
screenWidth = 500
screenHeight = 700
marginColor = (0,0,0)
borderColor = (0,0,150)
boardColor = (0,150,0)
ballColor = (150, 0, 0)
gameSpeed = 10
tileSize = 20
rowSize = 8
ballSize = tileSize // 2

clock = pygame.time.Clock()

win = create_surface(borderSize, marginSize, screenWidth, screenHeight)

def update_display(balls, frozen):
    draw_surface(win, marginSize, borderSize, screenWidth, screenHeight, marginColor, borderColor, boardColor)
    balls.draw()
    for i in frozen:
        i.draw()
    pygame.display.update()

class ball(object):
    def __init__(self, x, y, size, col):
        self.x = x
        self.y = y
        self.size = size
        self.col = col

    def draw(self):
        draw_circle(win, self.col, self.x, self.y, self.size)

class row(object):
    def __init__(self, balls):
        self.balls = balls

    def draw(self):
        for b in self.balls:
            b.draw()

run = True
incr = marginSize + borderSize
x_init = incr + ballSize
y_init = incr + screenHeight - ballSize
balls = []
frozen = []
loopVal = 2
spaceLoop = loopVal

for i in range(rowSize):
    balls.append(ball(x_init + (i*tileSize), y_init, ballSize, ballColor))

current_row = row(balls)
dir = 1

while run:

    clock.tick(gameSpeed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Maybe move this part up (check first)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and spaceLoop == loopVal:
        if frozen == []:
            prev_row = []

            for i in range(rowSize):
                prev_row.append(ball(balls[i].x, balls[i].y, balls[i].size, balls[i].col))

            frozen.append(row(prev_row))

            for b in balls:
                b.y -= tileSize
            spaceLoop = 0

        elif prev_row[rowSize-1].x < balls[0].x or prev_row[0].x > balls[rowSize-1].x:
            pass

        else:
            delIndex = []
            inRow = False
            for i in range(rowSize):
                for j in range(rowSize):
                    if balls[i].x == prev_row[j].x:
                        inRow = True

                if inRow == False:
                    delIndex.append(i)

                else:
                    inRow = False

            for i in reversed(delIndex):
                balls.pop(i)
            rowSize -= len(delIndex)


            prev_row = []

            for i in range(rowSize):
                prev_row.append(ball(balls[i].x, balls[i].y, balls[i].size, balls[i].col))

            frozen.append(row(prev_row))

            for b in balls:
                b.y -= tileSize
            spaceLoop = 0

    if balls[rowSize-1].x + ballSize == incr + screenWidth:
        dir = -1

    if balls[0].x - ballSize == incr:
        dir = 1

    for b in balls:
        b.x += dir*tileSize

    if spaceLoop < loopVal:
        spaceLoop += 1

    if rowSize == 1:
        print("You lost")

    update_display(current_row, frozen)
