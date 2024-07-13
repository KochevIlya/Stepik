points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

def pnt_dstns(crdnts):
    return (crdnts[0]**2 + crdnts[1]**2) ** (1/2)

print(sorted(points, key=pnt_dstns))