#!/usr/bin/env python

from random import randint

n = input()

l = []
print(n)
while len(l) < n:
    pair = (randint(1, 100), randint(1, 100))
    if pair not in l:
        l.append(pair)

for p in l:
    print("%d %d" % p)
