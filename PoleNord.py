from lib2to3.pytree import convert


def dms_to_dd(degres, minutes, secondes):
    Convert = degres + minutes/60 + secondes/3600
    return convert



