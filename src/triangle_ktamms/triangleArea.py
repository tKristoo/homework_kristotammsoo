def areaOfTriangle(b, h):
    if (b > 0 and h > 0):
        return 0.5 * b * h
    else:
        raise Exception("Inputted parameter must not be lass than zero.")