from lib2to3.pytree import convert

import math
def dms_to_dd(degres, minutes, secondes):
    Convert = degres + minutes/60 + secondes/3600
    return convert


def distance_deux_points(point1, point2, point3, point4):
    Formule_distance = math.sqrt((point2-point1)**2 + (point4-point3)**2)
    return Formule_distance


