#!/usr/bin/env python

import ch
import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((540, 540), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)

def off(x):
    return x * 10 + 10

def draw(hull):
    x2, y2 = [off(x) for x in hull[0]]
    for i in range(1, len(hull)):
        x1, y1 = [off(x) for x in hull[i]]
        pygame.draw.line(DISPLAYSURF, RED, (x1, 540 - y1), (x2, 540 - y2), 1)
        x2, y2 = [off(x) for x in hull[i]]
    x1, y1 = [off(x) for x in hull[0]]
    pygame.draw.line(DISPLAYSURF, RED, (x1, 540 - y1), (x2, 540 - y2), 1)


hulls = []


def append_hull(hull):
    hulls.append(hull)


n = int(input())
points = []

for i in range(0, int(n)):
    ent = raw_input().split(" ")
    a, b = [int(s) for s in ent]
    pygame.draw.circle(DISPLAYSURF, BLUE, (off(a), 540 - off(b)), 1, 0)
    points.append([a, b])

ch.convex_hull2(points, append_hull)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif len(hulls) > 0 and event.type == pygame.KEYUP:
            hull = hulls.pop(0)
            print(hull)
            draw(hull)
    pygame.display.update()
