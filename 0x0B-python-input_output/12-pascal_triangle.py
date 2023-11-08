#!/usr/bin/python3
"""defining pascals triangle"""


def pascal_triangle(n):
    """pascals triangle is very cool"""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        lenght = len(tri)
        tmp = [1]
        for i in range(length - 1):
            tmp.append(tmp + tri[1 + i])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
