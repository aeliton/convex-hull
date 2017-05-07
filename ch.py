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


def f(left_p, right_p, x):
    a = (right_p[1] - left_p[1])/(right_p[0] - left_p[0])
    return a*x + (left_p[1] - a*left_p[0])


def above(left_p, right_p, point):
    """Tells a given point is above or not the function func.
    """
    return point[1] > f(left_p, right_p, point[0])


def below(left_p, right_p, point):
    """Tells a given point is above or not the function func.
    """
    return point[1] < f(left_p, right_p, point[0])


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
        while above(left[l], right[r], left[next(left, l)]):
            l = next(left, l)
        while below(left[l], right[next(right, r)], right[r]):
            r = next(right, r)

    if left[l][1] <= right[r][1]:
        while above(left[l], right[r], right[prev(right, r)]):
            r = prev(right, r)
        while below(left[l], left[prev(left, l)], right[r]):
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
        while below(left[l], right[r], right[next(right, r)]):
            r = next(right, r)
        while above(left[next(left, l)], right[r], left[l]):
            l = next(left, l)

    if left[l][1] <= right[r][1]:
        while below(left[l], right[r], left[prev(left, l)]):
            l = prev(left, l)
        while above(left[l], right[prev(right, r)], right[r]):
            r = prev(right, r)

    return l, r


def combine(left, right):
    upper_l, upper_r = points_to_connect_upper(left, right)
    lower_l, lower_r = points_to_connect_lower(left, right)

    hull = []

    i = lower_l
    while True:
        hull.append(left[i])
        if i == upper_l:
            break
        i = next(left, i)

    i = upper_r
    while True:
        hull.append(right[i])
        if i == lower_r:
            break
        i = next(right, i)

    return hull


def ch(l):
    if len(l) == 1:
        return l
    l = ch(l[:len(l)/2])
    r = ch(l[len(l)/2:])
    return combine(l, r)


# n = int(input())
# print(n)

# for i in range(0, int(n)):
    # a, b = [int(s) for s in input().split(" ")]
    # insert(points, [a, b, i])


# print(points)
