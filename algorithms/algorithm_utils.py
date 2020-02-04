from operator import attrgetter
import math

def get_lowest_f_node(array):

    min_f = min(array, key = attrgetter("fScore"))
    return min_f


# distance from current node and start node
def find_g(current, start_pos):
    g = get_distance(current, start_pos)
    return g


# distance from current node and target / destination / finish node
def find_h(current, end_pos):

    dx = abs(current.x - end_pos.x)
    dy = abs(current.y - end_pos.y)

    D = 1
    D2 = 1
    h = D * ((dx + dy) + (D2 - 2 * D) * min(dx, dy))

    return h


# hscore and gscore added together
def find_f(score1, score2):
    return score1 + score2


# distance from 2 points. also the hueristics, which is causing issues
def get_distance(start, end):
    x1 = start.x
    y1 = start.y
    x2 = end.x
    y2 = end.y
    distancex = sqr(x2 - x1)
    distancey = sqr(y2 - y1)
    distance = sqrt(distancex + distancey)
    distance = distancex + distancey
    return distance


def sqr(number):
    return number * number


def sqrt(number):
    return math.sqrt(number)
