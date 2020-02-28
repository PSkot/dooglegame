import pygame
import numpy as np
from drawfunctions import collision, draw_circle, draw_rect, create_surface, draw_surface

#Game info
name = "Pacman"
borderSize = 0
marginSize = 100
screenWidth = 500
screenHeight = 600
marginColor = (0,0,0)
borderColor = (0,0,200)
boardColor = (0,0,0)
gameSpeed = 80
tileSize = 10
charSize = 45
wallFill = 10
wallBorder = 2

clock = pygame.time.Clock()
pm1 = pygame.image.load('Pacman1.png')
pm1 = pygame.transform.scale(pm1, (charSize, charSize))

#Create surface
win = create_surface(borderSize, marginSize, screenWidth, screenHeight)

#Draw surface
def update_display(pacman, map):
    draw_surface(win, marginSize, borderSize, screenWidth, screenHeight, marginColor, borderColor, boardColor)
    map.drawMap(win, wallFill, wallBorder)
    pacman.draw(win)
    pygame.display.update()

def getWalls(mapNum, border, margin):
    incr = border + margin

    if mapNum == 1:
        walls = [
                #Border
                (incr, incr, screenWidth, wallBorder), #Outer upper
                (incr + wallFill + wallBorder, incr + wallFill + wallBorder, screenWidth - wallFill * 2 - wallBorder, wallBorder), #Inner upper
                (incr, incr, wallBorder, screenHeight + wallBorder), #Outer left
                (incr + wallFill + wallBorder, incr + wallFill + wallBorder, wallBorder, screenHeight - wallFill * 2 - wallBorder), #Inner left
                (incr + screenWidth, incr, wallBorder, screenHeight + wallBorder), #Outer right
                (incr + screenWidth - wallFill - wallBorder, incr + wallFill + wallBorder, wallBorder, screenHeight - wallFill*2 - wallBorder), #Inner right
                (incr, incr + screenHeight, screenWidth, wallBorder), #Inner upper
                (incr + wallFill + wallBorder, incr + screenHeight - wallFill - wallBorder, screenWidth - wallFill * 2 - wallBorder, wallBorder) #Inner lower


            ]
        #Inner map
        for i in range(10):
            walls.append((incr + wallFill + wallBorder + charSize, incr + wallFill*(i+1) + wallBorder + charSize*(i+1), screenWidth - wallFill * 2 - wallBorder - charSize * 2, wallBorder))
            walls.append((incr + wallFill + wallBorder + charSize, incr + wallFill*(i+2) + wallBorder + charSize*(i+1), screenWidth - wallFill * 2 - wallBorder - charSize * 2, wallBorder))
            walls.append((incr + wallFill + wallBorder + charSize, incr + wallFill*(i+1) + wallBorder + charSize*(i+1), wallBorder, wallBorder + wallFill))
            walls.append((incr + screenWidth - charSize - wallFill - wallBorder, incr + wallFill*(i+1) + wallBorder + charSize*(i+1), wallBorder, wallBorder + wallFill))

    else:
        walls = []

    return walls

class map(object):
    def __init__(self, mapNum):
        self.mapNum = mapNum

    def drawMap(self, win, wallFill, wallBorder):
        walls = getWalls(self.mapNum, borderSize, marginSize)

        for i in walls:
            pygame.draw.rect(win, borderColor, i)

class gate(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

class wall(object):
    def __init__(self, x, y, border, width, height):
        self.x = x
        self.y = y
        self.border = border
        self.width = width
        self.height = height

    def draw(self, win):
        pass

class pacman(object):
    def __init__(self, x, y, img, size, vertical, horizontal):
        self.x = x
        self.y = y
        self.img = img
        self.size = size
        self.vertical = vertical
        self.horizontal = horizontal

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

class ghost(object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def draw(self):
        if self.state == 'aggressive':
            # Logic for being aggressive
            pass

        elif self.state == 'passive':
            # logic for being victim of Pacman
            pass

class candy(object):
    pass

class orb(object):
    pass

run = True
pacman = pacman(250, 250, pm1, charSize, 0, 0)
ghosts = []
vel = 1
map = map(1)
walls = getWalls(map.mapNum, borderSize, marginSize)
wallUp = False
wallDown = False
wallRight = False
wallLeft = False

while run:
    clock.tick(gameSpeed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    wallUp = False
    wallDown = False
    wallRight = False
    wallLeft = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        pacman.vertical = 1

    if keys[pygame.K_UP]:
        pacman.vertical = -1

    if keys[pygame.K_LEFT]:
        pacman.horizontal = -1

    if keys[pygame.K_RIGHT]:
        pacman.horizontal = 1


    for i in walls:
        if pacman.y == i[1] + wallBorder and pacman.x + charSize > i[0] + wallBorder and pacman.x < i[0] + i[2]:
            wallUp = True

        if pacman.y + charSize == i[1] + wallBorder and pacman.x + charSize > i[0] and pacman.x < i[0] + i[2] - wallBorder:
            wallDown = True

        if pacman.x == i[0] and pacman.y + charSize > i[1] and pacman.y < i[1] + i[3] - wallBorder:
            wallLeft = True

        if pacman.x + charSize == i[0] and pacman.y + charSize > i[1] and pacman.y < i[1] + i[3] - wallBorder:
            wallRight = True

    if wallUp == False and pacman.vertical == -1:
        pacman.y += vel*pacman.vertical

    if wallDown == False and pacman.vertical == 1:
        pacman.y += vel*pacman.vertical

    if wallLeft == False and pacman.horizontal == -1:
        pacman.x += vel*pacman.horizontal

    if wallRight == False and pacman.horizontal == 1:
        pacman.x += vel*pacman.horizontal

    update_display(pacman, map)
