#!/usr/bin/env python3

points = []

MAX = 10001
MIN = -1


def insert(points, p):
    """ Inserts p in the points list.
    """
    position = len(points) + 1
    for i in range(0, len(points)):
        if points[i][0] > p[0]:
            position = i
            break
    return points.insert(position, p)


def get_point(points, cmp, axis):
    """ Get a point based on values of either x or y axys.

    :cmp: Integer less than or greater than 0, representing respectively
    < and > singhs.
    :returns: a points attending the parameters restrictions.
    """
    if cmp < 0:
        inf = MAX
    else:
        inf = MIN

    point = [0, inf]
    for p in points:
        if p[axis] > point[axis]:
            point = p
    return point


def higher_y(points):
    return get_point(points, 1, 1)


def lower_y(points):
    return get_point(points, -1, 1)


def higher_x(points):
    return get_point(points, 1, 0)


def lower_x(points):
    return get_point(points, -1, 0)


def split(list):
    l = []
    r = []

    lx = lower_x(list)
    hx = higher_x(list)

    midle = (hx[0] - lx[0])/2

    for p in list:
        if p[0] < midle:
            l.append(p)
        else:
            r.append(p)

    return l, r


def f(left_p, right_p, x):
    a = (right_p[1] - left_p[1])/(right_p[0] - left_p[0])
    return a*x + (left_p[1] - a*left_p[0])


def points_to_connect_upper(left, right):
    """Determine which points must be connected on the upper bound of left and
    right points list.

    :returns: the uppermost point of left and right

    """
    left_p = higher_y(left)
    right_p = higher_y(right)

    if left_p[1] >= right_p[1]:
        for p in left:
            if left_p[0] <= p[0] and p[0] < right_p[0] and p[1] >= f(p[0]):
                left_p = p

    if left_p[1] <= right_p[1]:
        for p in right:
            if left_p[0] <= p[0] and p[0] < right_p[0] and p[1] >= f(p[0]):
                right_p = p

    return left_p, right_p


def points_to_connect_lower(left, right):
    """Determine which points must be connected on the lower bound of left and
    right points list.

    :returns: the lowermost point of left and right

    """
    left_p = higher_y(left)
    right_p = higher_y(right)

    if left_p[1] >= right_p[1]:
        for p in left:
            if left_p[0] <= p[0] and p[0] < right_p[0] and p[1] >= f(p[0]):
                left_p = p

    if left_p[1] <= right_p[1]:
        for p in right:
            if left_p[0] <= p[0] and p[0] < right_p[0] and p[1] >= f(p[0]):
                right_p = p

    return left_p, right_p


def combine(left, right):
    upper_l, upper_r = points_to_connect_upper(left, right)
    lower_l, lower_r = points_to_connect_lower(left, right)

    # get the points on the left side of lower left and upper left
    for i in range(len(left)):
        if left[i] == lower_l:
            break

    hull = []
    while left[i] != upper_l:
        hull.append(left[i])
        i = i-1 if i > 0 else len(left)
    hull.append(upper_l)

    # get the points on the right side of upper right and lower right
    for i in range(len(right)):
        if right[i] == upper_r:
            break

    while right[i] != lower_r:
        hull.append(right[i])
        i = i+1 if i < len(right) else 0
    hull.append(lower_r)

    return hull


def ch(l):
    l = ch(l[:len(l)/2])
    r = ch(l[len(l)/2:])
    return combine(l, r)


n = int(input())
print(n)

for i in range(0, int(n)):
    a, b = [int(s) for s in input().split(" ")]
    insert(points, [a, b, i])


print(points)
