from lib2to3.pytree import convert

import math
def dms_to_dd(degres, minutes, secondes):
    Convert = degres + minutes/60 + secondes/3600
    return convert


def distance_deux_points(point1, point2, point3, point4):
    Formule_distance = math.sqrt((point2-point1)**2 + (point4-point3)**2)
    return Formule_distance

POLE_NORD_X = 86, 0, 0
POLE_NORD_Y = 172, 0, 0
MONTREAL_X = 45, 30, 31
MONTREAL_Y = 73, 35, 16

polenord_dmsX = dms_to_dd(POLE_NORD_X)
polenord_dmsY = dms_to_dd(POLE_NORD_Y)
montreal_dmsX = dms_to_dd(MONTREAL_X)
montreal_dmsY = dms_to_dd(MONTREAL_Y)

print(polenord_dmsX, polenord_dmsY)
print(montreal_dmsX, montreal_dmsY)
print(distance_deux_points(polenord_dmsX, polenord_dmsY, montreal_dmsX, montreal_dmsY))



