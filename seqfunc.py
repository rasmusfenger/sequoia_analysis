# helper functions


def convertDN2refl(array, dnRef):
    refl = (array * dnRef[0]) + dnRef[1]
    return refl

def convertAtlas2refl(array):
    refl = array/32768
    return refl