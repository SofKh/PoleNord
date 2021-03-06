
# Importation de la formule (distance entre 2 points utilisée par la suite de l'exercice)

import math

# créer la fonction pour obtenir la conversion de la position Dms en Dd
def dms_to_dd(position):
    degres, minutes, secondes = position
    return degres + minutes / 60 + secondes / 3600

# Créer la fonction pour obtenir la distance entre deux points

def distance_deux_points(point1, point2, point3, point4):
    Formule_distance = math.sqrt((point2-point1)**2 + (point4-point3)**2)
    return Formule_distance

# Exemple avec la position de la ville de Montreal

POLE_NORD_X = 86, 29, 38
POLE_NORD_Y = 172, 52, 1
MONTREAL_X = 45, 30, 31
MONTREAL_Y = 73, 35, 16
polenord_dmsX = dms_to_dd(POLE_NORD_X)
polenord_dmsY = dms_to_dd(POLE_NORD_Y)
montreal_dmsX = dms_to_dd(MONTREAL_X)
montreal_dmsY = dms_to_dd(MONTREAL_Y)

print(polenord_dmsX, polenord_dmsY)
print(montreal_dmsX, montreal_dmsY)
print(distance_deux_points(polenord_dmsX, polenord_dmsY, montreal_dmsX, montreal_dmsY))



