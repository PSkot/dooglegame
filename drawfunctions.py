#### Module for easily drawing basic pygame objects ####

#Import libraries
import pygame
import numpy as np

pygame.init()


### Drawing functions ###
def create_surface(marginSize = 0, borderSize = 0, screenWidth = 100, screenHeight = 100):
    return pygame.display.set_mode((marginSize*2+borderSize*2+screenWidth, marginSize*2+borderSize*2+screenHeight))

def draw_surface(win, marginSize = 50, borderSize = 10, screenWidth = 500, screenHeight = 500, marginColor = (0,0,0), borderColor = (0,0,0), boardColor = (0,0,0), blit = False):
    if blit == True:
        pass
    else:
        win.fill(marginColor)
        pygame.draw.rect(win, borderColor, (marginSize, marginSize, borderSize*2 + screenWidth, borderSize*2 + screenHeight))
        pygame.draw.rect(win, boardColor, (marginSize+borderSize, marginSize + borderSize, screenWidth, screenHeight))


def draw_circle(win, col, x, y, radius):
    pygame.draw.circle(win, (col), (x, y), radius)

def draw_rect(win, col, x, y, len, wid):
    pygame.draw.rect(win, col, (x, y, len, wid))

### Collission ###
def collision(x1, y1, x2, y2, object1Type = 'circle', object2Type = 'circle', object1Dimensions = (), object2Dimensions = ()):
    if object1Type == 'circle':
        if object2Type == 'circle':
            distX = x1 - x2
            distY = y1 - y2
            distance = np.sqrt((distX*distX) + (distY * distY))
            if distance < object1Dimensions + object2Dimensions:
                return True
            else:
                return False

        if object2Type == 'rect':
            pass

    elif object1Type == 'rect':
        pass
    elif object1Type == 'foo':
        return "bar"

    else:
        return print("Please specify a valid object type for object 1")

def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

### Display game update ###
def display_update(*args, **kwargs):
    for arg in args:
        arg

    pygame.display.update()
