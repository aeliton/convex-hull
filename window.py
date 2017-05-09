#!/usr/bin/env python3

import ch
import pygame
import sys

pygame.init()

CANVASSIZE = 600 + 40

# set up the window
DISPLAYSURF = pygame.display.set_mode((CANVASSIZE, CANVASSIZE), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)

c1 = 235
c2 = 235
c3 = 235


def off(x):
    return x * 5 + 10


def draw(hull):
    global c1, c2, c3
    if c2 == 0:
        c1 = c1 - 10 if c1 - 10 > 0 else 0
    if c3 == 0:
        c2 = c2 - 10 if c2 - 10 > 0 else 0
    c3 = c3 - 10 if c3 - 10 > 0 else 0
    rgb = (c1, c2, c3)
    print(rgb)
    x2, y2 = [off(x) for x in hull[0]]
    for i in range(1, len(hull)):
        x1, y1 = [off(x) for x in hull[i]]
        p1 = (x1, CANVASSIZE - y1)
        p2 = (x2, CANVASSIZE - y2)
        pygame.draw.line(DISPLAYSURF, rgb, p1, p2, 1)
        x2, y2 = [off(x) for x in hull[i]]
    x1, y1 = [off(x) for x in hull[0]]
    p1 = (x1, CANVASSIZE - y1)
    p2 = (x2, CANVASSIZE - y2)
    pygame.draw.line(DISPLAYSURF, rgb, p1, p2, 1)


hulls = []


def append_hull(hull):
    hulls.append(hull)


n = int(input())
points = []

for i in range(0, int(n)):
    ent = input().split(" ")
    a, b = [int(s) for s in ent]
    pygame.draw.circle(DISPLAYSURF, BLUE, (off(a), CANVASSIZE - off(b)), 1, 0)
    points.append([a, b])

ch.convex_hull2(points, append_hull)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif len(hulls) > 0 and event.type == pygame.KEYUP:
            hull = hulls.pop(0)
            print(hull)
            draw(hull)
    pygame.display.update()
