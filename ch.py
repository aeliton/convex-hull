#!/usr/bin/env python3

from functools import cmp_to_key

points = []

MAX = 10001
MIN = -1


def get_point(points, cmp, axis):
    """ Get a point based on values of either x or y axys.

    :cmp: Integer less than or greater than 0, representing respectively
    < and > singhs.
    :returns: the index of the point matching the constraints
    """
    index = 0
    for i in range(len(points)):
        if cmp < 0:
            if points[i][axis] < points[index][axis]:
                index = i
        else:
            if points[i][axis] > points[index][axis]:
                index = i

    return index


def higher_y(points):
    return get_point(points, 1, 1)


def lower_y(points):
    return get_point(points, -1, 1)


def f(p1, p2, x):
    return ((p2[1] - p1[1])*x + (p2[0]*p1[1] - p1[0]*p2[1]))/(p2[0] - p1[0])


def above(left_p, right_p, point):
    """Tells a given point is above or not the function func.
    """
    return False if left_p[0] == right_p[0] else point[1] > f(left_p, right_p,
                                                              point[0])


def below(left_p, right_p, point):
    """Tells a given point is above or not the function func.
    """
    return False if left_p[0] == right_p[0] else point[1] < f(left_p, right_p,
                                                              point[0])


def next(points, index):
    return index + 1 if index < len(points) - 1 else 0


def prev(points, index):
    return index - 1 if index > 0 else len(points) - 1


def points_to_connect_upper(left, right):
    """Determine which points must be connected on the upper bound of left and
    right points list.

    :returns: the uppermost point of left and right

    """
    # indexes
    l = higher_y(left)
    r = higher_y(right)

    if left[l][1] >= right[r][1]:
        next_l = next(left, l)
        while l != next_l and above(left[l], right[r], left[next_l]):
            l = next_l
        next_r = next(right, r)
        while r != next_r and below(left[l], right[next_r], right[r]):
            r = next_r

    if left[l][1] <= right[r][1]:
        prev_r = prev(right, r)
        while r != prev_r and above(left[l], right[r], right[prev_r]):
            r = prev_r
        prev_l = prev(left, l)
        while l != prev_l and below(left[prev_l], right[r], left[l]):
            l = prev(left, l)

    return l, r


def points_to_connect_lower(left, right):
    """Determine which points must be connected on the upper bound of left and
    right points list.

    :returns: the uppermost point of left and right

    """
    # indexes
    l = lower_y(left)
    r = lower_y(right)

    if left[l][1] >= right[r][1]:
        next_r = next(right, r)
        while r != next_r and below(left[l], right[r], right[next_r]):
            r = next_r
        next_l = next(left, l)
        while l != next_l and above(left[next_l], right[r], left[l]):
            l = next_l

    if left[l][1] <= right[r][1]:
        prev_l = prev(left, l)
        while l != prev_l and below(left[l], right[r], left[prev_l]):
            l = prev_l
        prev_r = prev(right, r)
        while r != prev_r and above(left[l], right[prev_r], right[r]):
            r = prev_r

    return l, r


def combine(left, right):
    upper_l, upper_r = points_to_connect_upper(left, right)
    lower_l, lower_r = points_to_connect_lower(left, right)

    hull = []

    if lower_l == upper_l:
        hull.append(left[lower_l])
    else:
        i = lower_l
        while True:
            hull.append(left[i])
            if i == upper_l:
                break
            i = next(left, i)

    if lower_r == upper_r:
        hull.append(right[lower_r])
    else:
        i = upper_r
        while True:
            hull.append(right[i])
            if i == lower_r:
                break
            i = next(right, i)

    return hull


def ch(points):
    if len(points) == 1:
        return points
    left = ch(points[:len(points)//2])
    right = ch(points[len(points)//2:])
    return combine(left, right)


def ch2(points, draw):
    if len(points) == 1:
        return points
    left = ch2(points[:len(points)//2], draw)
    right = ch2(points[len(points)//2:], draw)
    hull = combine(left, right)
    draw(hull)
    return hull


def cmp(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return a[0] - b[0]


def sort(points):
    return sorted(points, key=cmp_to_key(cmp))


def convex_hull2(points, draw):
    return ch2(sort(points), draw)


def convex_hull(points):
    return ch(sort(points))
