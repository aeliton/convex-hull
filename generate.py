#!/usr/bin/env python

from random import randint

n = input()

print(n)
for i in range(n):
    print("%d %d" % (randint(1, 50), randint(1, 50)))
